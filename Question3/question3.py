import turtle # import the turtle library containing all the function that we'll use 

def draw_pattern(t, side_length, depth):
    
    if depth == 0:
       t.forward(side_length)
       
    else:
        draw_pattern(t, side_length / 3, depth - 1)
        t.right(60)
        draw_pattern(t, side_length / 3, depth - 1)
        t.left(120)
        draw_pattern(t, side_length / 3, depth - 1)
        t.right(60)
        draw_pattern(t, side_length / 3, depth - 1)

def main(): # wrap main program logic in this main() func
    
    screen = turtle.Screen() # create CANVAS for our drawing
    screen.title("Recursive Geometric Pattern Generator") # giving title for the screen
    screen.bgcolor("blue") # putting BLUE as a background color
    screen.setup(width=800, height=800) # setting up width and height
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    t.goto(-200, 10) 
    t.pendown()

    
    try:
        num_sides = int(screen.textinput("Input", "Enter the number of sides you want: "))
        side_length = int(screen.textinput("Input", "Enter the side length: "))
        depth = int(screen.textinput("Input", "Enter the recursion depth: "))
    except (ValueError, TypeError):
        
        print("Invalid input. Please enter a valid number.")
        turtle.done()
        return
    
    for _ in range(num_sides):
        draw_pattern(t, side_length, depth)
        t.left(360 / num_sides)
        
    turtle.done()
        
if __name__ == "__main__":
    main()