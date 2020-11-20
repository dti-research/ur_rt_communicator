# Copyright (c) 2020, Danish Technological Institute.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import socket
import time
import sys
import logging
import numpy as np
from . import ur_utils
from threading import Lock

# Setup logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


class URCommunicator():
    """URCommunicator class for UR5 robot.

    This class implements UR-robot specific packet URCommunicator.
    The packets it receives from UR-robot is of type
    `ur_utils.REALTIME_COMM_PACKET`.
    """

    def __init__(self, host, firmware_version,
                 disable_nagle_algorithm=True,
                 ):
        """Inits URCommunicator class with device- and task-specific parameters.

        Args:
            host: a string specifying UR Controller IP address
            firmware_version: a float specifying UR Controller firmware version
            disable_nagle_algorithm: a boolean specifying a parameter in
                socket class
        """
        self._host = host
        self._firmware_version = firmware_version
        self._disable_nagle_algorithm = disable_nagle_algorithm

        # The number of sensor reads since the last actuator write
        self._num_reads = 0
        self._num_read_lock = Lock()

        # make connections
        self._sock = URCommunicator.make_connection(
            self._host,
            port=ur_utils.REALTIME_COMM_CLIENT_INTERFACE_PORT,
            disable_nagle_algorithm=self._disable_nagle_algorithm
        )
        logging.debug('Socket Info: {}'.format(self._sock))
        self._sock.settimeout(0.2)

        self._dashboard_sock = URCommunicator.make_connection(
            host=self._host,
            port=ur_utils.DASHBOARD_SERVER_PORT,
            disable_nagle_algorithm=self._disable_nagle_algorithm
        )
        time.sleep(0.5)

        self._start_time = time.time()
        self._recv_time = self._start_time
        self._prev_recv_time = self._start_time

        # DEBUG:
        logging.debug('Start time: {}'.format(self._start_time))

    def recv_handler(self):
        """Receives and stores sensory packets from the UR.

        Waits for packets to arrive from UR-robot through `socket.recv` call,
        checks for any delay in transmission.
        This method also handles re-establishing of a lost connection.

        Raises:
            IOError, ValueError - data convertion errors.
        """

        try:
            REALTIME_COMM_PACKET = ur_utils.get_rt_packet_def(
                self._firmware_version)

            data = self._sock.recv(
                ur_utils.get_rt_packet_size(self._firmware_version))
            self._recv_time = time.time()  # time after receiving packet

            # To fix CB2 issue
            data = data.ljust(REALTIME_COMM_PACKET.itemsize, b'\0')

            # check and parse received packet
            self.pre_check(data)

            parsed = np.frombuffer(data, dtype=REALTIME_COMM_PACKET)

            self._prev_recv_time = self._recv_time
            self._num_read_lock.acquire()
            self._num_reads += 1
            self._num_read_lock.release()

            return parsed
        except (IOError, ValueError):
            self._stop = True
            self._sock.close()
            self._dashboard_sock.close()

            self._sock = self.make_connection(
                self._host,
                ur_utils.REALTIME_COMM_CLIENT_INTERFACE_PORT,
                disable_nagle_algorithm=self._disable_nagle_algorithm)

            self._dashboard_sock = self.make_connection(
                self._host,
                ur_utils.DASHBOARD_SERVER_PORT,
                disable_nagle_algorithm=self._disable_nagle_algorithm)

            self._stop = False
        except Exception:
            raise

    def pre_check(self, data):
        """Checks time and completeness of packet reception.

        Args:
            data: a numpy array with sensory information received from UR5
        """

        REALTIME_COMM_PACKET = ur_utils.get_rt_packet_def(
            self._firmware_version)

        if self._recv_time > self._prev_recv_time + 1.1 / 125:
            logging.debug(
                '{}: Hiccup of {:.2f}ms overhead between UR packets)'.format(
                    self._recv_time - self._start_time,
                    (self._recv_time - self._prev_recv_time - 0.008) * 1000,
                ))
        if len(data) != REALTIME_COMM_PACKET.itemsize:
            logging.debug('Warning: incomplete packet from UR')
            return

    @staticmethod
    def make_connection(host, port, disable_nagle_algorithm):
        """Establishes a TCP/IP socket connection with a UR5 controller.

        Args:
            host: a string specifying UR5 Controller IP address
            port: a string specifying UR5 Controller port
            disable_nagle_algorithm: a boolean specifying whether to
                disable nagle algorithm

        Returns:
             None or TCP socket connected to UR5 device.
        """
        sock = None
        for res in socket.getaddrinfo(host,
                                      port,
                                      socket.AF_UNSPEC,
                                      socket.SOCK_STREAM):
            afam, socktype, proto, canonname, sock_addr = res
            del canonname
            try:
                sock = socket.socket(afam, socktype, proto)
                if disable_nagle_algorithm:
                    sock.setsockopt(socket.IPPROTO_TCP,
                                    socket.TCP_NODELAY, True)
            except OSError as msg:
                logging.debug(msg)
                sock = None
                continue
            try:
                sock.connect(sock_addr)
            except OSError as msg:
                logging.debug(msg)
                sock.close()
                sock = None
                continue
            break
        return sock
