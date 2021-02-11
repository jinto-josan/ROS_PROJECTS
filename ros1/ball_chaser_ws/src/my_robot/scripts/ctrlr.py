import rospy
from std_msgs.msg import String


def main():
    rospy.init_node("Control")
    pub =rospy.Publisher("DIRECTION",String)
    print("W--UP\nA--LEFT\nD--RIGHT\nS--DOWN\nQ--STOP") 
    ip=input()
    msg=String()
    while ip != 'Z':
        if(ip=="W" or ip=="S" or ip=="A" or ip=="D" or ip=="Q"):
            msg.data=ip
            pub.publish(msg)
        else:
            print("W--UP\nA--LEFT\nD--RIGHT\nS--DOWN\nQ--STOP") 
        ip=input()

if __name__=="__main__":
    main()
        
