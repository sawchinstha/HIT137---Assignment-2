import turtle # import the turtle library containing all the function that we'll use 

def draw_pattern(t, side_length, depth): # creating draw_pattern function which takes the turtle object, side length, and depth as arguments
    
    if depth == 0: # this condition tells the function when to stop calling itself
       # base case: if depth is 0, just draw a straight line as asked in the question 3
       t.forward(side_length)
       
    else: # where we break the side into smaller segments and add the turns for the inward indentation
        
        # recursive step:
        # 1. draw the first third of the line
        draw_pattern(t, side_length / 3, depth - 1)
        
        # 2. turn right by 60 degrees for the inward indentation
        t.right(60)
        
        # 3. draw the second third of the line
        draw_pattern(t, side_length / 3, depth - 1)
        
        # 4. turn left by 120 degrees to complete the indentation
        t.left(120)
        
        # 5. draw the third third of the line
        draw_pattern(t, side_length / 3, depth - 1)
        
        # 6. turn right by 60 degrees to get back to the original angle
        t.right(60)
        
         # 7. draw the final segment
        draw_pattern(t, side_length / 3, depth - 1)

def main(): # wrap main program logic in this main() func
    
    screen = turtle.Screen() # create CANVAS for our drawing
    screen.title("Recursive Geometric Pattern Generator") # giving title for the screen
    screen.bgcolor("blue") # putting BLUE as a background color
    screen.setup(width=800, height=800) # setting up width and height
    
    t = turtle.Turtle() # creating turtle obj that will do the drawing
    t.speed(0) # setting up max speed to draw quickly
    t.penup() # lift the pen up initially so we can position it without drawing a line
    
    t.goto(-200, 10)  # moving the turtle to good starting pos so everuthing is visible on the screen
    t.pendown() # then, putting the pen done

    
    try: # using try..except block to handle cases where the user enters text instead of a number
        
        num_sides = int(screen.textinput("Input", "Enter the number of sides you want: ")) # asking user for the three parameters: no. of sides, side length and recursion depth
        side_length = int(screen.textinput("Input", "Enter the side length: "))
        depth = int(screen.textinput("Input", "Enter the recursion depth: "))
        
    except (ValueError, TypeError):
        
        print("Invalid input. Please enter a valid number.")
        turtle.done()
        return
    
    for _ in range(num_sides): # using a for loop to repeatedly call draw_pattern function for each side of the polygon
        draw_pattern(t, side_length, depth)
        t.left(360 / num_sides) #  make sure that the turtle turns the correct amount to complete the shape
        
    turtle.done() # keeps the window open after the drawing is complete so that user can see the final view
        
if __name__ == "__main__":
    main()