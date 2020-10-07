# AI
#AI人工智慧課程
#NTCU AI course
#Professor Chih-Hung Wu NTCU DCT

#吃豆人
#Pacman Ghost Algorithm - www.101computing.net/pacman-ghost-algorithm/
from math import atan, cos, sin
from processing import *

WIDTH=400
HEIGHT=400
pacman_X = 30
pacman_Y = 30
delay = 3

ghost_X = 10
ghost_Y = 10

def setup():
    strokeWeight(1)
    frameRate(20)
    size(WIDTH,HEIGHT)

def moveGhost():    
  global ghost_X,ghost_Y,pacman_X,pacman_Y
  fill(0,0,0)
  stroke(255,255,255)
  
  #Find out the direction (angle) the Ghost needs to move towards
  #Using SOH-CAH-TOA trignometic rations
  opposite=pacman_Y-ghost_Y
  adjacent=pacman_X-ghost_X
  angle = atan(opposite/adjacent)
  if ghost_X>pacman_X:
    angle=angle+180
  
  #Use this angle to calculate the velocity vector of the Ghost
  #Once again using SOH-CAH-TOA trignometic rations
  velocity=10 #pixels per frame
  
  vx = velocity * cos(angle)
  vy = velocity * sin(angle)
  
  #Apply velocity vector to the Ghost coordinates to move/translate the ghost
  ghost_X = ghost_X + vx
  ghost_Y = ghost_Y + vy
  
  #Draw Ghost  
  ellipse( ghost_X,ghost_Y,20,20)
    
def movePacman():
    global pacman_X, pacman_Y

    fill(0,0,0)
    stroke(0,0,0)
    fc = environment.frameCount

    #Pacman follows the mouse cursor
    pacman_X += (mouse.x-pacman_X)/delay;
    pacman_Y += (mouse.y-pacman_Y)/delay;
    
    #Draw Pacman
    ellipse(pacman_X,pacman_Y,5,5)
    
def playGame():
  background(50,50,150)
  movePacman()
  moveGhost()

draw = playGame
run()
