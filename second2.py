import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("white")   
  
turtle.pensize()  
  
# To design curve  
def curve():  
    for i in range(200):  
        t.right(1)  
        t.forward(1)  
t.hideturtle()   
t. speed(0)  
t.color("blue", "red")  
  
t.begin_fill()  
t.left(140)  
t.forward(111.65)  
curve()  

t.left(120)  
curve()  
t.forward(111.65)  
t.end_fill()  
t.hideturtle()  
  
turtle.mainloop()  
# t.clear()

# import turtle  
# # Creating turtle  
# t = turtle.Turtle()  
  
# turtle.bgcolor("cyan")  
# turtle.pensize(5)  
# turtle.speed(0)  
  
# while (True):  
#     for i in range(6):  
#         for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:  
#             turtle.color(colors)
#             turtle.write( "Afzaal")
#             turtle.circle(200)  
#             turtle.right(5)  
  
  
# turtle.hideturtle()  
# turtle.mainloop()  