import turtle
import math

# Initialize turtle screen
screen = turtle.Screen()
screen.title("Scientific Calculator")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Initialize turtle pens
input_field_text_pen = turtle.Turtle()
output_field_text_pen = turtle.Turtle()
button_pen = turtle.Turtle()

# Set turtle pen settings
input_field_text_pen.penup()
input_field_text_pen.goto(-180, 300)
input_field_text_pen.pendown()
output_field_text_pen.penup()
output_field_text_pen.goto(-180, 280)
output_field_text_pen.pendown()
button_pen.penup()
button_pen.goto(-180, 100)
button_pen.pendown()

# Set button settings
button_width = 60
button_height = 60
button_spacing = 10
buttons = [
    ["7", "8", "9", "+", "Clear"],
    ["4", "5", "6", "-", "Delete"],
    ["1", "2", "3", "*", "pi"],
    ["0", ".", "/", "sqrt", "="],
    ["sin", "cos", "tan", "log", "exp"],
    ["(", ")", "mod", " ", " "]
]

# Initialize input field
input_field = ""
input_field_text_pen.write("Enter your expression:", align="left", font=("Arial", 16, "normal"))

# Function to draw a button on the screen
def draw_button(t, x, y, label):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(button_width)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x + button_width / 2, y + button_height / 2 - 10)
    t.write(label, align="center", font=("Arial", 12, "normal"))

# Function to clear the input field
def clear_input():
    global input_field
    input_field_text_pen.clear()
    input_field_text_pen.write("Enter your expression:", align="left", font=("Arial", 16, "normal"))
    input_field = ""

# Function to delete the last character in the input field
def delete_last_character():
    global input_field
    if len(input_field) > 0:
        input_field = input_field[:-1]
        input_field_text_pen.clear()
        input_field_text_pen.write(input_field, align="left", font=("Arial", 16, "normal"))

# Function to evaluate the expression in the input field
def evaluate_expression():
    global input_field
    try:
        # Replace "log" with "math.log"
        input_field_modified = input_field.replace("log", "math.log10")

        # Replace "exp" with "math.exp"
        input_field_modified = input_field_modified.replace("exp", "math.exp")

        # Replace "pi" with "math.pi"
        input_field_modified = input_field_modified.replace("pi", "math.pi")

        # Replace "mod" with "%"
        input_field_modified = input_field_modified.replace("mod", "%")

        # Replace "sqrt" with "math.sqrt"
        input_field_modified = input_field_modified.replace("sqrt", "math.sqrt")

        # Convert degrees to radians for trigonometric functions
        input_field_modified = input_field_modified.replace("sin(", "math.sin(math.radians(")
        input_field_modified = input_field_modified.replace("cos(", "math.cos(math.radians(")
        input_field_modified = input_field_modified.replace("tan(", "math.tan(math.radians(")

        # Count and close parentheses if needed
        count_open_parentheses = input_field_modified.count("(")
        count_close_parentheses = input_field_modified.count(")")
        missing_parentheses = count_open_parentheses - count_close_parentheses
        input_field_modified += ")" * missing_parentheses

        result = eval(input_field_modified)
        output_field_text_pen.clear()
        output_field_text_pen.write("Result: " + str(result), align="left", font=("Arial", 16, "normal"))
        input_field = str(result)
        input_field_text_pen.clear()
        input_field_text_pen.write(input_field, align="left", font=("Arial", 16, "normal"))
    except:
        output_field_text_pen.clear()
        output_field_text_pen.write("Error: Invalid expression", align="left", font=("Arial", 16, "normal"))

# Function to append the clicked character to the input field
def append_character(character):
    global input_field
    if character == "log":
        input_field += "log("
    elif character in ["sin", "cos", "tan"]:
        input_field += character + "("
    elif character == "exp":
        input_field += "exp("
    elif character == "pi":
        input_field += "pi"
    elif character == "sqrt":
        input_field += "sqrt("
    else:
        input_field += character
    input_field_text_pen.clear()
    input_field_text_pen.write(input_field, align="left", font=("Arial", 16, "normal"))

# Function to handle button clicks
def handle_click(x, y):
    global input_field, button_pen
    for row_index, row in enumerate(buttons):
        for button_index, button_label in enumerate(row):
            # Calculate the buttons position
            button_x = -180 + button_spacing + button_index * (button_width + button_spacing)
            button_y = 200 - button_spacing - row_index * (button_height + button_spacing)

            # Check if the click is inside the button
            if x > button_x and x < button_x + button_width and y > button_y and y < button_y + button_height:
                if button_label == "Clear":
                    clear_input()
                elif button_label == "Delete":
                    delete_last_character()
                elif button_label == "=":
                    evaluate_expression()
                else:
                    append_character(button_label)

# Initialize turtles
screen.onclick(handle_click)

# Draw the buttons
button_pen.speed(0)
button_pen.color("black", "lightgray")
for row_index, row in enumerate(buttons):
    for button_index, button_label in enumerate(row):
        # Calculate the button's position
        button_x = -180 + button_spacing + button_index * (button_width + button_spacing)
        button_y = 200 - button_spacing - row_index * (button_height + button_spacing)
        draw_button(button_pen, button_x, button_y, button_label)

# Start the turtle main loop
turtle.mainloop()
                
               
