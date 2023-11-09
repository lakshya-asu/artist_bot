# Pixel Artist Bot
Hi! this is Lakshya Jain from ASU, Robotics and Autonomous Systems.
In this project, I'm trying to make a myCobot 280 M5 do a task of arranging blocks to create a 4×4 pixel art from the popular game 'Among Us'.
This can be extended to any combination of pixels as needed!


## Background
As a gamer, pixel artist and roboticist, I thought it'd be fun to make a robot do something that links all three. The task I want to achieve with this project is to give the robot an input of a 4×4 pixel art, give it some colored blocks and ask it to arrange them in the way it looks in the artwork.
This project involves robotic arm movements and kinematics and computer vision.

##image used
![alt text](amongus.png)

## Workflow

 1. To start off, I defined a working area with 16 blocks, and saved their coordinates into a list. 
 2. Then I color calibrate the camera to make sure it detects the red, blue, yellow and green
blocks properly. This is done using sliders to manually adjust HSV values in images.
 3. Now I can start presenting it with blocks one by one, and letting it choose where to place them.
 4. Here's a basic flowchart of how the program works for now:
 ```mermaid
graph LR
A{Color Recognition} --> D[If color is needed] --> B(Decision of where to place it)
A --> G[if color is not needed]
G --> H[tell user that color not needed]
B --> E[Pick and Place into desired position]
```
