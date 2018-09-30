"""
Программа, хранящая информация о книгах:
Заголовок, Автор
Год, Номер идентификации


Пользователь может:

Просматривать записи
Искать записи
Добавлять записи
Вносить изменения в записи
Удалять записи
Закрывать программу


"""
from tkinter import *
import BookShop_back as backend


# баг с пустым listbox'ом можно исправить и через try-except
def get_selected_row(event):
    # try:
    global selected_tuple
    if not list1.curselection():
        print("Пусто! Добавьте элементы или отобразите существующие")
    else:
        index = list1.curselection()[
            0]  # в переменной index записывается первый элемент(первичный ключ) выбранной курсором
        selected_tuple = list1.get(index)  # в переменную selected_tuple будет храниться вся запись по данному индексу
        ent1.delete(0, END)
        ent1.insert(END, selected_tuple[1])
        ent2.delete(0, END)
        ent2.insert(END, selected_tuple[2])
        ent3.delete(0, END)
        ent3.insert(END, selected_tuple[3])
        ent4.delete(0, END)
        ent4.insert(END, selected_tuple[4])
    # except IndexError:
    #   pass


def view_command():
    list1.delete(0, END)
    for row in backend.view():  # функция - связка frontend'a и backend'a, добавляется в функционал кнопок
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_var.get(), author_var.get(), year_var.get(), isbn_var.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_var.get(), author_var.get(), year_var.get(), isbn_var.get())
    list1.delete(0, END)
    list1.insert(END, (title_var.get(), author_var.get(), year_var.get(), isbn_var.get()))


def update_command():
    backend.update(selected_tuple[0], title_var.get(), author_var.get(), year_var.get(), isbn_var.get())


def delete_command():
    backend.delete(selected_tuple[0])


window = Tk()

window.wm_title('Мои книги')

lab1 = Label(window, text='Название')
lab1.grid(row=0, column=0)

lab2 = Label(window, text='Автор')
lab2.grid(row=0, column=2)

lab3 = Label(window, text='Год')
lab3.grid(row=1, column=0)

lab4 = Label(window, text='Номер ISBN')
lab4.grid(row=1, column=2)

title_var = StringVar()
ent1 = Entry(window, textvariable=title_var)
ent1.grid(row=0, column=1)

year_var = StringVar()
ent2 = Entry(window, textvariable=year_var)
ent2.grid(row=1, column=1)

author_var = StringVar()
ent3 = Entry(window, textvariable=author_var)
ent3.grid(row=0, column=3)

isbn_var = StringVar()
ent4 = Entry(window, textvariable=isbn_var)
ent4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)  # привязка события (прочитать подробнее!)

but1 = Button(window, text='Посмотреть всё', width=12, command=view_command)
but1.grid(row=2, column=3)

but2 = Button(window, text='Найти запись', width=12, command=search_command)
but2.grid(row=3, column=3)

but3 = Button(window, text='Добавить запись', width=12, command=add_command)
but3.grid(row=4, column=3)

but4 = Button(window, text='Изменить', width=12, command=update_command)
but4.grid(row=5, column=3)

but5 = Button(window, text='Удалить', width=12, command=delete_command)
but5.grid(row=6, column=3)

but6 = Button(window, text='Закрыть', width=12, command=window.destroy)
but6.grid(row=7, column=3)

window.mainloop()
