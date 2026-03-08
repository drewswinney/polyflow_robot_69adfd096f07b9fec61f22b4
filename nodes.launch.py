import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69adfd226f07b9fec61f22eb",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69adfd226f07b9fec61f22eb",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint":"69adfd126f07b9fec61f22d6","control_mode":"position","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":0,"limit.upper_position":360,"limit.position_step":null,"limit.max_effort":0,"limit.effort_step":0.1,"limit.max_velocity":0,"limit.velocity_step":0.1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"6976bda65eb68f72bfec9b31:/joint/state","name":"/joint/state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"6976bda65eb68f72bfec9b31:/joint_controller/command","name":"/joint_controller/command","direction":"input","msg_type":"trajectory_msgs/JointTrajectory"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
    ])