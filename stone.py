import viz
import vizact
import vizinfo
import viztask
from random import uniform as rand
from random import randint as rint
from random import choice
import random
import math
import time
import vizproximity
import vizshape
import vizcam
import vizconfig 
from vizfx.postprocess.effect import BaseShaderEffect 
from vizfx.postprocess.distort import BulgeEffect
from vizfx.postprocess.blur import ZoomBlurEffect
import vizfx.postprocess 
import projector
import datetime
import random
viz.setMultiSample(4)
viz.fov(120)
counter = 0
game_over = False
game_started = False
timer_running = False
goal_made = False
obstacle_created = False
global text
text = viz.addText("GOAL")
text.setPosition([12,6,12])
text.setEuler(90,90,0)
text.fontSize(0)
text.color(viz.RED)
x = random.randint(1,5)
goal_made = False






arrow_forward = None
arrow_left = None
arrow_up_left = None
arrow_right = None
arrow_up_right = None




def goaltext(x):
    if x==1:
        text.fontSize(15)
        text.setScale(0.5,0.5,0.5)
    if x==0:
        text.remove()
viz.go()
viz.MainView.setEuler([90,90,0])
viz.MainView.setPosition([15,40,0])
viz.fov(60)

ground = viz.addChild('field2.dae', scale = [0.7,1,2], color=viz.GREEN)
ground.setPosition(0,0,0)
#front Left Goal	
ground1 = viz.addChild( 'goal_post.osgb' )
ground1.setPosition( 34.6, 0 ,30)
ground1.setEuler([90, 0, 0])  # Rotate 90 degrees around the X-axis
#front Right Goal
ground2 = viz.addChild( 'goal_post.osgb' )
ground2.setPosition( 34.6, 0,-31)
ground2.setEuler([90, 0, 0])  # Rotate 90 degrees around the X-axis
#right Goal Post 
ground3 = viz.addChild( 'goal_post.osgb' )
ground3.setPosition(6.5, 0 ,-36.3)
ground3.setEuler([180, 0, 0])  # Rotate 180 degrees around the X-axis
#left Goal Post 
ground2 = viz.addChild( 'goal_post.osgb' )
ground2.setPosition(6.5, 0 ,36.3)
#welcome screen
ground4 = viz.addChild('welcome3D.glb')
ground4.setPosition( 25.5, 6, 14)
ground4.setEuler(90,90,0)
ground4.setScale(5,5,5)

timer_text = viz.addText('Time:')
# Set the position for the timer text
timer_text.setPosition([27,12,15])
timer_text.setEuler([90,90,0])
# Set a larger font size for better clarity
timer_text.fontSize(25)
timer_text.setScale(0.1,0.1,0.1)
# Set text color to white and background color to black for better visibility
timer_text.color(viz.WHITE)

def arrowforward():
    global arrow_forward
    arrow_forward = viz.addChild('arrow.glb')
    arrow_forward.setPosition(14, 1, 0)
    arrow_forward.setEuler(270, 0, 0)
    arrow_forward.setScale(1, 1, 1)

def arrowleft():
    global arrow_left
    arrow_left = viz.addChild('arrow.glb')
    arrow_left.setPosition(4, 1, 12)
    arrow_left.setEuler(180, 0, 0)
    arrow_left.setScale(1, 1, 1)

def arrowupleft():
    global arrow_up_left
    arrow_up_left = viz.addChild('arrow.glb')
    arrow_up_left.setPosition(16, 1, 12)
    arrow_up_left.setEuler(225, 0, 0)
    arrow_up_left.setScale(1, 1, 1)

def arrowright():
    global arrow_right
    arrow_right = viz.addChild('arrow.glb')
    arrow_right.setPosition(4, 1, -12)
    arrow_right.setEuler(360, 0, 0)
    arrow_right.setScale(1, 1, 1)

def arrowupright():
    global arrow_up_right
    arrow_up_right = viz.addChild('arrow.glb')
    arrow_up_right.setPosition(16, 1, -12)
    arrow_up_right.setEuler(315, 0, 0)
    arrow_up_right.setScale(1, 1, 1)
if x==1:
    arrowforward()
if x==2:
    arrowleft()
if x==3:
    arrowupleft()
if x==4:
    arrowright()
if x==5:
    arrowupright()
# Create a soccer ball object
soccer_ball = viz.addChild('soccerball.osgb',scale = (15,20,20), color =[rand(0.1,0.8), rand(0.1,0.8), rand(0.1,0.8)])
soccer_ball.setPosition([0, 0, 0])  # Set the initial position of the ball
soccer_ball.setEuler(0,0,0)
def add_arrays(arr1, arr2):
    # Check if both arrays have the same length
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length")
    # Initialize an empty result array
    result = []
    # Iterate through the arrays and add corresponding elements
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result
    
#obstacls 
obstacle_created = False
def create_random_obstacle():
    obstacle = viz.addChild('extra_life.glb')  # Replace 'extra_life.glb' with the actual model name
    #obstacle.setEuler(90,90,0)
    obstacle.setScale(0.09, 0.09, 0.09)
    x = random.uniform(-10, 30)  # Random X position within a certain range
    z = random.uniform(-10, 30)  # Random Z position within a certain range
    obstacle.setPosition([x, 0, z])  # Set obstacle position
    # Add continuous spinning animation to the obstacle
    spin_speed = random.uniform(30, 60)  # Random rotation speed in degrees per second
    # Function to handle continuous spinning animation
    def spin_obstacle():
        current_euler = obstacle.getEuler()
        obstacle.setEuler([current_euler[0], current_euler[1] + spin_speed * viz.elapsed(), current_euler[2]])
    # Call the spin_obstacle function continuously to create the continuous spinning effect
    vizact.ontimer(0, spin_obstacle)
    return obstacle


# Function to move the bal?l
def move_ball_forward():
    step_size = 1    # Adjust this value to control the movement speed
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(0, 0,-step_size)))
def move_ball_backward():
    step_size = 1
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(0, 0,step_size)))
def move_ball_left():
    step_size = 1
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(step_size, 0, 0)))
def move_ball_right():
    step_size = 1
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(-step_size, 0, 0)))
def move_upper_right(): 
    step_size = 1
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(-step_size,0,-step_size)))
def move_upper_left():
    step_size = 1
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(step_size,0,-step_size)))
def move_down_right():
    step_size = 1
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(-step_size,0,step_size)))
def move_down_left():
    step_size = 1
    soccer_ball.setPosition(add_arrays(soccer_ball.getPosition(),(step_size,0,step_size)))
# Register the keyboard event handlers for arrow keys
target_locationFL = [34.6, 0 ,31]
target_locationFR= [34.6, 0,-31]
target_locationR = [6.5, 0 ,-36.3]
target_locationL = [6.5, 0 ,36.3]
target_locationM = [33.6, 0,1]
target_locationField = [0,0,0]
tolerance = 2





# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)

# Function to calculate trajectory between two points
def calculate_trajectory(start_point, end_point):
    trajectory = [end_point[0] - start_point[0], end_point[1] - start_point[1], end_point[2] - start_point[2]]
    return trajectory

# Function to calculate displacement between two points
def calculate_displacement(start_point, end_point):
    displacement = calculate_distance(start_point, end_point)
    return displacement

# Inside your check_goalFL() function (and similarly for other goal-checking functions), calculate distance, trajectory, and displacement
def check_goalFL():
    global game_over, goal_made
    current_position = soccer_ball.getPosition()
    distance_to_target1 = vizmat.Distance(current_position, target_locationFL)
    if x == 3 and distance_to_target1 <= tolerance:  # Check if arrow direction is up-left (x==3)
        goaltext(1)
        timer_running = False
        game_over = True
        goal_made = True
        
        # Calculate and print the distance, trajectory, and displacement
        distance = calculate_distance(soccer_ball.getPosition(), target_locationFL)
        trajectory = calculate_trajectory(soccer_ball.getPosition(), target_locationFL)
        displacement = calculate_displacement(soccer_ball.getPosition(), target_locationFL)
        
        print("Distance to target: {}".format(distance))
        print("Trajectory to target: {}".format(trajectory))
        print("Displacement to target: {}".format(displacement))
        
        return True
    return False




def check_goalFR():
    current_position = soccer_ball.getPosition()
    distance_to_target2 = vizmat.Distance(current_position, target_locationFR)
    if x == 5 and distance_to_target2 <= tolerance:  # Check if arrow direction is up-right (x==5)
        goaltext(1)
        timer_running = False
        game_over = True
        goal_made = True
        
        # Calculate and print the distance, trajectory, and displacement
        distance = calculate_distance(soccer_ball.getPosition(), target_locationFL)
        trajectory = calculate_trajectory(soccer_ball.getPosition(), target_locationFL)
        displacement = calculate_displacement(soccer_ball.getPosition(), target_locationFL)
        
        print("Distance to target: {}".format(distance))
        print("Trajectory to target: {}".format(trajectory))
        print("Displacement to target: {}".format(displacement))
        return True
    return False

def check_goalR():
    current_position = soccer_ball.getPosition()
    distance_to_target3 = vizmat.Distance(current_position, target_locationR)
    if x == 4 and distance_to_target3 <= tolerance:  # Check if arrow direction is right (x==4)
        goaltext(1)
        timer_running = False
        game_over = True
        goal_made = True
        
        # Calculate and print the distance, trajectory, and displacement
        distance = calculate_distance(soccer_ball.getPosition(), target_locationFL)
        trajectory = calculate_trajectory(soccer_ball.getPosition(), target_locationFL)
        displacement = calculate_displacement(soccer_ball.getPosition(), target_locationFL)
        
        print("Distance to target: {}".format(distance))
        print("Trajectory to target: {}".format(trajectory))
        print("Displacement to target: {}".format(displacement))
        return True
    return False

def check_goalL():
    current_position = soccer_ball.getPosition()
    distance_to_target4 = vizmat.Distance(current_position, target_locationL)
    if x == 2 and distance_to_target4 <= tolerance:  # Check if arrow direction is left (x==2)
        goaltext(1)
        timer_running = False
        game_over = True
        goal_made = True
        
        # Calculate and print the distance, trajectory, and displacement
        distance = calculate_distance(soccer_ball.getPosition(), target_locationFL)
        trajectory = calculate_trajectory(soccer_ball.getPosition(), target_locationFL)
        displacement = calculate_displacement(soccer_ball.getPosition(), target_locationFL)
        
        print("Distance to target: {}".format(distance))
        print("Trajectory to target: {}".format(trajectory))
        print("Displacement to target: {}".format(displacement))
        
        return True
    return False

def check_goalM():
    current_position = soccer_ball.getPosition()
    distance_to_targetM = vizmat.Distance(current_position, target_locationM)
    if x == 1 and distance_to_targetM <= tolerance:  # Check if arrow direction is forward (x==1)
        goaltext(1)
        timer_running = False
        game_over = True
        goal_made = True
        
        # Calculate and print the distance, trajectory, and displacement
        distance = calculate_distance(soccer_ball.getPosition(), target_locationFL)
        trajectory = calculate_trajectory(soccer_ball.getPosition(), target_locationFL)
        displacement = calculate_displacement(soccer_ball.getPosition(), target_locationFL)
        
        print("Distance to target: {}".format(distance))
        print("Trajectory to target: {}".format(trajectory))
        print("Displacement to target: {}".format(displacement))
        
        return True
    return False



def update_timer():
    global time_remaining, timer_running, game_started, game_over, goal_made,x
    while not game_started:
        yield viztask.waitTime(0.1)
    time_remaining = 12  
    timer_running = True  # set the starting time
    while time_remaining > 0 and timer_running and not game_over:
        if time_remaining <= 5:
            timer_text.alpha(1.0)
            timer_text.color(viz.RED)
            timer_text.setScale(0.1, 0.1, 0.1)
        else:
            timer_text.alpha(1.0)
            timer_text.color(viz.BLUE)
            timer_text.setScale(0.1, 0.1, 0.1)
        timer_text.message('Time remaining: {}'.format(time_remaining))
        # wait for 1 second
        yield viztask.waitTime(1)
        if counter == 0:
            time_remaining -= 1
        
        if check_goalFL() or check_goalFR() or check_goalR() or check_goalL() or check_goalM():
            timer_running = False  # Stop the timer when a goal is made
            goaltext(1)  # Display goal text
            # Display message and wait for user input
            print('Goal made! Press Enter to continue...')
            input()  # Wait for user input
            goaltext(0)  # Remove goal text
            time_remaining = 12  # Reset the timer
            timer_text.message('Time remaining: {}'.format(time_remaining))  # Reset timer text
            # Reset ball position to starting position
            soccer_ball.setPosition([0, 0, 0])
            x = random.randint(1, 5)  # Generate a new random arrow direction
            arrow_remove()  # Remove existing arrows
            # Add new arrow based on the random direction
            if x == 1:
                arrowforward()
            elif x == 2:
                arrowleft()
            elif x == 3:
                arrowupleft()
            elif x == 4:
                arrowright()
            elif x == 5:
                arrowupright()
        
            timer_running = True  # Start the timer again
            game_over = False  # Reset game over flag
            goal_made = False  # Reset goal made flag
             
    # when the timer reaches zero, display a message
    timer_text.message('Time is up!')
    print('time up')

myTask = viztask.schedule(update_timer())

    
    
def boundary():
    global time_remaining, timer_running, x
    current_position = soccer_ball.getPosition()
    distance_to_targetField = vizmat.Distance(current_position, target_locationField)
    if distance_to_targetField >= 50:
        soccer_ball.setPosition(0, 0, 0)
        input("PRESS ENTER TO CONTINUE....")
        goaltext(0)
        time_remaining = 12  # Reset the time remaining to its initial value
        timer_running = True  # Start the timer again
        x = random.randint(1, 5)  # Generate a new random arrow direction
        arrow_remove()  # Remove existing arrows
        if x == 1:
            arrowforward()
        elif x == 2:
            arrowleft()
        elif x == 3:
            arrowupleft()
        elif x == 4:
            arrowright()
        elif x == 5:
            arrowupright()
        vizact.ontimer(0.1, check_goalFL)  # Start checking for goal based on the new arrow direction    
 
    
vizact.onkeydown(viz.KEY_RIGHT, move_ball_forward)
vizact.onkeydown(viz.KEY_LEFT, move_ball_backward)
vizact.onkeydown(viz.KEY_UP, move_ball_left)
vizact.onkeydown(viz.KEY_DOWN, move_ball_right)
if soccer_ball.getPosition() == (12, 0 ,36.3):
        soccer_ball.setPosition([0,0,0])
        viztask.waitTime(0.01)
ball_pos = soccer_ball.getPosition();



def welcome_remove():
	ground4.remove()
def arrow_remove():
    global arrow_forward, arrow_left, arrow_up_left, arrow_right, arrow_up_right
    if arrow_forward:
        arrow_forward.remove()
    if arrow_left:
        arrow_left.remove()
    if arrow_up_left:
        arrow_up_left.remove()
    if arrow_right:
        arrow_right.remove()
    if arrow_up_right:
        arrow_up_right.remove()

def display_instructions(text,position):
    # Create a text object for the instruction initially
    instructions_text = viz.addText(text, pos=position)
    instructions_text.setPosition(24, 8, 26)
    instructions_text.setEuler(90,90,0)
    instructions_text.setScale(2,2,2)
    def remove_instruction_text():
        global arrow_keys_enabled
        instructions_text.remove()  # Remove the text
        arrow_keys_enabled = True
    # Register a callback for the Enter key press event
    def onKeyPress(key):
        global game_started, obstacle_created 
        if key == viz.KEY_RETURN and not game_started and not obstacle_created:
            game_started = True
            remove_instruction_text()
            welcome_remove()
            obstacles_created = True
            create_random_obstacle()
            # Call this function whenever you want to create a new random obstacle with continuous spinning animation
            random_obstacle = create_random_obstacle()
            # Remove the instruction text when Enter key is pressed
    # Register the key press event handler
    viz.callback(viz.KEYBOARD_EVENT, onKeyPress)
    instruction_displayed = True
ball_pos = viz.MainView.getPosition()
display_instructions('\nPress Enter to Start The game and Try to reach any Goal Post.',[1,2,1])
if x==5:
    vizact.ontimer(0.1, check_goalFR)
if x==3:
    vizact.ontimer(0.1,check_goalFL)
if x==2:
    vizact.ontimer(0.1,check_goalL)
if x==4:
    vizact.ontimer(0.1,check_goalR)
if x==1:
    vizact.ontimer(0.1,check_goalM)
vizact.ontimer(0.1,boundary)
counter_m = 0

viz.go()