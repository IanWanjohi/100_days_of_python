# from turtle import Turtle, Screen
# turtle = Turtle()
# print(turtle)
#
# turtle.shape("turtle")
# turtle.color("red")
# turtle.forward(100)
#
# my_Screen = Screen()
# height = my_Screen.canvheight
# print(height)
# my_Screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Countries", ["Kenya", "New Zealand", "Italy"])
table.add_column("Cities", ["Nairobi", "Wellington", "Rome"])

table.align = "l"

print(table)

