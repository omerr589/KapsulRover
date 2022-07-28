#!/usr/bin/python
import rospy 
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


def joy_to_cmd(msg):
    print(msg.axes[3]) 
    print(msg.axes[2]) 
    print('-----------  ')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    cmd = Twist()
    if abs(msg.axes[3]) > abs(msg.axes[2]):
        cmd.linear.x = msg.axes[3]
    elif abs(msg.axes[2]) > abs(msg.axes[3]):
        cmd.angular.z = msg.axes[2]

    pub.publish(cmd)


def joy_listener():
    rospy.init_node('listener_of_joy', anonymous=True)
    rospy.Subscriber("joy", Joy, joy_to_cmd)
    rospy.spin()



if __name__ == '__main__':
    
    try:
        joy_listener()
    except rospy.ROSInterruptException:
        pass

    