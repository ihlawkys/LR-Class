from tkinter import *
from random import choice

def print_hello():
    print("привет")

def change_color(event=None):
    colors = ['blue', 'white', 'pink', 'green', 'purple']
    root.configure(bg=choice(colors))



root = Tk()
root.title("Hello")
root.geometry("450x470")
root.configure(bg='pink')

label = Label(root, text="I am glad to see you.", font=('Times New Roman', 20))
label.pack(pady=20)

button_1 = Button(root, text="print", command=print_hello, width=15, height=2)
button_1.pack(pady=10)

button_2 = Button(root, text="exit", command=root.destroy, width=15, height=2)
button_2.pack(side='bottom')

button_3 = Button(root, text="Смена цвета", width=15, height=2)
button_3.pack(pady=10)

button_3.bind("<Button-1>", change_color)

root.mainloop()