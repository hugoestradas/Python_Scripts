from turtle import *

speed(200)
fillcolor('yellow')

def polygon(sides, side_len):
  begin_fill()
  for i in range(0, sides):
    forward(side_len)
    left(360/sides)
  end_fill()
  if side_len >0:
    left(2)
    forward(8)
    polygon(sides, side_len-1)

polygon(8,50)
