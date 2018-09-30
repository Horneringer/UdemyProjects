from tkinter import *

window = Tk()
window.geometry('580x50')


def convertion():
    grams = float(en1_value.get()) * 1000
    tx1.insert(END, grams)
    pounds = float(en1_value.get()) * 2.20462
    tx2.insert(END, pounds)
    ounces = float(en1_value.get()) * 35.274
    tx3.insert(END, ounces)


def entry_del():
    en1.delete(first=0, last=22)
    tx1.delete(1.0, END)
    tx2.delete(1.0, END)
    tx3.delete(1.0, END)


lb1 = Label(window, text='Kg')
lb1.grid(row=0, column=0)

en1_value = StringVar()
en1 = Entry(window, textvariable=en1_value)
en1.grid(row=0, column=1)

bt1 = Button(window, text='Convert', command=convertion)
bt1.grid(row=0, column=2)
bt2 = Button(window, text='Clear', command=entry_del)
bt2.grid(row=0, column=3)

tx1 = Text(window, height=1, width=22)
tx1.grid(row=2, column=0)

tx2 = Text(window, height=1, width=22)
tx2.grid(row=2, column=1)

tx3 = Text(window, height=1, width=22)
tx3.grid(row=2, column=2)

window.mainloop()
