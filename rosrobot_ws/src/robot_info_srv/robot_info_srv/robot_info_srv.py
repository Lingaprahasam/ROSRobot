import platform
import os
import json

import rclpy
from rclpy.node import Node

from rosrobot_interfaces.srv import RobotInfoSrv
from rosrobot_interfaces.msg import SystemInfo
from rosrobot_interfaces.msg import OSInfo
from rosrobot_interfaces.msg import ROSInfo

class RobotInfoService(Node):

    def __init__(self):
        super().__init__('robot_info_service')
        self.srv = self.create_service(RobotInfoSrv, 'robot_info_service', self.robot_info_service_callback)
        self.get_logger().info('robot_info_service is running')

    def robot_info_service_callback(self, request, response):
        self.system_info_msg = SystemInfo()
        _osInformation = OSInformation()
        _rosInformation = ROSInformation()
        
        # Get OS Info
        self.system_info_msg.os_info = _osInformation.getOSInfoMsg()
        # Get ROS Info
        self.system_info_msg.ros_info = _rosInformation.getROSInfoMsg()
        response.system_info = self.system_info_msg
        # self.get_logger().info('ros_domain_id is: %s' %response.system_info_msg.ros_info.ros_domain_id)

        return response

class RosHelper():
    def __init__(self):
        super().__init__()

    def json_to_osInfoMsg(self, json_data):        
        # parst json data
        data = json.loads(json_data)

        # ROS message type, 
        # Updating os info to robo info message
        os_info_msg = OSInfo()
        os_info_msg.name = data['name']
        os_info_msg.release = data['release']
        os_info_msg.processor = data['processor']
        os_info_msg.machine = data['machine']
        os_info_msg.network_name = data['network_name']

        return os_info_msg

class EnvVariables():
    def __init__(self):
        super().__init__()

    def getEnvVariable(self, envVarName):
        # Get the value of a specific environment variable
        envVarValue = os.environ.get(envVarName)

        if envVarValue:
            return envVarValue
        else:
            return None

class OSInformation():
    def __init__(self):
        super().__init__()
    
    def getOSInfo(self):
        # Get the operating system
        name = platform.system()
        release = platform.release()
        processor = platform.processor()
        machine = platform.machine()
        network_name = platform.node()

        if (name!=None):
            data = {
                "name": name,
                "release": release,
                "processor": processor,
                "machine": machine,
                "network_name": network_name
            }

            json_string = json.dumps(data)
            return json_string
        else:
            return {}
        
    def getOSInfoMsg(self):
        # Get OS Info
        os_info = self.getOSInfo()
        
        helper = RosHelper()
        os_info_msg = helper.json_to_osInfoMsg(os_info)
        return os_info_msg

class ROSInformation():
    def __init__(self):
        super().__init__()

    def getROSInfoMsg(self):
        envVariable = EnvVariables()
        _rosDistro = envVariable.getEnvVariable('ROS_DISTRO')
        _ros_domain_id = envVariable.getEnvVariable('ROS_DOMAIN_ID')

        _rosInfoMsg = ROSInfo()
        _rosInfoMsg.rosdistro = _rosDistro
        if(_ros_domain_id != None):
            _rosInfoMsg.ros_domain_id = int(_ros_domain_id)
        else:
            _rosInfoMsg.ros_domain_id = 0
        

        return _rosInfoMsg



def main():
    rclpy.init()

    robot_info_service = RobotInfoService()

    rclpy.spin(robot_info_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()