from turtle import*
speed(100)

def polygon(sides, side_len):
  for i in range(0, sides):
    forward(side_len)
    left(360/sides)
  if side_len > 0:
    left(2)
    forward(8)
    polygon(sides, side_len-1)

polygon(5, 130)
