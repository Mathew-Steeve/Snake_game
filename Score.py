from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!!", False, "Center", FONT)

    def update(self):
        self.write(f"Score:{self.score}", False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()