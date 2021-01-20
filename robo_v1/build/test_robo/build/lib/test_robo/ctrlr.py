from rclpy.node import Node
import rclpy
from std_msgs.msg import String


def main():
    rclpy.init()
    node =Node('Controller')
    pub =node.create_publisher(String,'DIRECTION',10)
    print("W--UP\nA--LEFT\nD--RIGHT\nS--DOWN\nQ--STOP") 
    ip=input()
    msg=String()
    while ip is not 'Z':
        if(ip=="W" or ip=="S" or ip=="A" or ip=="D" or ip=="Q"):
            msg.data=ip
            pub.publish(msg)
        else:
            print("W--UP\nA--LEFT\nD--RIGHT\nS--DOWN\nQ--STOP") 
        ip=input()
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
        
