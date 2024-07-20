from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Score_record.txt", "r") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score :{self.high_score}", False, ALIGNMENT, FONT)
        with open("Score_record.txt", "w") as data:
            data.write(f"{self.high_score}")


    def increase(self):
        self.score += 1
        self.update()
