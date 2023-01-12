import turtle
import random
import time
delay = 0.1
score = 0
heighestscore= 0
#snake boddied
bodies = []
# screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("pink")
s.setup(width=800,height=600)



#snake size
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"


#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()


#score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-350,-250)
sb.write("Score : 0   | Height Score : 0")

def moveup ():
    if head.direction!= "down":
        head.direction = "up"
def movedown():
    if head.direction!= "up":
        head.direction ="down"
def moveleft():
    if head.direction!= "right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction= "right"

def movestop():
    head.direction = "stop"


def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction=="down" :
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


# event handling - key mapping
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft, "Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")



# main loop
while True:
    s.update()
    #this is update the screen
    #check collosion wth border
    if head.xcor()>390:
        head.setx(-390)
    if head.xcor()<(-390):
        head.setx(390)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()< (-290):
        head.sety(290)


        #check collision with food
    if head.distance(food) < 20:
            #move food to random place
        x = random.randint(-390,390)
        y= random.randint(-290,290)
        food.goto(x,y)


            #increase the lenght of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)  #append new body


            #increse the score
        score += 10

            #change delay
        delay -= 0.01

            #update the high score
        if score > heighestscore:
            heighestscore= score
        sb.clear()
        sb.write("Score:{} Heighest Score : {}".format(score,heighestscore))

    #move the snake body
    for index in range(len(bodies)-1,0,-1):
        x = bodies[index -1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)


    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)

    move()



    #check collison with snake body
    for body in bodies :
        if body .distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"


            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()



            score = 0
            delay = 0.1


            #update score board
            sb.clear()
            sb.write("Score : {}  Heighest Score : {}".format(score,heighestscore))
    time.sleep(delay)
s.mainloop()

#this is end of code



