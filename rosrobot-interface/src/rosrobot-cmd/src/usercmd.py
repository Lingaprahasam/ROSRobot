import rospy

from std_msgs.msg import String



def usercmd():

    rospy.init_node('usercmd', anonymous=True)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        # Listen to user command
        _usercmd = raw_input()
        

        # Write it on ros parameter server



        rate.sleep()

if __name__ == '__main__':

    try:

        usercmd()

    except rospy.ROSInterruptException:

        pass