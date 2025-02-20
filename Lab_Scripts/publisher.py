import rospy
from std_msgs.msg import String

def publisher():
  rospy.init_node('publisher_node')
  pub = rospy.Publisher('publisher_1', String, queue_size=10)
  rate = rospy.Rate(5)

  i = 0
  while not rospy.is_shutdown():
    msg = "hello world %s" % i
    rospy.loginfo(msg)
    pub.publish(msg)
    i+=1
    rate.sleep()

if __name__ == '__main__':
  try:
    publisher()
  except rospy.ROSInterruptException:
    pass