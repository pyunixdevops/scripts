#!/usr/bin/python

import turtle
import math
import tkinter

bob=turtle.Turtle()
def polygon(t, n, length):
   angle=360/n
   for i in range(n):
      t.fd(length)
      t.lt(angle)
   polygon(bob, 7, 70)
