from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0


class Snake:
    def __init__(self):

        self.my_turtle = []
        self.create_snake()
        self.head = self.my_turtle[0]

    def create_snake(self):
        for turtle in STARTING_POSITION:
            self.add_segment(turtle)

    def add_segment(self, turtle):
        jam = Turtle(shape="square")
        jam.color('white')
        jam.penup()
        jam.goto(turtle)
        # jam.goto(turtle*(-20), 0)
        # New_tuple = (jam.pos())
        self.my_turtle.append(jam)

    def extend(self):
        self.add_segment(self.my_turtle[-1].pos())

    def move(self):
        k = self.my_turtle
        for i in range(len(k) - 1, 0, -1):
            new_x = k[i - 1].xcor()
            new_y = k[i - 1].ycor()
            k[i].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



