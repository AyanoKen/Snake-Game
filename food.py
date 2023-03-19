from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, screen_wid, screen_height):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("blue")
        self.speed("fastest")
        self.change_position(screen_wid, screen_height)
        
        
    def change_position(self, screen_wid, screen_height):
        x_pos = random.randint(-screen_wid + 50, screen_wid - 50)
        y_pos = random.randint(-screen_height + 50, screen_height - 50)

        self.goto(x_pos, y_pos)