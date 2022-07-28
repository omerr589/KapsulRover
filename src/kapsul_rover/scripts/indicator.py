#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Bool

def indicator():
    pub = rospy.Publisher('role', Bool, queue_size=10)
    rospy.init_node('indicator', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(True)
        pub.publish(True)
        rate.sleep()

if __name__ == '__main__':
    try:
        indicator()
    except rospy.ROSInterruptException:
        pass