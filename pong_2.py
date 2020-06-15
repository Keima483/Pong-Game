import turtle
class Game(object):
    def __init__(self,speed,length):
        self.speed=speed
        self.lenght=length

    def game(self):
        score_a = 0
        score_b = 0

# First Paddle
        paddle_a = turtle.Turtle()  # create an object
        paddle_a.shape('square')  # Shape
        paddle_a.speed(0)  # speed(fastest possible)
        paddle_a.color("white")  # colour
        paddle_a.shapesize(stretch_len=1, stretch_wid=self.lenght) # streatching the shape of the bar
        paddle_a.penup()  # draw lines
        paddle_a.goto(-350, 0) # coordinates(x,y) -350 since its on the left to the center of the screen, the center of the screen is (0,0)

        # Second paddle (for explanation se the comments on first paddle)
        paddle_b = turtle.Turtle()
        paddle_b.color("white")
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.shapesize(stretch_len=1, stretch_wid=self.lenght)
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # Ball (for explanation se the comments on first paddle)
        ball = turtle.Turtle()
        ball.color("white")
        ball.speed(0)
        ball.shape("circle")
        ball.penup()
        ball.goto(0, 0)  # to send it to center
        ball.dx = self.speed  # to move the ball and can also to change the direction
        ball.dy = self.speed  # same as above

        # Score using pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup()
        pen.hideturtle() # to hide the line made by the pen since it will always go from center to the top
        pen.color("white")
        pen.goto(0,260) # a bit less then the upper limit
        pen.write("Player A: 0  Player B: 0" , align="center" , font=("Courier", 24 , 'normal')) # text , align (it can be any where) , finally the font detail which i set to courier with size 24 and normale insted of bold and etalix

        # function for paddle up for paddle_a

        def paddle_a_up():
            y = paddle_a.ycor()  # to get the y co-ordinate
            y += 50  # to increase it by 20 (to move it)
            paddle_a.sety(y)  # setting the value of increased position in the paddle


        def paddle_a_down():
            y = paddle_a.ycor()  # to get the y co-ordinate
            y -= 50  # to increase it by 20 (to move it)
            paddle_a.sety(y)  # setting the value of increased position in the paddle

        # function for paddle up for paddle_b

        def paddle_b_up():
            y = paddle_b.ycor()  # to get the y co-ordinate
            y += 50  # to increase it by 20 (to move it)
            paddle_b.sety(y)  # setting the value of increased position in the paddle


        def paddle_b_down():
            y = paddle_b.ycor()  # to get the y co-ordinate
            y -= 50  # to increase it by 20 (to move it)
            paddle_b.sety(y)  # setting the value of increased position in the paddle


        # key mapping
        wn.listen()  # taking input from the keyboard
        wn.onkeypress(paddle_a_up, "w")  # maping the function to key w in keyboard
        wn.onkeypress(paddle_a_down, "s")
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")

        # Game loop
        while True:
            wn.update()  # manually updating the screen

        # to move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        # to make the ball bounce from the boundries
        # top and bottom border
            if ball.ycor() > 290:  # if the location is greater then the border (its 290 here cause the balls diameter is 20)
                ball.sety(290)  # so we will set bring the ball b   ack to 290 and
                ball.dy *= -1  # to bounce it off in a diffrent direction

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1  # to bounce it off in a diffrent direction

        # side borders
            if ball.xcor() > 390:
                ball.goto(0, 0)  # send it back to the center
                ball.dx *= -1  # Change the direction
                score_a += 1 # to increase the score
                pen.clear() # to clear the screen
                pen.write("Player A: {}  Player B: {}".format(score_a , score_b) , align="center" , font=("Courier", 24 , 'normal')) # to update the score

            if ball.xcor() < -390:
                ball.goto(0, 0)  # send it back to the center
                ball.dx *= -1  # Change the direction
                score_b += 1
                pen.clear() # to clear the screen
                pen.write("Player A: {}  Player B: {}".format(score_a , score_b) , align="center" , font=("Courier", 24 , 'normal')) # to update the score

        # for restrictung the movement the paddle
            if paddle_a.ycor() + 40 > 300:
                paddle_a.sety(260)

            if paddle_b.ycor() + 40 > 300:
                paddle_b.sety(260)

            if paddle_a.ycor() - 40 < -300:
                paddle_a.sety(-260)

            if paddle_b.ycor() - 40 < -300:
                paddle_b.sety(-260)

            # for making the ball bounce
            """
            So what we basically did here is:
            in the first half of the if statement we checked wether the x coordinate of the ball is touching the path of movement of the paddle 
            then we will check weather the y co-ordinate is > the possition -40  or < the position +40 we have 40 her cause since we streatched the bars they have became 4 times of 20 i.e., 100 so if it colides in the middle then 40 must be ok
            """
            if self.speed == 2 and self.lenght == 10:
                if((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 100 and ball.ycor() > paddle_b.ycor() - 100)):
                    ball.setx(340)
                    ball.dx *= -1  # to change the direction

                if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 100 and ball.ycor() > paddle_a.ycor() - 100):
                    ball.setx(-340)
                    ball.dx *= -1

            if self.speed == 4 and self.lenght == 7.5:
                if((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 75 and ball.ycor() > paddle_b.ycor() - 75)):
                    ball.setx(340)
                    ball.dx *= -1  # to change the direction

                if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 75 and ball.ycor() > paddle_a.ycor() - 75):
                    ball.setx(-340)
                    ball.dx *= -1
            if self.speed == 8 and self.lenght == 5:
                if((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50)):
                    ball.setx(340)
                    ball.dx *= -1  # to change the direction

                if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
                    ball.setx(-340)
                    ball.dx *= -1


wn = turtle.Screen()  # for making the screen
wn.title("Pong By Keima")  # for the name in top of the screen
wn.bgcolor("Black")  # for the background colour
wn.setup(width=800, height=600)  # for the dimensions of the window
  # to stop the window from refreshing

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle() # to hide the line made by the pen since it will always go from center to the top
pen.color("white")
pen.goto(0,40) # a bit less then the upper limit
pen.write("Press 1 to play" , align="center" , font=("Courier", 24 , 'normal'))

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle() # to hide the line made by the pen since it will always go from center to the top
pen.color("white")
pen.goto(0,-40) # a bit less then the upper limit
pen.write("Press 2 to Exit" , align="center" , font=("Courier", 24 , 'normal'))

def level_1():
    wn.clear()
    wn.bgcolor("black")
    c=Game(2 , 10)
    c.game()

def level_2():
    wn.clear()
    wn.bgcolor("black")
    c=Game(4 , 7.5)
    c.game()

def level_3():
    wn.clear()
    wn.bgcolor("black")
    c=Game(8 , 5)
    c.game()

def start_game():
    wn.clear()
    wn.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.hideturtle() # to hide the line made by the pen since it will always go from center to the top
    pen.color("white")
    pen.goto(0,-80) # a bit less then the upper limit
    pen.write("Press 1 for Easy\n\nPress 2 for Medium\n\nPress 3 for Hard" , align="center" , font=("Courier", 24 , 'normal'))

    wn.listen()  # taking input from the keyboard
    wn.onkeypress(level_1, "1")  # maping the function to key w in keyboard
    wn.onkeypress(level_2, "2")
    wn.onkeypress(level_3, "3")

    

def end_game():
    wn.bye()

wn.listen()  # taking input from the keyboard
wn.onkeypress(start_game, "1")  # maping the function to key w in keyboard
wn.onkeypress(end_game, "2")

while True:
    wn.update()
