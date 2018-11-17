from tkinter import *

top = Tk()
top.title("Calculator")
top.geometry("350x450")

textin = StringVar()
operator = ""

def button_location():
    button_list = [[0, 17, 3, 'red', 17, 382],
                   [1, 8, 3, 'red', 17, 302],
                   [2, 8, 3, 'red', 100, 302],
                   [3, 8, 3, 'red', 182, 302],
                   [4, 8, 3, 'red', 17, 222],
                   [5, 8, 3, 'red', 100, 222],
                   [6, 8, 3, 'red', 182, 222],
                   [7, 8, 3, 'red', 17, 142],
                   [8, 8, 3, 'red', 100, 142],
                   [9, 8, 3, 'red', 182, 142],
                   ["," , 8, 3, 'blue', 182, 382],
                   ["*", 8, 3, 'blue', 264, 66],
                   ["/", 8, 3, 'blue', 182, 66],
                   ["+", 8, 3, 'blue', 264, 222],
                   ["-", 8, 3, 'blue', 264, 142]]


top.configure(bg="LightBlue")
top.mainloop()