from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

WIDTH = 1000
HEIGHT = 600
SNAKE_SIZE = 100
SNAKE_SPEED = 3
UPDATE_DELAY = 0.005

screen = Screen()
screen.setup(width= WIDTH, height= HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

player = Snake(thickness= SNAKE_SIZE, speed= SNAKE_SPEED)
food = Food(screen_wid= WIDTH/2, screen_height= HEIGHT/2)
scoreboard = ScoreBoard(location= (0, HEIGHT/2 - 50))

screen.listen()
screen.onkey(player.turn_left, "Left")
screen.onkey(player.turn_right, "Right")

alive = True
while alive:
    player.move()
    screen.update()
    time.sleep(UPDATE_DELAY)

    if player.snake[0].distance(food.position()) < 15:
        food.change_position(WIDTH/2, HEIGHT/2)
        scoreboard.increase_score()
        player.increase_size()
        player.increase_size()

    if abs(player.snake[0].xcor()) > WIDTH/2 or abs(player.snake[0].ycor()) > HEIGHT/2:
        scoreboard.game_over()
        alive = False

    if player.tail_collision():
        scoreboard.game_over()
        alive = False


screen.exitonclick()