# Copyright (c) 2020, Danish Technological Institute.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from ur.ur_communicator import URCommunicator

host = "10.224.60.30"
firmware_version = 1.8

ur_sock = URCommunicator(host, firmware_version)

data = ur_sock.recv_handler()

print(data['tool_vector'])
