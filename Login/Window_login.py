from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry('300x500')
root.title('Вход в систему')

def registration():
    text = Label(text='Для входа в систему - зарегистрируйтесь!')
    text_log = Label(text='Введите Ваш логин:')
    registr_login = Entry()
    text_password1 = Label(text='Введите Ваш пароль:')
    registr_password1 = Entry(show='*')
    text_password2 = Label(text='Ещё раз пароль:')
    registr_password2 = Entry(show='*')
    button_registr = Button(text='Зарегистрироваться!', command=lambda: save())
    text.pack()
    text_log.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_password1.get()
        f = open('Login\\login.txt', 'wb')
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text='Поздравляем! Теперь вы можете войти в систему!')
    text_enter_login = Label(text='Введите Ваш логин:')
    enter_login = Entry()
    text_enter_pass = Label(text='Введите Ваш пароль:')
    enter_password = Entry(show='*')
    button_enter = Button(text='Войти')
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open('Login\\login.txt', 'rb')


registration()

root.mainloop()
