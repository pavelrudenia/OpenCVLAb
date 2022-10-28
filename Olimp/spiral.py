import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.width(1)
t.speed(15)

col = ('white','yellow','blue')
for i in range(5555):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
