from tkinter import *
import random
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

# Скорости ракеток
PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0

# Скорость мяча с каждым ударом
BALL_SPEED_UP = 1.00
# Максимальная скорость мяча
BALL_MAX_SPEED = 30
# Начальная скорость мяча
BALL_X_SPEED = 20
BALL_Y_SPEED = 20
# Расстояние до правого края
RIGHT_LINE_DISTANCE = WIDTH - PAD_W

# Отскок мяча от ракеток
def bounce(action):
    global BALL_X_SPEED
    global BALL_Y_SPEED
    if action == 'strike':
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED

# Функции движения
def move_ball():
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2
    # Вертикальный отскок
    if ball_right + BALL_X_SPEED < RIGHT_LINE_DISTANCE and ball_left + BALL_X_SPEED > PAD_W:
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
        

def move_pads():
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

def main():
    move_ball()
    move_pads()
    # Вызываем саму себя
    root.after(30, main)

# Фокус на канвас (реакция на клавиши)
c.focus_set()

# Обработка нажатий
def moveent_handler(event):
    global LEFT_PAD_SPEED
    global RIGHT_PAD_SPEED
    if event.keysym == 'w':
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == 's':
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == 'Up':
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == 'Down':
        RIGHT_PAD_SPEED = PAD_SPEED

# Привязка к канвас
c.bind('<KeyPress>', moveent_handler)

# Отпускание клавишь
def stop_pad(event):
    global LEFT_PAD_SPEED
    global RIGHT_PAD_SPEED
    if event.keysym in 'ws':
        LEFT_PAD_SPEED = 0
    elif event.keysym in ('Up', 'Down'):
        RIGHT_PAD_SPEED = 0

c.bind('<KeyRelease>', stop_pad)

main()

root.mainloop()
