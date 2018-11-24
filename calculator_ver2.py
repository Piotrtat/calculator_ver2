from tkinter import *

top = Tk()
top.title("Calculator")
top.geometry("350x450")

textin = StringVar()
operator = ""

def clickbut(number):
    print(str(number))
    global operator
    operator = operator + str(number)
    textin.set(operator)


def equlbut():
    global operator
    try:
        print(operator)
        div = str(eval(operator))
    except Exception:
        div = 'ERROR'
    textin.set(div)
    operator = ""

def clrbut():
    textin.set("")

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

    for entry in button_list:
        elemnt = (entry[0])
        print("element: {}".format(elemnt))
        m_button = Button(top, command=lambda elm=elemnt: clickbut(elm), text=str(entry[0]),
                          width=entry[1], height=entry[2], fg=entry[3])
        m_button.place(x=entry[4], y=entry[5])

        B_15 = Button(top, command=equlbut, text="=", width=8, height=8, fg="blue")
        B_15.place(x=264, y=302)

        B_16 = Button(top, text="Clear (CE)", command=clrbut, width=17, height=3, fg="purple")
        B_16.place(x=17, y=66)

print(button_location())

def rst():
    L1 = Label(top, text="Result", fg="green")
    L1.pack(side=TOP)
    E1 = Entry(top, textvar=textin, width=int(34.5), bd=5)
    E1.pack(side=TOP)


print(rst())

def options():
    menubar = Menu(top)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Load", command=options)
    filemenu.add_separator()
    filemenu.add_command(label="Save", command=options)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=top.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=options)
    editmenu.add_command(label="Copy", command=options)
    editmenu.add_command(label="Paste", command=options)
    editmenu.add_command(label="Delete", command=options)
    editmenu.add_command(label="Select All", command=options)

    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=options)
    helpmenu.add_command(label="About...", command=options)
    menubar.add_cascade(label="Help", menu=helpmenu)

    top.config(menu=menubar)


print(options())


top.configure(bg="LightBlue")
top.mainloop()