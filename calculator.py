from tkinter import *

root = Tk()
root.title("Your Calculator")

e = Entry(root, width= 40, borderwidth= 5)

# Set up calculator box
e.grid(row = 0, column= 0, columnspan= 3, padx = 5, pady = 5)

# Input numbers into the calculator
def click_button(number):
    e.insert(END, number)

# Clear calculator functionality
def clear_button():
    e.delete(0, END)

# Adds the addition functionality
def add_button():
    global first_number
    first_number = e.get()
    e.delete(0, END)

# Adds the equals functionality
def solve_button():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, int(first_number) + int(second_number))

# Create number buttons

button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: click_button(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: click_button(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: click_button(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: click_button(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: click_button(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: click_button(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: click_button(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: click_button(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: click_button(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: click_button(0))

# Create operation buttons
button_plus = Button(root, text = "+", padx = 39, pady = 20, command = add_button)
button_subtract = Button(root, text = "-", padx = 39, pady = 20, command = click_button)
button_multiply = Button(root, text = "x", padx = 39, pady = 20, command = click_button)
button_divide = Button(root, text = "÷", padx = 39, pady = 20, command = click_button)
button_equal = Button(root, text = "=", padx = 39, pady = 20, command = solve_button)
button_decimal = Button(root, text = ".", padx = 39, pady = 20, command = click_button)
button_clear = Button(root, text = "Clear", padx = 39, pady = 20, command = clear_button)


# Display buttons 
button_7.grid(row = 1, column= 0)
button_8.grid(row = 1, column= 1)
button_9.grid(row = 1, column= 2)
button_divide.grid(row = 1, column = 3)

button_4.grid(row = 2, column= 0)
button_5.grid(row = 2, column= 1)
button_6.grid(row = 2, column= 2)
button_multiply.grid(row = 2, column = 3)

button_1.grid(row = 3, column= 0)
button_2.grid(row = 3, column= 1)
button_3.grid(row = 3, column= 2)
button_subtract.grid(row = 3, column = 3)

button_0.grid(row = 4, column= 0)
button_decimal.grid(row = 4, column = 1)
button_equal.grid(row = 4, column = 2)
button_plus.grid(row = 4, column = 3)

button_clear.grid(row = 5, column = 0)

root.mainloop()