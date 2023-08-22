#import turtle library
import  turtle
#list for storing color
mycolor=["red","blue","yellow","green","orange","pink","red","blue","yellow","green","orange","pink","navy"]
#set background to black
turtle.bgcolor("black")
#set pencolor to orange
turtle.pencolor("yellow")
turtle.color("yellow","green")
#change pen shape
turtle.shape("turtle")
turtle.pensize(10)
turtle.rt(270)
j=0

for i in range(13):
    #set color for each line
    turtle.pencolor(mycolor[j])
    j+=1
    turtle.forward(200)
    turtle.right(194)
#changing pensize
turtle.pensize(15)
turtle.pencolor("green")
turtle.lt(182)
turtle.fd(300)
turtle.rt(360)
turtle.backward(100)

turtle.pensize(10)
for m in range(0,15):
 turtle.rt(m)
 turtle.backward(m+7) 
turtle.pensize(5)
j=0
for i in range(13):
    #set color for each line
    turtle.pencolor(mycolor[j])
    j+=1
    turtle.forward(70)
    turtle.right(194)
turtle.done()