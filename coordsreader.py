import cv2
import keyboard
from pymycobot.genre import Angle, Coord
from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD 
import time

mc = MyCobot("COMXX", 115200)
def coordsReader():
    # Get the coordinates from the robot
    coords = mc.get_coords()

    # Add the coordinates to the list
    coords_list.append(coords)
    
keyboard.on_press_key("space", lambda _: coordsReader())

# Wait for 'esc' to be pressed, then quit the program
keyboard.wait('esc')

# Initialize an empty list for the coordinates
coords_list = []

# Print the list of coordinates
print(coords_list)