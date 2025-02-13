import rospy
from std_msgs.msg import String

def process_subscriber_msg(data):
  print('Message received: ' + str(data))


def create_subscriber():
  rospy.init_node('subscriber_node')
  rospy.Subscriber("publisher_1", String, callback)


if __name__ == '__main__':
  create_subscriber()
  rospy.spin() # Keeps the script running until the node is stopped
  rospy.loginfo("Subscriber node started")
    