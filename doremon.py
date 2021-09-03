import turtle
import random
from turtle import *

 
turtle.bgcolor()

setup(500,500)
#set brush
speed(10)
bgcolor("black")
shape("turtle")
colormode(255)

def drawRound(size, filled):
    pendown()
    if filled==True:
        begin_fill()
    setheading (180)
    circle(size, 360)
    if filled==True:
        end_fill()

def drawRect(length,width,filled):
    setheading(0)
    pendown()
    if filled==True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled==True:
        end_fill()

def head():
    color("blue","blue")
    penup()
    goto(0,100)
    drawRound(75,True)

    color('white','white')
    penup()
    goto(0,72)
    drawRound(60,True)

def eyes():
    #left eye
    color("black","white")
    penup()
    goto(-15,80)
    drawRound(17,True)
#right eye
    color("black","white")
    penup()
    goto(19,80)
    drawRound(17,True)

    color("black","black")
    penup()
    goto(-8,70)
    drawRound(6,True)
    color("white","white")
    penup()
    goto(-8,66)
    drawRound(2,True)
    #right eyball
    color("black","black")
    penup()
    goto(12,70)
    drawRound(6,True)
    color("white","white")
    penup()
    goto(12,66)
    drawRound(2,True)

def nose():
    color("red","red")
    penup()
    goto(0,40)
    drawRound(7,True)
      



def package():
    color("black","black")
    penup()
    goto(-25,-70)
    pendown()
    setheading(-90)
    circle(25,180)
    goto(-25,-70)
    hideturtle()
    head()
    eyes()
    nose()
    mouth()
    whiskers()
    body()
    feet()
    arms()
    hands()
    bell()
    package()



