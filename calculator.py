from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Calculator")

e = Entry(root, width= 50, borderwidth= 1)

# Set up calculator box
e.grid(row = 0, column= 0, columnspan= 5, padx = 5, pady = 5)

# Input numbers into the calculator
def click_button(number):
    e.insert(END, number)

# Clear calculator functionality
def clear_button():
    e.delete(0, END)

# Adds the addition functionality
def add_button():
    global first_number
    global operation
    operation = "+"
    first_number = e.get()
    e.delete(0, END)

# Adds the subtraction functionality
def subtract_button():
    global first_number
    global operation
    operation = "-"
    first_number = e.get()
    e.delete(0, END)

# Adds the multiplication functionality
def multiply_button():
    global first_number
    global operation
    operation = "x"
    first_number = e.get()
    e.delete(0, END)

# Adds the division functionality
def divide_button():
    global first_number
    global operation
    operation = "÷"
    first_number = e.get()
    e.delete(0, END) 

# Adds the exponent functionality
def exponent_button():
    global first_number
    global operation
    operation = "^"
    first_number = e.get()
    e.delete(0, END) 

# Adds the percent functionality
def percent_button():
    first_number = e.get()
    e.delete(0, END)
    if int(first_number) == 0:
        print("Error. Please clear and try again.")
    else:
        e.insert(0, float(first_number) / 100)

# Adds the equals functionality
def solve_button():
    second_number = e.get()
    second_number = float(second_number)
    e.delete(0, END)
    if operation == "+":
        answer = float(first_number) + float(second_number)
        if(answer.is_integer()):
            e.insert(0, int(answer))
        else:
            e.insert(0, answer)
    elif operation == "-":
        answer = float(first_number) - float(second_number)
        if(answer.is_integer()):
            e.insert(0, int(answer))
        else:
            e.insert(0, answer)
    elif operation == "x":
        answer = float(first_number) * float(second_number)
        if(answer.is_integer()):
            e.insert(0, int(answer))
        else:
            e.insert(0, answer)
    elif operation == "÷":
        if int(second_number) == 0:
            e.insert(0, "Error. Please clear and try again.")
        else:
            answer = float(first_number) / float(second_number)
            if(answer.is_integer()):
                e.insert(0, int(answer))
            else:
                e.insert(0, answer)
    elif operation == "^":
        if(second_number.is_integer()):
            exponent_result = 1
            for x in range(int(second_number)):
                exponent_result = float(exponent_result) * float(first_number)
            if(exponent_result.is_integer):
                e.insert(0, int(exponent_result))
            else:
                e.insert(0, float(exponent_result))
        else:
            print("Error. Please clear and try again.")

# Create number buttons

button_1 = Button(root, text = "1", padx = 10, pady = 20, command = lambda: click_button(1))
button_2 = Button(root, text = "2", padx = 10, pady = 20, command = lambda: click_button(2))
button_3 = Button(root, text = "3", padx = 10, pady = 20, command = lambda: click_button(3))
button_4 = Button(root, text = "4", padx = 10, pady = 20, command = lambda: click_button(4))
button_5 = Button(root, text = "5", padx = 10, pady = 20, command = lambda: click_button(5))
button_6 = Button(root, text = "6", padx = 10, pady = 20, command = lambda: click_button(6))
button_7 = Button(root, text = "7", padx = 10, pady = 20, command = lambda: click_button(7))
button_8 = Button(root, text = "8", padx = 10, pady = 20, command = lambda: click_button(8))
button_9 = Button(root, text = "9", padx = 10, pady = 20, command = lambda: click_button(9))
button_0 = Button(root, text = "0", padx = 70, pady = 20, command = lambda: click_button(0))

# Create operation buttons
button_plus = Button(root, text = "+", bg ='orange', fg='white', padx = 10, pady = 20, command = add_button)
button_subtract = Button(root, text = "-", bg ='orange', fg='white', padx = 10, pady = 20, command = subtract_button)
button_multiply = Button(root, text = "x", bg ='orange', fg='white', padx = 10, pady = 20, command = multiply_button)
button_divide = Button(root, text = "÷", bg ='orange', fg='white', padx = 10, pady = 20, command = divide_button)
button_exponent = Button(root, text = "^", padx = 10, pady = 20, command = exponent_button)
button_percent = Button(root, text = "%", padx = 10, pady = 20, command = percent_button)
button_equal = Button(root, text = "=", bg ='orange', fg='white', padx = 10, pady = 20, command = solve_button)
button_decimal = Button(root, text = ".", padx = 10, pady = 20, command = click_button)
button_clear = Button(root, text = "AC", padx = 10, pady = 20, command = clear_button)


# Display buttons 
button_clear.grid(row = 1, column = 0)
button_exponent.grid(row = 1, column = 1)
button_percent.grid(row = 1, column = 2)
button_divide.grid(row = 1, column = 3)

button_7.grid(row = 2, column= 0)
button_8.grid(row = 2, column= 1)
button_9.grid(row = 2, column= 2)
button_multiply.grid(row = 2, column = 3)

button_4.grid(row = 3, column= 0)
button_5.grid(row = 3, column= 1)
button_6.grid(row = 3, column= 2)
button_subtract.grid(row = 3, column = 3)

button_1.grid(row = 4, column= 0)
button_2.grid(row = 4, column= 1)
button_3.grid(row = 4, column= 2)
button_plus.grid(row = 4, column = 3)


button_0.grid(row = 5, column = 0, columnspan= 2)
button_decimal.grid(row = 5, column = 2)
button_equal.grid(row = 5, column = 3)

root.mainloop()