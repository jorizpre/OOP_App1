import math
import random
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance(self, x, y):
        distance_x = abs(x - self.x)
        distance_y = abs(y - self.y)
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        return distance


class TurtlePoint(Point):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(5, 'red')


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


# Creating a child class of the Rectangle class (inheritance)
# TurtleRectangle inherits from Rectangle
# TurtleRectangle will have Rectangle's methods + its own ones
class TurtleRectangle(Rectangle):
    def draw(self, canvas):  # canvas will actually be a turtle object
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()
        canvas.forward(abs(self.upright.x - self.lowleft.x))
        canvas.left(90)
        canvas.forward(abs(self.upright.y - self.lowleft.y))
        canvas.left(90)
        canvas.forward(abs(self.upright.x - self.lowleft.x))
        canvas.left(90)
        canvas.forward(abs(self.upright.y - self.lowleft.y))


rectangle1 = Rectangle(lowleft=Point(random.randint(0, 199), random.randint(0, 199)),
                       upright=Point(random.randint(200, 400), random.randint(200, 400)))

print("The rectangle coordinates are: (" + str(rectangle1.lowleft.x) + ", " + str(rectangle1.lowleft.y) + ") and ("
      + str(rectangle1.upright.x) + ", " + str(
    rectangle1.upright.y) + "). Guess a point that falls in the rectangle and its area")
user_x = float(input("Guess Coordinate X: "))
user_y = float(input("Guess Coordinate Y: "))
user_area = float(input("Guess the Area: "))

print("Does the point fall in the rectangle? " + str(Point(user_x, user_y).falls_in_rectangle(rectangle1)))

if user_area == rectangle1.area():
    print("Correct, the area of the rectangle is " + str(user_area))
else:
    print("Wrong, your area is off by " + str(abs(user_area - rectangle1.area())))

myturtle = turtle.Turtle()
turtle_rectangle = TurtleRectangle(rectangle1.lowleft, rectangle1.upright)
turtle_rectangle.draw(canvas=myturtle)
turtle_point = TurtlePoint(user_x, user_y)
turtle_point.draw(canvas=myturtle)
turtle.done()
