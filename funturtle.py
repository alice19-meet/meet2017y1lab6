import turtle
turtle.shape('turtle')
square=turtle.clone()
square.shape('square')
square.penup()
square.goto(100,100)
square.pendown()
square.goto(100,200)
square.stamp()
square.goto(200,200)
square.stamp()
square.goto(200,100)
square.stamp()
square.goto(100,100)

#draw triangle
triangle=turtle.clone()
triangle.shape('triangle')
triangle.penup()
triangle.goto(-50,-50)
triangle.pendown()
triangle.stamp()
triangle.goto(-100,-100)
triangle.stamp()
triangle.goto(-100,-50)
triangle.stamp()
triangle.goto(-50,-50)

turtle.mainloop()

