# discrete time state estimation 
import math 

class MobileRobot: 
    def __init__(self, x,y,theta):
        self.x= x
        self.y= y 
        self.theta = theta
    def move(self, linear_vel, angular_vel, dt):
        self.linear_vel = linear_vel
        self.angular_vel = angular_vel
        self.dt = dt 
        self.x = self.x+ self.linear_vel*math.cos(self.theta)*(self.dt)
        self.y = self.y+ self.linear_vel*math.sin(self.theta)*(self.dt)
        self.theta = self.theta + self.angular_vel*self.dt 
    def get_pose(self):
        return (self.x, self.y ,self.theta)
state = MobileRobot(3,4,90)
state.move(5,0,1)
print(state.get_pose())

    