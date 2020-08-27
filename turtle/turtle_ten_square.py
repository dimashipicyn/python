import turtle

turtle.shape('turtle')

n = 10
for i in range(10):
	for i in range(4):
		turtle.forward(n)
		turtle.left(90)
	n += 20
	turtle.right(135)
	turtle.penup()
	turtle.forward(14)
	turtle.pendown()
	turtle.left(135)
