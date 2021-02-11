import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge,CvBridgeError
import numpy as np
from geometry_msgs.msg import Twist
from ball_chaser.srv import *

laserSamples=40
imageWidth=640
bridge=CvBridge()
middle=imageWidth//2
angleConstant=1.3962634/640
prev_x=0
cmd=Twist()
movingFlag=False

def call_srvc(angle):
    global sub
    sub.unregister()
    rospy.wait_for_service('command_robot')
    try:
        srvc=rospy.ServiceProxy('command_robot',goto)
        msg=gotoRequest()
        msg.angle=angle
        _=srvc(msg)
    except rospy.ServiceException as e:
            print("Service call failed :%s"%e)
    sub=rospy.Subscriber("front_camera/image_raw",Image,callback,queue_size=1)


def callback(img):
    global bridge,prev_x,angleConstant,imageWidth,movingFlag
    try:
        img=bridge.imgmsg_to_cv2(img,"bgr8")
    except CvBridgeError as e:
        print(e)


    #find white colour object
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_white=np.array([0,0,100],dtype=np.uint8)
    upper_white=np.array([0,0,255],dtype=np.uint8)
    mask=cv2.inRange(hsv,lower_white,upper_white)
    res=cv2.bitwise_and(img,img,mask=mask)
    #cv2.imshow("mask",mask)
    #cv2.imshow("res",res) 

    #find circles
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.20,100,param1=50,param2=30,minRadius=0,maxRadius=0)
    if circles is not None:
        circles=np.round(circles[0,:]).astype("int")
        for (x,y,r) in circles:
            cv2.circle(img,(x,y),r,(0,255,0),4)
            if abs(prev_x-x)>30 and abs(middle-x) >=40:
                print("px:{} x: {} px:{}  mx: {}  ",prev_x,x,abs(prev_x-x),abs(middle-x))
                prev_x=x
                movingFlag=True
                #left '+' angle and right '-' angle as per odom frame
                relativeAngle=(middle - x)*angleConstant
                call_srvc(relativeAngle)
    elif movingFlag:
        #no ball stop
        call_srvc(4)
        movingFlag=False
        print("stopped")

    cv2.imshow("Image_Window",img)
    #3 ms wait
    cv2.waitKey(3)

sub=rospy.Subscriber("front_camera/image_raw",Image,callback,queue_size=1)  
def main():

    rospy.init_node('detect_ball')
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()


