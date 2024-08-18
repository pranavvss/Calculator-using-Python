import tkinter as tk

# Function to update the display when a button is clicked
def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(value))

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Creating the main window
root = tk.Tk()
root.title("Calculator")
# Adjusted height 
root.geometry("400x700")  
root.resizable(False, False)

# Setting the background color
root.configure(bg="#000000")

# Creating the display
display = tk.Entry(root, font=("Helvetica", 24), borderwidth=0, justify='right', bg="#000000", fg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=40, sticky="nsew")

# Function to create a button with specified properties
def create_button(root, text, row, column, width=1, height=1, command=None, bg="#333333", fg="white"):
    button = tk.Button(root, text=text, font=("Helvetica", 20), command=command, bg=bg, fg=fg, bd=0, highlightthickness=0)
    button.grid(row=row, column=column, columnspan=width, rowspan=height, sticky="nsew", padx=5, pady=5)
    return button

# Adding buttons to the grid
create_button(root, "AC", 1, 0, command=clear_display, bg="#A6A6A6", fg="black")
create_button(root, "+/-", 1, 1, command=lambda: None, bg="#A6A6A6", fg="black")  # Not implemented
create_button(root, "%", 1, 2, command=lambda: button_click('%'), bg="#A6A6A6", fg="black")
create_button(root, "÷", 1, 3, command=lambda: button_click('/'), bg="#FF9500")

create_button(root, "7", 2, 0, command=lambda: button_click('7'))
create_button(root, "8", 2, 1, command=lambda: button_click('8'))
create_button(root, "9", 2, 2, command=lambda: button_click('9'))
create_button(root, "×", 2, 3, command=lambda: button_click('*'), bg="#FF9500")

create_button(root, "4", 3, 0, command=lambda: button_click('4'))
create_button(root, "5", 3, 1, command=lambda: button_click('5'))
create_button(root, "6", 3, 2, command=lambda: button_click('6'))
create_button(root, "-", 3, 3, command=lambda: button_click('-'), bg="#FF9500")

create_button(root, "1", 4, 0, command=lambda: button_click('1'))
create_button(root, "2", 4, 1, command=lambda: button_click('2'))
create_button(root, "3", 4, 2, command=lambda: button_click('3'))
create_button(root, "+", 4, 3, command=lambda: button_click('+'), bg="#FF9500")

# Larger "0" button spanning two columns
create_button(root, "0", 5, 0, width=2, command=lambda: button_click('0'))
create_button(root, ".", 5, 2, command=lambda: button_click('.'))
create_button(root, "=", 5, 3, command=evaluate, bg="#FF9500")

# Adjusting row and column configurations for responsive resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
