from tkinter import *
root = Tk()
root.geometry('500x500')
root.title('ыыыыыы')
canva = Canvas(width= 500, height= 500, background='green')
canva.pack()
# canva.create_line(0,0, 1300,700, width=5,  fill='pink')
# canva.create_rectangle(400,200, 600,400, width=10, fill='white')
# canva.create_oval(1000, 200, 700, 420, width=15, fill='purple')
# canva.create_line(500,500, 600,600, width=10, fill='FFDEAD')
# for  i in range(10):
#     if i% 2 == 0:
#         color = 'black'
#     if i == 9:
#         color = 'red'
#     else:
#         color = 'white'
#     canva.create_oval(425+i*15, 175+i*15, 975-i*15, 525-i*15, fill=color, width=1)
for  i in range(10):
    if i % 3 == 0:
        color = 'white'
    elif i % 2 == 0:
        color = 'red'
    else:
        color = 'green'
    canva.create_rectangle(150+i*10, 150+i*10, 350-i*10, 350-i*10, fill=color, width=1)

root.mainloop()