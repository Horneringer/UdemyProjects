import sqlite3


class Database:
    def __init__(self,db):  # конструктор объекта, в нашем случае осуществляет подключение к базе данных, создаёт
        # курсор и таблицу, если её нет
        self.conn = sqlite3.connect(db)  # при создании объекта вместо db подставляется название базы данных
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year INTEGER, "
            "isbn INTEGER)")
        self.conn.commit()
    
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()
    
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows
    
    def search(self, title='', author='', year='',
               isbn=''):  # если один,два или три параметра не будут указаны, поиск пройдёт
        # только по заполненному, ошибки не будет(аргументам присвоены пустые строки по умолчанию)
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                         (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows
    
    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
    
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()
    
    def __del__(self):  # деструктор объекта, в нашем случае закрывает соединение с базой
        self.conn.close()

# insert("Заговор корпорации Амбрелла", "Стефани Перри", 1998, 17405)
# delete(2)
# update(3, "Бухта Калибан", "Стефани Перри", 1998, 17405)
# print(view())

# print(search(author="Ник Горькавый"))
