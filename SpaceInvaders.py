#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle
import random

turtle.register_shape('Invader.gif')

class Invaders(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pu()
        self.goto(random.randint(-100, 100), random.randint(100,200))
        self.active = True
        
        
Invaders()

print("Hello World")
    
