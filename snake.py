from turtle import Turtle

class Snake:

    def __init__(self, thickness, speed= 5):
        self.snake = []
        self.thicc = thickness
        self.speed = speed
        self._create_snake(position=(0, 0))

    def _create_snake(self, position):
        body = Turtle("square", visible= False)
        body.color("white")
        body.penup()
        body.goto(position)
        body.showturtle()
        self.snake.append(body)

    def increase_size(self):
        last = self.snake[-1]

        direction = last.heading()

        if direction == 0: #Facing East
            x_spawn = last.xcor() - self.thicc
            y_spawn = last.ycor()
            self._create_snake(position=(x_spawn, y_spawn))

        elif direction == 90: #Facing North
            x_spawn = last.xcor() 
            y_spawn = last.ycor() - self.thicc
            self._create_snake(position=(x_spawn, y_spawn))

        elif direction == 180: #Facing West
            x_spawn = last.xcor() + self.thicc
            y_spawn = last.ycor()
            self._create_snake(position=(x_spawn, y_spawn))

        elif direction == 270: #Facing South
            x_spawn = last.xcor() 
            y_spawn = last.ycor() + self.thicc
            self._create_snake(position=(x_spawn, y_spawn))

        else:
            print("invalid rotation, check code")

    def move(self):
        for i in range(len(self.snake)):
            
            if i == 0:
                prev_pos = self.snake[i].position()
                self.snake[i].forward(self.speed)
            else:
                current_pos = self.snake[i].position()
                self.snake[i].goto(prev_pos)

                prev_pos = current_pos

    def turn_right(self):
        self.snake[0].right(90)

    def turn_left(self):
        self.snake[0].left(90)

    def tail_collision(self):

        for segment in self.snake[1:]:

            if self.snake[0].position() == segment.position():
                return True
        
        return False
