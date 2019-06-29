from tkinter import *

canvas_width = 700
canvas_height = 500
brush_size = 3
color = 'black'

def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def brush_size_change(new_size):
    global brush_size
    brush_size = new_size

def color_change(new_color):
    global color
    color = new_color

root = Tk()
root.title('Paint на Питоне')

w = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
w.bind('<B1-Motion>', paint)

label1 = Label(text='Цвет кисти', width=10)
red_btn = Button(text='Красный', width=10, bg='red', fg='white', command=lambda: color_change('red'))
blue_btn = Button(text='Голубой', width=10, bg='blue', fg='white', command=lambda: color_change('blue'))
black_btn = Button(text='Чёрный', width=10, bg='black', fg='white', command=lambda: color_change('black'))
white_btn = Button(text='Ластик', width=10, bg='white', command=lambda: color_change('white'))
clear_btn = Button(text='Удалить всё', width=10, command=lambda: w.delete('all'))

label2 = Label(text='Размер кисти', width=10)
one_btn = Button(text='2', width=10, command=lambda: brush_size_change(2))
five_btn = Button(text='5', width=10, command=lambda: brush_size_change(5))
ten_btn = Button(text='10', width=10, command=lambda: brush_size_change(10))
twelve_btn = Button(text='12', width=10, command=lambda: brush_size_change(12))
twenty_btn = Button(text='15', width=10, command=lambda: brush_size_change(15))

w.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

label1.grid(row=0, column=1)
red_btn.grid(row=0, column=2)
blue_btn.grid(row=0, column=3)
black_btn.grid(row=0, column=4)
white_btn.grid(row=0, column=5)
clear_btn.grid(row=0, column=6, sticky=W)

label2.grid(row=1, column=1)
one_btn.grid(row=1, column=2)
five_btn.grid(row=1, column=3)
ten_btn.grid(row=1, column=4)
twelve_btn.grid(row=1, column=5)
twenty_btn.grid(row=1, column=6, sticky=W)

root.mainloop()
