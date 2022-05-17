import turtle, random
color=['red','green','blue','orange','purple','pink','yellow']
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
	color = random.choice(color)
	painter.pencolor(color)
	painter.circle(100)
	painter.right(30)
	painter.left(60)
	painter.setposition(0,0)
painters = turtles.Turtle()
painters.pensize(4)
for i in range(10):
	color = random.choice(color)
	painters.pencolor(color)
	painters.circle(200)
	painters.right(10)
	painters.left(50)
	painters.setposition(1,0)