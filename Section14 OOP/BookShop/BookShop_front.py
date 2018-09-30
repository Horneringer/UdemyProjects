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
from BookShop.BookShop_back import Database  # импортирование класса Database из модуля BookShop_back

database = Database('books.db')  # создаём объект класса Database и храним его в переменной database


class Graphic:
    
    def __init__(self, parent):
        self.widgets(parent)  # при создании объекта конструктор вызывает метод рисования графических виджетов
    
    def widgets(self, window): # метод, создающий графический интерфейс
        
        self.lab1 = Label(window, text='Название')
        self.lab1.grid(row=0, column=0)
        
        self.lab2 = Label(window, text='Автор')
        self.lab2.grid(row=0, column=2)
        
        self.lab3 = Label(window, text='Год')
        self.lab3.grid(row=1, column=0)
        
        self.lab4 = Label(window, text='Номер ISBN')
        self.lab4.grid(row=1, column=2)
        
        self.title_var = StringVar()
        self.ent1 = Entry(window, textvariable=self.title_var)
        self.ent1.grid(row=0, column=1)
        
        self.year_var = StringVar()
        self.ent2 = Entry(window, textvariable=self.year_var)
        self.ent2.grid(row=1, column=1)
        
        self.author_var = StringVar()
        self.ent3 = Entry(window, textvariable=self.author_var)
        self.ent3.grid(row=0, column=3)
        
        self.isbn_var = StringVar()
        self.ent4 = Entry(window, textvariable=self.isbn_var)
        self.ent4.grid(row=1, column=3)
        
        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        
        self.sb1 = Scrollbar(window)
        self.sb1.grid(row=2, column=2, rowspan=6)
        
        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)
        
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)  # привязка события (прочитать подробнее!)
        
        self.but1 = Button(window, text='Посмотреть всё', width=12, command=self.view_command)
        self.but1.grid(row=2, column=3)
        
        self.but2 = Button(window, text='Найти запись', width=12, command=self.search_command)
        self.but2.grid(row=3, column=3)
        
        self.but3 = Button(window, text='Добавить запись', width=12, command=self.add_command)
        self.but3.grid(row=4, column=3)
        
        self.but4 = Button(window, text='Изменить', width=12, command=self.update_command)
        self.but4.grid(row=5, column=3)
        
        self.but5 = Button(window, text='Удалить', width=12, command=self.delete_command)
        self.but5.grid(row=6, column=3)
        
        but6 = Button(window, text='Закрыть', width=12, command=window.destroy)
        but6.grid(row=7, column=3)
    
    # в параметрах объекта указываем путь и название бызы, чтобы подставить в класс инициализации
    
    # баг с пустым listbox'ом можно исправить и через try-except
    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[
                0]  # в переменной index записывается первый элемент(первичный ключ) выбранной
            # курсором записи
            selected_tuple = self.list1.get(
                index)  # в переменную selected_tuple будет храниться вся запись по данному индексу
            self.ent1.delete(0, END)
            self.ent1.insert(END, selected_tuple[1])
            self.ent2.delete(0, END)
            self.ent2.insert(END, selected_tuple[3])
            self.ent3.delete(0, END)
            self.ent3.insert(END, selected_tuple[2])
            self.ent4.delete(0, END)
            self.ent4.insert(END, selected_tuple[4])
        except IndexError:
            pass
    
    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():  # функция - связка frontend'a и backend'a, добавляется в функционал кнопок
            self.list1.insert(END, row)
    
    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_var.get(), self.author_var.get(), self.year_var.get(),
                                   self.isbn_var.get()):
            self.list1.insert(END, row)
    
    def add_command(self):
        database.insert(self.title_var.get(), self.author_var.get(), self.year_var.get(), self.isbn_var.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_var.get(), self.author_var.get(), self.year_var.get(), self.isbn_var.get()))
    
    def update_command(self):
        database.update(selected_tuple[0], self.title_var.get(), self.author_var.get(), self.year_var.get(),
                        self.isbn_var.get())
    
    def delete_command(self):
        database.delete(selected_tuple[0])


window = Tk()

window.wm_title('Мои книги')

graph = Graphic(window)  # объект класса

window.mainloop()
