from turtle import *

RAD = 100
RAD2 = RAD / 2
RAD6 = RAD / 6

degrees() # Switch to degrees
# Draw the circle, radius 100, half black
fillcolor('black')
begin_fill()
circle(RAD, 180)
end_fill()
circle(RAD, 180)

# Draw smaller black semi-circle
left(180)
penup()
goto(0, RAD)
pendown()
begin_fill()
circle(RAD2, 180)
end_fill()

# Draw smaller white semi-circle
penup()
goto(0, RAD)
pendown()
fillcolor('white')
begin_fill()
circle(RAD2, 180)
end_fill()

# Draw smaller circles
penup()
goto(0, RAD2 + RAD6)
begin_fill()
circle(RAD6)
end_fill()

fillcolor('black')
goto(0, 2 * (RAD - RAD6))
begin_fill()
circle(RAD6)
end_fill()
