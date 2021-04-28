from turtle import *

speed(100)

def polygon(sides, side_len):
  for i in range(0, sides):
    forward(side_len)
  polygon(sides, sided_len-1)

polygon(9,50)
