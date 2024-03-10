#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.media.ev3dev import SoundFile, ImageFile





def control(balls_list):
    
        # Initialize the EV3 Brick.
    ev3 = EV3Brick()

    # Initialize the motors.
    left_motor = Motor(Port.B,Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.C,Direction.COUNTERCLOCKWISE)
    gripper_motor = Motor(Port.A)
    
    # Initialize the drive base.
    golfBot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
    
    if not balls_list:
        # our logic when no balls detected
        print("No balls detected.")
        return
    
    for ball in balls_list:
        x, y, radius = ball
        # info about the detected ball     
        print(f"Detected ball at ({x}, {y}) with radius {radius}")    
    # for now we choose the first ball, we will improve the code in the near future 
    ball = balls_list[0]
    
    frame_center = 640//2 
    distance = ball.x -frame_center
    if distance > 0:
        golfBot.turn(180)
    elif distance < 0:
         golfBot.turn(360)  
          
    
   
