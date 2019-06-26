from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Викторина')
root.geometry('200x300')

def que_one():
    question = Label(root, text='Висит груша и её нельзя скушать?')
    answer = Entry()
    btn = Button(root, text='Ответить!', command=lambda: game(que_two))
    question.grid(row=0)
    answer.grid(row=1)
    btn.grid(row=2)

    def game(que_two):
        if answer.get() == 'Лампочка':
            que_two()
        else:
            messagebox.showerror('Ошибка!', 'Попробуй ещё раз!')


def que_two():
    question_2 = Label(root, text='Зимой и летом одного цвета?')
    answer_2 = Entry()
    btn = Button(root, text='Ответить!')
    question_2.grid(row=0)
    answer_2.grid(row=1)
    btn_2.grid(row=2)

que_one()

root.mainloop()
