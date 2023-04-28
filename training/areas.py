import math

def calculate_square(x):
    square = x * 2
    print(square)
    return square

def calculate_rectangle(x,y):
    rectangle = (x * y)
    print(rectangle)
    return rectangle



side = float(input('What is the length of a side of the square?: '))
calculate_square(side)

length = float(input('What is the length of rectangle?: '))
width = float(input('What is the width of the rectangle?: '))
calculate_rectangle(length, width)

