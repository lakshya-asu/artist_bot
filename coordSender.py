from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD 
import time
import os
import sys
from pymycobot.genre import Angle, Coord
import time


mc = MyCobot("COMXX", 115200)
# Initialize a list of arrays with arbitrary values
coords_list = [
    [-247.3, -34.0, 52.7, 105.76, -68.65, -116.98],
    [-248.3, -35.0, 53.7, 106.76, -69.65, -117.98],
    # ... add more arrays here ...
]

# Define the speed
speed = 1  # replace with the actual speed

def coordSender(position_instruction):
    # Convert the position instruction to an index
    index = int(position_instruction) - 1

    # Select the coordinates from the list
    coords = coords_list[index]

    # Call the function
    mc.sync_send_coords(coords, speed, 1, timeout=2)

