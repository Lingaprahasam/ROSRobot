import sys

from rosrobot_interfaces.srv import RobotInfoSrv
import rclpy
from rclpy.node import Node


class RobotInfoClientAsync(Node):

    def __init__(self):
        super().__init__('robot_info_client_async')
        self.cli = self.create_client(RobotInfoSrv, 'robot_info_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('robot_info_service is not available, waiting again...')
        self.req = RobotInfoSrv.Request()

    def send_request(self):
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    robot_info_client = RobotInfoClientAsync()
    response = robot_info_client.send_request()
    print(response)
    # robot_info_client.get_logger().info(response)

    robot_info_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()