from tkinter import *

root = Tk()
root.title('Бомба')
root.geometry('500x500')

startLabel = Label(root, text='Нажми Enter, чтобы начать игру!', font=('Helvetica', 12))
bombLabel = Label(root, text='Фитиль:',font=('Helvetica', 12))
dayLabel = Label(root, text='День:', font=('Helvetica', 12))

#nophoto = PhotoImage(file='Game_bomb\\bomb_no.gif')
normalphoto = PhotoImage(file='Game_bomb\\bomb_normal.gif')
#bangphoto = PhotoImage(file='Game_bomb\\bang.gif')

bomb_normal = Label(root, image=normalphoto)
btn_no_bomb = Button(root, text='Нажми меня!')

startLabel.pack()
bombLabel.pack()
dayLabel.pack()

bomb_normal.pack()
btn_no_bomb.pack()

root.mainloop()
