import rospy
from geometry_msgs.msg import Twist
from ball_chaser.srv import *
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

imgWidth=640
pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
cmd=Twist()
roll=pitch=yaw=0.0

#using propotional controller to control the speed of rotation
#feedback taken using odom
#error of 0.03 rad is choosen which is approx 14 frames
kp=3.0
def get_angle(msg):
    global roll,pitch,yaw
    cur=msg.pose.pose.orientation
    (roll,pitch,yaw)=euler_from_quaternion([cur.x,cur.y,cur.z,cur.w])

def srv_callback(req):
    reqdAngle=yaw+req.angle
    #+ z left rotate and -z right rotate
    cmd.linear.x=0.0
    cmd.angular.z=0.0
    pub.publish(cmd)
    r=rospy.Rate(10)
    #print(req.angle)
    while abs(reqdAngle-yaw)>0.03 and req.angle!=4.0 and req.angle !=0.0:
        cmd.angular.z=kp*(reqdAngle-yaw)
        pub.publish(cmd)
        #print("speed= {}, reqdAngle  {}, yaw  {}",cmd.angular.z,reqdAngle,yaw)
        r.sleep()
    
    cmd.angular.z=0.0
   # cmd.linear.x=0.0
   # pub.publish(cmd)
    if req.angle == 4:
        cmd.linear.x=0.0
    else:
        cmd.linear.x=1.0
    pub.publish(cmd)
    return gotoResponse(True)
def main():
    rospy.init_node("command_robot")
    sub=rospy.Subscriber('odom',Odometry,get_angle)
    srv=rospy.Service("command_robot",goto,srv_callback)
    rospy.spin()

if __name__=="__main__":
    main()
