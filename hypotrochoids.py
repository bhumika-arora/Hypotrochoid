#importing the modules being used in the program
import math as m
import turtle


def draw_hypotrochoid(hypt, r, R, d):
    
    '''(turtle, int, int, int)-> void
    Draws a hypotrochoid using the functions x and y given
    the radius of the outer circle, inner circle and distance
    d from the inner circle.
    '''
#initializing the variable for lcm
    
    #lcm = 0
    
#iterating over the loop to find the smallest possible multiple
    
    for lcm in range(R, (r*R)+1):
       
#ending the loop if lcm found
        
        if (lcm%r==0 and lcm%R==0):
            break
        
#use penup so that it doesn't draw a line
        
        hypt.penup()
        
#initializing the value of theta
    
    theta = 0.0

#using a while loop to iterate over all the values
#of theta in the range and plot different x and y
        
    while (0.0<= theta < (2*(m.pi))*(lcm/R)):

#calculating the x and y using the functions given to us
    
        x = (R-r)*(m.cos(theta)) + d*m.cos(((R-r)/r)*theta)
        y = (R-r)*(m.sin(theta)) - d*m.sin(((R-r)/r)*theta)
        
#using the goto method to set the position to (x,y)
        
        hypt.goto(x,y)
        
        if(theta==0.0):
            
#start drawing the turtle when the theta is 0
            
            hypt.pendown()
        
        theta += 0.1
        
#testing
        
#create a turtle

first = turtle.Turtle()

#color the turtle as per your choice

first.color("purple")

#hide the pointer

first.hideturtle()

#call the function to draw the hypotrochoid.

draw_hypotrochoid(first, 75, 125, 125)

 


