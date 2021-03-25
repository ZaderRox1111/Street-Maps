import turtle
import sys
from math import cos, sin, pi

#create global constants
BLOCK_SIZE = 5

def main():
    #receives the street data file from argv[1]
    #initialize the turtle we are going to use to draw the streets
    street_data = sys.argv[1]
    turt = turtle.Turtle()

    #setting some general settings for the turtle environment
    turtle.bgcolor('black')
    turtle.screensize(750)
    turtle.speed(0)
    turtle.tracer(50,0)
    turt.color("white")
    turt.ht()

    #opening up the street data and reading in the lines
    with open(street_data) as streets:
        data_lines = streets.readlines()

    #doing work on each line to make it easy to work with
    #then draws the line with the data gathered
    for line in data_lines:
        #split between each space in the lines
        line = line.split()

        #read in the necessary data like x start point, y start point, length, direction
        x_start = float(line[0]) * BLOCK_SIZE
        y_start = float(line[1]) * BLOCK_SIZE
        length = float(line[2]) * BLOCK_SIZE
        direction = float(line[3])

        draw_street(turt, x_start, y_start, length, direction)

    #exit the turtle graphic when clicked after end of program
    turtle.exitonclick()

def draw_street(turt, x_start, y_start, length, direction):
    #move the turtle to the starting point
    turt.penup()
    turt.goto(x_start, y_start)
    turt.pendown()

    #calculate the endpoint
    x_end, y_end = calculate_endpoint(x_start, y_start, length, direction)

    #move the turtle to the ending point, drawing the line
    turt.goto(x_end, y_end)

def calculate_endpoint(x_start, y_start, length, direction):
    #find the x and y components of the length/direction
    x_comp = length * cos(direction / 5.0 * pi)
    y_comp = length * sin(direction / 5.0 * pi)

    #add the components to the starting point to find the end point
    x_end = x_start + x_comp
    y_end = y_start + y_comp

    #return the end points
    return x_end, y_end

if __name__ == '__main__':
    main()
