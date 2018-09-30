import psycopg2


def create_table():
    conn = psycopg2.connect("dbname ='database 1' user = 'postgres' password = 'postgres' host = 'localhost' port = "
                            "'5432'")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, PRICE REAL)')
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname ='database 1' user = 'postgres' password = 'postgres' host = 'localhost' port = "
                            "'5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))  # каждый раз при вызове функции с
    # параметрами, параметры будут подставдяться в аргументы и вставляться в таблицу в правильном порядке; данный
    # вариант записи является более защищённым!
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname ='database 1' user = 'postgres' password = 'postgres' host = 'localhost' port = "
                            "'5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname ='database 1' user = 'postgres' password = 'postgres' host = 'localhost' port = "
                            "'5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname ='database 1' user = 'postgres' password = 'postgres' host = 'localhost' port = "
                            "'5432'")
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item = %s', (quantity, price, item))  # после ключевого
    # слова SET указываем поля,
    # которые хотим изменить
    conn.commit()
    conn.close()


create_table()
update(24, 8, 'Apple')
# insert("Orange", 10, 15)
# delete("Orange")
print(view())
