"""A menu-driven application to draw filled geometric shapes using Turtle Graphics."""

import turtle

# Global Constants for menu choice validation (Slide 5-6 / 5-10 alignment)
SQUARE_CHOICE = '1'
CIRCLE_CHOICE = '2'
TRIANGLE_CHOICE = '3'
QUIT_CHOICE = '4'

def main():
    # Initialize choice tracking loop
    choice = '0'
    
    # Run the menu system until the user enters the designated quit choice constant
    while choice != QUIT_CHOICE:
        print("\nShape Menu")
        print(f"{SQUARE_CHOICE}) Draw a Square")
        print(f"{CIRCLE_CHOICE}) Draw a Circle")
        print(f"{TRIANGLE_CHOICE}) Draw an Equilateral Triangle")
        print(f"{QUIT_CHOICE}) Quit")
        
        # Validate menu selection dynamically using the assignment-required walrus operator
        while (choice := input("Enter your choice: ")) != SQUARE_CHOICE and choice != CIRCLE_CHOICE and choice != TRIANGLE_CHOICE and choice != QUIT_CHOICE:
            print(f"Invalid choice. Please enter {SQUARE_CHOICE}, {CIRCLE_CHOICE}, {TRIANGLE_CHOICE}, or {QUIT_CHOICE}.")
            print("\nShape Menu")
            print(f"{SQUARE_CHOICE}) Draw a Square")
            print(f"{CIRCLE_CHOICE}) Draw a Circle")
            print(f"{TRIANGLE_CHOICE}) Draw an Equilateral Triangle")
            print(f"{QUIT_CHOICE}) Quit")
            
        if choice in [SQUARE_CHOICE, CIRCLE_CHOICE, TRIANGLE_CHOICE]:
            # If the window was previously closed, reset the global graphics state completely
            if not turtle.TurtleScreen._RUNNING:
                turtle.TurtleScreen._RUNNING = True
                
            # Create a localized pen that safely attaches to the clean or active canvas
            t = turtle.Turtle()
            t.hideturtle()
            t.clear()
            
            if choice == SQUARE_CHOICE:
                start_x = float(input("Enter the starting X coordinate: "))
                start_y = float(input("Enter the starting Y coordinate: "))
                side_length = float(input("Enter the length of a side: "))
                fill_color = input("Enter the fill color: ")
                draw_square(t, start_x, start_y, side_length, fill_color)
                
            elif choice == CIRCLE_CHOICE:
                center_x = float(input("Enter the X coordinate of the center: "))
                center_y = float(input("Enter the Y coordinate of the center: "))
                radius = float(input("Enter the radius: "))
                fill_color = input("Enter the fill color: ")
                draw_circle(t, center_x, center_y, radius, fill_color)
                
            elif choice == TRIANGLE_CHOICE:
                start_x = float(input("Enter the starting X coordinate: "))
                start_y = float(input("Enter the starting Y coordinate: "))
                side_length = float(input("Enter the length of a side: "))
                fill_color = input("Enter the fill color: ")
                draw_triangle(t, start_x, start_y, side_length, fill_color)
            
        elif choice == QUIT_CHOICE:
            print("Exiting the program.")
            try:
                turtle.bye()  # Cleanly shut down turtle window if it is open
            except turtle.Terminator:
                pass

def draw_square(t, x, y, side, color):
    """Draws a custom-filled square using coordinates and line steps."""
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for count in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()

def draw_circle(t, x, y, radius, color):
    """Draws a custom center-offset circular fill shape."""
    t.penup()
    # Adjust starting Y coordinate down by the radius to keep the center positioned properly
    t.goto(x, y - radius)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_triangle(t, x, y, side, color):
    """Draws a custom equilateral triangle structure using 120-degree angles."""
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for count in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()

if __name__ == "__main__":
    main()
