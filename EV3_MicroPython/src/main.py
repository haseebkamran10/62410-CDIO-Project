#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from control import motor_control
from vision import camera_control


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def main():
    #camera control process and detection initialization 
    camera_control.main()
   
    #EV3 Initilization
    #ev3 = EV3Brick()
    #ev3.speaker.beep()
    
    ''' balls_list = camera_control.detect()
    // motor_control.control(balls_list) '''
if __name__ == "__main__":
    main()
 

