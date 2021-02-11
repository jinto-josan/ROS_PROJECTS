import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist



pub=rospy.Publisher("cmd_vel",Twist)
def mover(msg):
    val=msg.data
    cmd=Twist()
    if val == "W":
        cmd.linear.x=1.0
    elif val == "S":
        cmd.linear.x=-1.0
    elif val == "A":
        cmd.angular.z=0.3
    elif val == "D":
        cmd.angular.z=-0.3
    elif val == "Q":
        cmd.linear.x=0.0
        cmd.angular.y=0.0
    pub.publish(cmd)

sub=rospy.Subscriber("DIRECTION",String,mover)

def main():
    rospy.init_node("Driver")
    rospy.spin()

if __name__ == "__main__":
    main()
