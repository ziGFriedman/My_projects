from tkinter import *

root = Tk()
root.title('Бомба')
root.geometry('500x500')

startLabel = Label(root, text='Нажми Enter, чтобы начать игру!', font=('Helvetica', 12))
bombLabel = Label(root, text='Фитиль:',font=('Helvetica', 12))
dayLabel = Label(root, text='День:', font=('Helvetica', 12))

startLabel.pack()
bombLabel.pack()
dayLabel.pack()

root.mainloop()
