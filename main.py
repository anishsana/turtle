import turtle
import random

screen = turtle.getscreen()

# Create player 1.
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")

# Create player 2.
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")

# Create player 1 home.
player_two.penup()
player_two.goto(-200, -100)
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)

# Create player 2 home.
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# Create die.
die = [1, 2, 3, 4, 5, 6]

# Roll dice until either player reaches home.
for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        # Roll dice and move player 1.
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        player_one.fd(20 * die_outcome)

        # Roll dice and move player 2.
        player_two_turn = input("Press 'Enter' to roll the die ")
        d = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        player_two.fd(20 * die_outcome)

# Prevent screen from immediately closing after execution.
screen.mainloop()
