import turtle
import time
from turtle import *

#creating the gui 

myScreen= turtle.Screen()
myScreen.bgcolor("white")
myScreen.setup(width=1000, height=1000)
myScreen.title("Analogue Clock")
myScreen.tracer(0)  # control blinking

# Create the drawing pen
draw = turtle.Turtle()
draw.hideturtle()
draw.speed(0)
draw.pensize(3) #control the width of the structure


def draw_clock(hour, minute, second, draw):
    # Draw clock face
    draw.up() #jump the turtle with out drawing
    draw.goto(0, 300)#put it from the center of the screen to 210 radius up
    draw.setheading(180)# face the turtle to the left(180 degree)
    draw.color("silver")
    draw.pendown()# know i want to draw the circle
    draw.circle(300)
    # Draw hour hashes
    draw.up() # no drawings since pen.up()
    draw.goto(0, 0) # go back to the center
    draw.setheading(90)# face him 90 degree

    #this draw hour pointers
    
    
    for i in range(12):
        draw.color("green")
        draw.fd(280)#go 190 without drawing 
        draw.pendown()

        draw.fd(20)# the draw the rest 20 
        draw.penup()
        draw.goto(0, 0)
        draw.rt(30)
    setheading(90)
    hideturtle()
    #this draw the minute pointers 
    for j in range(60):
        pensize(2)
        penup()
        forward(290)
        pendown()
        color("green")
        forward(10)
        penup()
        goto(0,0)
        right(6)

        
    #thi align the amharic numbers in the clock with respective of their places
    setheading(90)
    penup()
    goto(0,235)
    write("፲፪",align="center",font=("arial",30))
    goto(0,0)

    setheading(90)
    penup()
    goto(265,-20)
    write("፫",align="center",font=("arial",30))
    goto(0,0)

    setheading(90)
    penup()
    goto(0,-275)
    write("፮",align="center",font=("arial",30))
    goto(0,0)

    setheading(90)
    penup()
    goto(-255,-20)
    write("፱",align="center",font=("arial",30))
    goto(0,0)
    
    #this draw the hour hand
    draw.penup()
    draw.goto(0,0)
    draw.color("red")
    draw.setheading(90)
    angle=(hour/12)*360
    draw.right(angle)
    draw.pendown()
    draw.forward(114)
    #this draw the minute hand

    draw.penup()
    draw.goto(0,0)
    draw.color("blue")
    draw.setheading(90)
    angle=(minute/60)*360
    draw.right(angle)
    draw.pendown()
    draw.forward(150)

#this darw the second hand 
    draw.penup()
    draw.goto(0,0)
    draw.color("green")
    draw.setheading(90)
    angle=(second/60)*360
    draw.right(angle)
    draw.pendown()
    draw.forward(170)


    
while True:
    hour = int(time.strftime("%I"))#this make the hour "string formated time""%I,converted to 0-12"
    minute = int(time.strftime("%M"))#this is for the minute
    second = int(time.strftime("%S"))#this done for the second
    draw_clock(hour, minute, second, draw)
    myScreen.update()
    time.sleep(1)# not to dipilicate 
    draw.clear()
wndw.mainloop()