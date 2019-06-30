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



root = Tk()
root.title('Бомба')
root.geometry('500x500')

startLabel = Label(root, text='Нажми Enter, чтобы начать игру!', font=('Helvetica', 12))
bombLabel = Label(root, text='Фитиль:',font=('Helvetica', 12))
dayLabel = Label(root, text='День:', font=('Helvetica', 12))

nophoto = PhotoImage(file='Game_bomb\\bomb_no.gif')
normalphoto = PhotoImage(file='Game_bomb\\bomb_normal.gif')
bangphoto = PhotoImage(file='Game_bomb\\bang.gif')

bomb_normal = Label(root, image=normalphoto)
btn_no_bomb = Button(root, text='Нажми меня!')

startLabel.pack()
bombLabel.pack()
dayLabel.pack()

bomb_normal.pack()
btn_no_bomb.pack()

root.bind('<Return>', start)

root.mainloop()
