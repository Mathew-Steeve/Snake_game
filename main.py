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
snake_head = snake.head
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
    if snake_head.xcor() > 280 or snake_head.ycor() > 280 or snake_head.xcor() < -290 or snake_head.ycor() < -290:
        is_game_on = False
        score.game_over()
    for seg in snake.my_turtle[1:]:
        if snake_head.distance(seg) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
