#!/usr/bin/env python
import rospy

startcmd = "start"
stopcmd = "stop"

def statecmd():
    #rospy.init_node('statecmd', anonymous=True)
    #rate = rospy.Rate(10) # 10hz

    #while not rospy.is_shutdown():
        print ('Enter robot state command "start" or "stop"')
        state = raw_input()

        # Takes care of upper case and mixed case and endof line space character
        if (startcmd == state.lower().rstrip() or stopcmd == state.lower().rstrip()):
            if rospy.has_param('state'):
                # Write it to parameter name 'state'
                rospy.set_param('state', state)        
            else:
                print ('Invalid parameter "state"')        
        else:
            print ('Invalid command')

if __name__ == '__main__':

    try:
        statecmd()
    except rospy.ROSInterruptException:
        pass