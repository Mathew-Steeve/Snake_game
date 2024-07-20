from turtle import Screen
import time
from snake import Snake
from Food import Food
from Score import Score


screen = Screen()
screen.bgcolor('black')
screen.title('My snake game')
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
score = Score()

screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    snake_head = snake.head
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake_head.xcor() > 280 or snake_head.ycor() > 280 or snake_head.xcor() < -280 or snake_head.ycor() < -280:
        score.reset()
        snake.reset()
    for seg in snake.my_turtle[1:]:
        if snake_head.distance(seg) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
