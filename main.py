from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
choice = screen.textinput(title="Turtle race",
                          prompt="which color would win, red, yellow, orange, blue, green, black? ")
colors = ["red", "yellow", "orange", "blue", "green", "black"]
play = False
if choice:
    play = True

num = 50
name = []
for i in range(len(colors)):
    name.append(colors[i])
    name[i] = Turtle(shape="turtle")
    name[i].penup()
    name[i].color(colors[i])
    name[i].goto(x=-230, y=175 - num)
    num += 50

while play:
    for i in range(len(name)):
        if name[i].xcor()>230:
            play = False
            if name[i]==choice:
                print(f"you've won! {colors[i]} is the winner")
            else:
                print(f"you've lost! {colors[i]} is the winner")

        name[i].forward(random.randint(0,10))

screen.exitonclick()
