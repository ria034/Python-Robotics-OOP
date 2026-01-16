class  Robot:
    # Class variable shared by all instances
    robot_count = 0
    world_frame = "map"

    def __init__(self):
        # Increment robot count whenever a new robot is created
        Robot.robot_count += 1

    # Class method to access class variable
    @classmethod
    def get_robot_count(cls):
        return cls.robot_count

    # Static method to return constant world frame
    @staticmethod
    def get_world_frame():
        return Robot.world_frame


# Create some robots
robot1 = Robot()
robot2 = Robot()
robot3 = Robot()

# Use class method to check count
print("Robot count:", Robot.get_robot_count())  # or robot3.get_robot_count()
# Use static method to check world frame
print("World frame:", Robot.get_world_frame())
