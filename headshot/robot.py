# to connect with some physical machine
from pyrobot import Robot

# Initialize the robot
robot = Robot('locobot')

def move_forward(distance):
    # Move the robot forward
    robot.base.go_to_relative([distance, 0, 0])

if __name__ == "__main__":
    # Define the displacement (in meters) for the robot to move forward
    forward_distance = 0.5  # Move 0.5 meters forward
    
    # Move the robot forward
    move_forward(forward_distance)