import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from flask import Flask, jsonify

app = Flask(__name__)
node = None

@app.route('/ros_topic_data', methods=['GET'])
def ros_topic_data():
    global node
    if node is None:
        return jsonify({'message': 'ROS node is not initialized'})

    # Callback function to handle received messages
    def callback(msg):
        return jsonify({'data': msg.data})

    # Create a subscriber to a ROS topic
    subscriber = node.create_subscription(
        String,
        'my_topic',
        callback,
        10  # QoS profile
    )

    return jsonify({'message': 'ROS topic listener started'})


class ROSNode(Node):
    def __init__(self):
        super().__init__('ros_flask_node')

        # ROS publisher
        self.publisher_ = self.create_publisher(String, 'my_topic', 10)

        # Flask route for publishing data to ROS topic
        @app.route('/publish_data', methods=['POST'])
        def publish_data():
            # data = request.json
            data = ""
            if 'data' in data:
                msg = String()
                msg.data = data['data']
                self.publisher_.publish(msg)
                return jsonify({'message': 'Data published to ROS topic'})
            else:
                return jsonify({'error': 'Data field missing'})

def main():
    global node
    rclpy.init()
    node = ROSNode()

    # Start Flask app
    app.run(debug=True, use_reloader=False, port=5000)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
