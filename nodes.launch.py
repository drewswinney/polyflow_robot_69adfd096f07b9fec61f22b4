import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69b5b255145f6cae225f9dcd",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69b5b255145f6cae225f9dcd",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint":"69b41631c5096273c88f9861","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":-180,"limit.upper_position":180,"limit.position_step":0.1,"limit.max_effort":50,"limit.effort_step":0.1,"limit.max_velocity":720,"limit.velocity_step":0.1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:/joint/state","name":"/joint/state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:/joint_controller/command","name":"/joint_controller/command","direction":"input","msg_type":"trajectory_msgs/JointTrajectory"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69bf479ee33d16f41fbf6c34",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69bf479ee33d16f41fbf6c34",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint_id":null,"transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":null,"limit.upper_position":null,"limit.position_step":null,"limit.max_effort":null,"limit.effort_step":null,"limit.max_velocity":null,"limit.velocity_step":null}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:state","name":"state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:trajectory","name":"trajectory","direction":"input","msg_type":"trajectory_msgs/JointTrajectoryPoint"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
    ])