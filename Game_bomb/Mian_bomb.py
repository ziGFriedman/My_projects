from tkinter import *

okToPressReturn = True
bomb = 100
day = 0

def start(event):
    global okToPressReturn
    if okToPressReturn == False:
        pass
    else:
        startLabel.config(text='')
        updateBomb()
        updateDay()
        updateDisplay()

        okToPressReturn == False

def updateDisplay():
    global bomb
    global day
    if bomb <= 50:
        bomb_normal.config(image=nophoto)
    else:
        bomb_normal.config(image=normalphoto)

    bombLabel.config(text='Фитиль:' + str(bomb))
    dayLabel.config(text='День:' + str(day))
    bomb_normal.after(100, updateDisplay)

def updateBomb():
    global bomb
    bomb -= 1
    if isAlive():
        bombLabel.after(500, updateBomb)

def isAlive():
    global bomb
    if bomb <= 0:
        startLabel.config(text='БАМ! БАМ!')
        bomb_normal.config(image=bangphoto)
        return False
    else:
        return True

def updateDay():
    global day
    day += 1
    if isAlive():
        dayLabel.after(5000, updateDay)

def stop():
    global bomb
    if isAlive():
        if bomb <= 79:
            bomb += 20
        else:
            bomb -= 20

root = Tk()
root.title('Бомба')
root.geometry('500x440')

startLabel = Label(root, text='Нажми Enter, чтобы начать игру!', font=('Helvetica', 12))
bombLabel = Label(root, text='Фитиль:' + str(bomb), font=('Helvetica', 12))
dayLabel = Label(root, text='День:' + str(day), font=('Helvetica', 12))

nophoto = PhotoImage(file='Game_bomb\\bomb_no.gif')
normalphoto = PhotoImage(file='Game_bomb\\bomb_normal.gif')
bangphoto = PhotoImage(file='Game_bomb\\bang.gif')

bomb_normal = Label(root, image=normalphoto)
btn_no_bomb = Button(root, text='Нажми меня!', command=stop)

startLabel.pack()
bombLabel.pack()
dayLabel.pack()

bomb_normal.pack()
btn_no_bomb.pack()

bang_photo = Label(root, image=bangphoto)

root.bind('<Return>', start)

root.mainloop()
