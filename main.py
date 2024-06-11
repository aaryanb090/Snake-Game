from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# bug in the code --> you can turn the head backwards by giving two commands simultaneously which ends the game

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # 0 value turns tracer off

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # adds 0.1 sec delay between each movements
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        scoreboard.update_scoreboard()
        snake.reset()

    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.update_scoreboard()
            snake.reset()

screen.exitonclick()
