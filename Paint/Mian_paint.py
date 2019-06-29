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

w.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

root.mainloop()
