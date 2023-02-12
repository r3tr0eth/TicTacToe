import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Tic Tac Toe")

# Create a turtle for the X player
player_x = turtle.Turtle()
player_x.shape("turtle")
player_x.color("blue")
player_x.pensize(5)

# Create a turtle for the O player
player_o = turtle.Turtle()
player_o.shape("circle")
player_o.color("red")
player_o.pensize(5)
