from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, location= (0, 0)):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.pendown()
        self.color("white")
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align= "center", font= ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align= "center", font= ("Arial", 24, "normal"))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align= "center", font= ("Arial", 24, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER, Press Y to continue", align= "center", font= ("Arial", 24, "normal"))