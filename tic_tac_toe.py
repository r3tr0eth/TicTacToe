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

# Draw the grid
for i in range(-100, 101, 50):
    player_x.penup()
    player_x.goto(i, 100)
    player_x.pendown()
    player_x.goto(i, -100)

    player_x.penup()
    player_x.goto(100, i)
    player_x.pendown()
    player_x.goto(-100, i)

# Initialize the game board
board = [[" " for i in range(3)] for j in range(3)]

# Define a function to draw X or O on the board
def draw_mark(player, x, y):
    player.penup()
    player.goto(x * 50, y * 50)
    player.pendown()
    player.stamp()

# Define a function to check if the game is over
def game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Show the winner
turtle.done()
