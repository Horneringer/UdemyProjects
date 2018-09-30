from tkinter import *

window = Tk()


def km_to_miles():
    miles = float(en1_value.get()) * 1.6
    t1.insert(END, miles)


btn1 = Button(window, text='Выполнить', command=km_to_miles)  # функция пишется без скобок вконце! работае как ссылка!
btn1.grid(row=0, column=0)

en1_value = StringVar()  # функция захватывает строку, которую ввёл пользователь и помещает её в переменную en1_value
# (строка является последовательностью)

en1 = Entry(window, textvariable=en1_value)
en1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
