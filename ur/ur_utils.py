# Copyright (c) 2020, Danish Technological Institute.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np

DASHBOARD_SERVER_PORT = 29999  # to unlock protective stop
PRIMARY_CLIENT_INTERFACE_PORT = 30001
SECONDARY_CLIENT_INTERFACE_PORT = 30002
REALTIME_COMM_CLIENT_INTERFACE_PORT = 30003
RTDE_COMM_CLIENT_INTERFACE_PORT = 30004

def get_rt_packet_size(firmware_version):
    if firmware_version >= 3.10 or firmware_version >= 5.4:
        REALTIME_COMM_PACKET_SIZE = 1116
    elif firmware_version >= 3.5 and firmware_version <= 5.4:
        REALTIME_COMM_PACKET_SIZE = 1108
    elif firmware_version >= 3.2:
        REALTIME_COMM_PACKET_SIZE = 1060
    elif firmware_version >= 3.0:
        REALTIME_COMM_PACKET_SIZE = 1044
    elif firmware_version >= 1.8:
        REALTIME_COMM_PACKET_SIZE = 812
    elif firmware_version >= 1.7:
        REALTIME_COMM_PACKET_SIZE = 764
    else:
        REALTIME_COMM_PACKET_SIZE = 756
    return REALTIME_COMM_PACKET_SIZE

def get_rt_packet_def(firmware_version):
    if firmware_version >= 3.10 or firmware_version >= 5.4:
        REALTIME_COMM_PACKET = np.dtype(
        [('message_size', '>i4'),
        ('time', '>f8'),
        ('q_target', '>f8', (6,)),
        ('qd_target', '>f8', (6,)),
        ('qdd_target', '>f8', (6,)),
        ('i_target', '>f8', (6,)),
        ('m_target', '>f8', (6,)),
        ('q_actual', '>f8', (6,)),
        ('qd_actual', '>f8', (6,)),
        ('i_actual', '>f8', (6,)),
        ('i_control', '>f8', (6,)),
        ('tool_vector_actual', '>f8', (6,)),
        ('tcp_speed_actual', '>f8', (6,)),
        ('tcp_force', '>f8', (6,)),
        ('tool_vector_target', '>f8', (6,)),
        ('tcp_speed_target', '>f8', (6,)),
        ('digital_input_bits', '>f8'),
        ('motor_temperatures', '>f8', (6,)),
        ('controller_timer', '>f8'),
        ('test_value', '>f8'),
        ('robot_mode', '>f8'),
        ('joint_modes', '>f8', (6,)),
        ('safety_mode', '>f8'),
        ('reserved_0', '>f8', (6,)),
        ('tool_accelerometer_values', '>f8', (3,)),
        ('reserved_1', '>f8', (6,)),
        ('speed_scaling', '>f8'),
        ('linear_momentum_norm', '>f8'),
        ('reserved_2', '>f8'),
        ('reserved_3', '>f8'),
        ('v_main', '>f8'),
        ('v_robot', '>f8'),
        ('i_robot', '>f8'),
        ('v_actual', '>f8', (6,)),
        ('digital_outputs', '>f8'),
        ('program_state', '>f8'),
        ('elbow_position', '>f8', (3,)),
        ('elbow_velocity', '>f8', (3,)),
        ('safety_status', '>f8')
        ])
    elif firmware_version >= 3.5 and firmware_version <= 5.4:
        REALTIME_COMM_PACKET = np.dtype(
        [('message_size', '>i4'),
        ('time', '>f8'),
        ('q_target', '>f8', (6,)),
        ('qd_target', '>f8', (6,)),
        ('qdd_target', '>f8', (6,)),
        ('i_target', '>f8', (6,)),
        ('m_target', '>f8', (6,)),
        ('q_actual', '>f8', (6,)),
        ('qd_actual', '>f8', (6,)),
        ('i_actual', '>f8', (6,)),
        ('i_control', '>f8', (6,)),
        ('tool_vector_actual', '>f8', (6,)),
        ('tcp_speed_actual', '>f8', (6,)),
        ('tcp_force', '>f8', (6,)),
        ('tool_vector_target', '>f8', (6,)),
        ('tcp_speed_target', '>f8', (6,)),
        ('digital_input_bits', '>f8'),
        ('motor_temperatures', '>f8', (6,)),
        ('controller_timer', '>f8'),
        ('test_value', '>f8'),
        ('robot_mode', '>f8'),
        ('joint_modes', '>f8', (6,)),
        ('safety_mode', '>f8'),
        ('reserved_0', '>f8', (6,)),
        ('tool_accelerometer_values', '>f8', (3,)),
        ('reserved_1', '>f8', (6,)),
        ('speed_scaling', '>f8'),
        ('linear_momentum_norm', '>f8'),
        ('reserved_2', '>f8'),
        ('reserved_3', '>f8'),
        ('v_main', '>f8'),
        ('v_robot', '>f8'),
        ('i_robot', '>f8'),
        ('v_actual', '>f8', (6,)),
        ('digital_outputs', '>f8'),
        ('program_state', '>f8'),
        ('elbow_position', '>f8', (3,)),
        ('elbow_velocity', '>f8', (3,)),
        ])
    elif firmware_version >= 3.2:
        REALTIME_COMM_PACKET = np.dtype(
        [('message_size', '>i4'),
        ('time', '>f8'),
        ('q_target', '>f8', (6,)),
        ('qd_target', '>f8', (6,)),
        ('qdd_target', '>f8', (6,)),
        ('i_target', '>f8', (6,)),
        ('m_target', '>f8', (6,)),
        ('q_actual', '>f8', (6,)),
        ('qd_actual', '>f8', (6,)),
        ('i_actual', '>f8', (6,)),
        ('i_control', '>f8', (6,)),
        ('tool_vector_actual', '>f8', (6,)),
        ('tcp_speed_actual', '>f8', (6,)),
        ('tcp_force', '>f8', (6,)),
        ('tool_vector_target', '>f8', (6,)),
        ('tcp_speed_target', '>f8', (6,)),
        ('digital_input_bits', '>f8'),
        ('motor_temperatures', '>f8', (6,)),
        ('controller_timer', '>f8'),
        ('test_value', '>f8'),
        ('robot_mode', '>f8'),
        ('joint_modes', '>f8', (6,)),
        ('safety_mode', '>f8'),
        ('reserved_0', '>f8', (6,)),
        ('tool_accelerometer_values', '>f8', (3,)),
        ('reserved_1', '>f8', (6,)),
        ('speed_scaling', '>f8'),
        ('linear_momentum_norm', '>f8'),
        ('reserved_2', '>f8'),
        ('reserved_3', '>f8'),
        ('v_main', '>f8'),
        ('v_robot', '>f8'),
        ('i_robot', '>f8'),
        ('v_actual', '>f8', (6,)),
        ('digital_outputs', '>f8'),
        ('program_state', '>f8'),
        ])
    elif firmware_version >= 3.0:
        REALTIME_COMM_PACKET = np.dtype(
        [('message_size', '>i4'),
        ('time', '>f8'),
        ('q_target', '>f8', (6,)),
        ('qd_target', '>f8', (6,)),
        ('qdd_target', '>f8', (6,)),
        ('i_target', '>f8', (6,)),
        ('m_target', '>f8', (6,)),
        ('q_actual', '>f8', (6,)),
        ('qd_actual', '>f8', (6,)),
        ('i_actual', '>f8', (6,)),
        ('i_control', '>f8', (6,)),
        ('tool_vector_actual', '>f8', (6,)),
        ('tcp_speed_actual', '>f8', (6,)),
        ('tcp_force', '>f8', (6,)),
        ('tool_vector_target', '>f8', (6,)),
        ('tcp_speed_target', '>f8', (6,)),
        ('digital_input_bits', '>f8'),
        ('motor_temperatures', '>f8', (6,)),
        ('controller_timer', '>f8'),
        ('test_value', '>f8'),
        ('robot_mode', '>f8'),
        ('joint_modes', '>f8', (6,)),
        ('safety_mode', '>f8'),
        ('reserved_0', '>f8', (6,)),
        ('tool_accelerometer_values', '>f8', (3,)),
        ('reserved_1', '>f8', (6,)),
        ('speed_scaling', '>f8'),
        ('linear_momentum_norm', '>f8'),
        ('reserved_2', '>f8'),
        ('reserved_3', '>f8'),
        ('v_main', '>f8'),
        ('v_robot', '>f8'),
        ('i_robot', '>f8'),
        ('v_actual', '>f8', (6,)),
        ])
    elif firmware_version >= 1.8:
        REALTIME_COMM_PACKET = np.dtype(
        [('message_size', '>i4'),
        ('time', '>f8'),
        ('q_target', '>f8', (6,)),
        ('qd_target', '>f8', (6,)),
        ('qdd_target', '>f8', (6,)),
        ('i_target', '>f8', (6,)),
        ('m_target', '>f8', (6,)),
        ('q_actual', '>f8', (6,)),
        ('qd_actual', '>f8', (6,)),
        ('i_actual', '>f8', (6,)),
        ('tool_accelerometer_values', '>f8', (3,)),
        ('unused', '>f8', (15,)),
        ('tcp_force', '>f8', (6,)),
        ('tool_vector', '>f8', (6,)),
        ('tcp_speed', '>f8', (6,)),
        ('digital_input_bits', '>f8'),
        ('motor_temperatures', '>f8', (6,)),
        ('controller_timer', '>f8'),
        ('test_value', '>f8'),
        ('robot_mode', '>f8'),
        ('joint_modes', '>f8', (6,)),
        ])
    elif firmware_version >= 1.7:
        REALTIME_COMM_PACKET = np.dtype(
        [('message_size', '>i4'),
        ('time', '>f8'),
        ('q_target', '>f8', (6,)),
        ('qd_target', '>f8', (6,)),
        ('qdd_target', '>f8', (6,)),
        ('i_target', '>f8', (6,)),
        ('m_target', '>f8', (6,)),
        ('q_actual', '>f8', (6,)),
        ('qd_actual', '>f8', (6,)),
        ('i_actual', '>f8', (6,)),
        ('tool_accelerometer_values', '>f8', (3,)),
        ('unused', '>f8', (15,)),
        ('tcp_force', '>f8', (6,)),
        ('tool_vector', '>f8', (6,)),
        ('tcp_speed', '>f8', (6,)),
        ('digital_input_bits', '>f8'),
        ('motor_temperatures', '>f8', (6,)),
        ('controller_timer', '>f8'),
        ('test_value', '>f8'),
        ('robot_mode', '>f8'),
        ])
    else:
        REALTIME_COMM_PACKET = np.dtype(
        [('message_size', '>i4'),
        ('time', '>f8'),
        ('q_target', '>f8', (6,)),
        ('qd_target', '>f8', (6,)),
        ('qdd_target', '>f8', (6,)),
        ('i_target', '>f8', (6,)),
        ('m_target', '>f8', (6,)),
        ('q_actual', '>f8', (6,)),
        ('qd_actual', '>f8', (6,)),
        ('i_actual', '>f8', (6,)),
        ('tool_accelerometer_values', '>f8', (3,)),
        ('unused', '>f8', (15,)),
        ('tcp_force', '>f8', (6,)),
        ('tool_vector', '>f8', (6,)),
        ('tcp_speed', '>f8', (6,)),
        ('digital_input_bits', '>f8'),
        ('motor_temperatures', '>f8', (6,)),
        ('controller_timer', '>f8'),
        ('test_value', '>f8'),
        ])
    
    return REALTIME_COMM_PACKET

class SafetyModes(object):
    """
    UR5 Safety Modes (for firmware 3.3, 3.4)
    """

    FAULT = 9
    VIOLATION = 8
    ROBOT_EMERGENCY_STOP = 7
    SYSTEM_EMERGENCY_STOP = 6
    SAFEGUARD_STOP = 5
    RECOVERY = 4
    PROTECTIVE_STOP = 3
    REDUCED = 2
    NORMAL = 1
    NONE = 0 # To fix CB2 issue
