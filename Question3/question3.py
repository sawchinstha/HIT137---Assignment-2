import turtle

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

def main():
    screen = turtle.Screen()
    screen.title("Recursive Geometric Pattern Generator")
    screen.bgcolor("blue")
    screen.setup(width=800, height=800)
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    try:
        num_sides = int(screen.textinput("Input", "Enter the number of sides you want: "))
        side_length = int(screen.textinput("Input", "Enter the side length: "))
        depth = int(screen.textinput("Input", "Enter the recursion depth: "))
    except (ValueError, TypeError):
        
        print("Invalid input. Please enter a valid number.")
        turtle.done()
        return

if __name__ == "__main__":
    main()