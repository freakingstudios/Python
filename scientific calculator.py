import math
import tkinter as tk

# Create the GUI window
root = tk.Tk()
root.title("Scientific Calculator")

# Set the calculator display
display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button click events
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_add():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_subtract():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_multiply():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_divide():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_sqrt():
    first_number = display.get()
    global math_operation
    math_operation = "sqrt"
    display.delete(0, tk.END)
    display.insert(0, str(math.sqrt(float(first_number))))

def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)
    if math_operation == "addition":
        display.insert(0, str(f_num + float(second_number)))
    elif math_operation == "subtraction":
        display.insert(0, str(f_num - float(second_number)))
    elif math_operation == "multiplication":
        display.insert(0, str(f_num * float(second_number)))
    elif math_operation == "division":
        display.insert(0, str(f_num / float(second_number)))

# Create the calculator buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
