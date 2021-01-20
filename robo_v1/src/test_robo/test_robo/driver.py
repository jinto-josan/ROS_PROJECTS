import rclpy
from std_msgs.msg import String
from rclpy.node import Node
from geometry_msgs.msg import Twist

class robo(Node):

    def __init__(self,name):
        super().__init__(name)
        self.pub=self.create_publisher(Twist,"cmd_vel",10)
        self.sub=self.create_subscription(String,"DIRECTION",self.mover,10)
    def mover(self,msg):
        val=msg.data
        cmd=Twist()
        if val == "W":
            cmd.angular.z=-1.0
        elif val == "S":
            cmd.angular.z=1.0
        elif val == "A":
            cmd.linear.x=-0.2
        elif val == "D":
            cmd.linear.x=0.2
        elif val == "Q":
            cmd.linear.x=0.0
        self.pub.publish(cmd)

def main():
    rclpy.init()
    node=robo("Driver")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
