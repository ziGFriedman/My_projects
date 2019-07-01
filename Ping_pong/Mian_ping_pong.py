from tkinter import *

# Настройки окна
WIDTH = 900
HEIGHT = 300
# Ширина/высота ракетки
PAD_W = 10
PAD_H = 100
# Радиус мяча
BALL_RADIUS = 40
# Скорость мяча
BALL_X_CHANGE = 20
BALL_Y_CHANGE = 0

root = Tk()
root.title('Пинг-понг')

c = Canvas(root, width=WIDTH, height=HEIGHT, bg='#008B8B')
c.pack()

# Левая линия
c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill='white')
# Правая линия
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill='white')

# Разделитель игрового поля
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill='white')

#Мяч
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2, HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2, HEIGHT/2+BALL_RADIUS/2, fill='#FF4500')

# Ракетки
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill='#DA70D6')
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, PAD_H, width=PAD_W, fill='#DA70D6')

# Функции движения мяча
def move_ball():
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)

def main():
    move_ball()
    # Вызываем саму себя
    root.after(30, main)

main()

root.mainloop()
