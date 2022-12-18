from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, location= (0, 0)):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.pendown()
        self.color("white")
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 24, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", align= "center", font= ("Arial", 24, "normal"))