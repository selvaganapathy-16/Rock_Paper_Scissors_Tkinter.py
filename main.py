import tkinter
import random

win = tkinter.Tk()

win.geometry("500x400")

win.title("ROCK PAPER SCISSORS")

img = tkinter.PhotoImage(file="sample.ppm")
limg=tkinter.Label(win,image=img).pack()

img2 = tkinter.PhotoImage(file="iconsample.png")
win.iconphoto(False,img2)



list = ['ROCK', 'PAPER','SCISSORS']

def button_diable():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")



def isrock():
    x=random.choice(list)
    if x == "ROCK":
        result='It\'s a tie'

    elif x == "SCISSORS":
        result='You Win'

    else:
        result='HaHa..I win'
    l1.config(text="ROCK")
    l3.config(text=x)
    l4.config(text=result)
    button_diable()

def ispaper():
    x = random.choice(list)
    if x == "PAPER":
        result = 'It\'s a tie'

    elif x == "ROCK":
        result = 'You Win'

    else:
        result = 'HaHa..I win'
    l1.config(text="PAPER")
    l3.config(text=x)
    l4.config(text=result)
    button_diable()


def isscissors():
    x = random.choice(list)
    if x == "SCISSORS":
        result = 'It\'s a tie'

    elif x == "PAPER":
        result = 'You Win'

    else:
        result = 'HaHa..I win'
    l1.config(text="SCISSORS")
    l3.config(text=x)
    l4.config(text=result)
    button_diable()

def reset():
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    l1.config(text="PLAYER")
    l3.config(text="COMPUTER")
    l4.config(text="")




label = tkinter.Label(win, text ="ROCK PAPER SCISSORS",font=("Century", 19,"bold"),bg = "purple",fg="white")
label.place(relx=.19,rely=.1)

l1 = tkinter.Label(win , text = " PLAYER",font=("TimesNewRoman",15,"bold"),bg="black",fg="white")
l1.place(relx=.1,rely=.3)

l2 = tkinter.Label(win , text = " VS",font=("TimesNewRoman",15,"bold"),bg="black",fg="white")
l2.place(relx=.5,rely=.3)

l3 = tkinter.Label(win,text ="COMPUTER",font=("TimesNewRoman",15,"bold"),bg="black",fg="white")
l3.place(relx=.7,rely=.3)

l4 = tkinter.Label(win, text="",font=("TimesNewRoman",15,"bold"))
l4.place(relx=.4,rely=.5)

b1=tkinter.Button(win,text="ROCK",font=12,width=7,command=isrock)
b1.place(relx=.1,rely=.7)

b2 = tkinter.Button(win,text="PAPER",font=12,width=7,command=ispaper)
b2.place(relx=.4,rely=.7)

b3 = tkinter.Button(win,text="SCISSORS",font=10,width=9,command=isscissors)
b3.place(relx=.7,rely=.7)

b4 = tkinter.Button(win,text="RESET",font=10,width=9,bg = "red",command=reset)
b4.place(relx=.4,rely=.9)

win.mainloop()
