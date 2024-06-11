import turtle
from turtle import Turtle
import random
turtle.colormode(255)
COLOR_LIST = [(210, 165, 74), (96, 182, 194), (233, 216, 122), (16, 114, 171), (178, 47, 71), (106, 84, 79),
              (5, 146, 80), (250, 211, 218), (216, 63, 85), (130, 192, 118), (239, 153, 175), (77, 126, 185),
              (230, 242, 247), (9, 169, 93), (144, 118, 114), (0, 125, 69), (204, 141, 151), (79, 58, 54),
              (185, 28, 46), (164, 210, 179), (156, 207, 215), (62, 167, 184), (223, 176, 171), (69, 56, 51),
              (173, 189, 214), (187, 118, 65), (73, 63, 54)]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(random.choice(COLOR_LIST))
        self.goto(random_x, random_y)
