import psycopg2


def create_table():
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, PRICE REAL)')
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))  # каждый раз при вызове функции с
    # параметрами, параметры будут
    # подставдяться в аргументы и вставляться в таблицу в правильном порядке
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(quantity,price,item):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=?, price=? WHERE item = ?', (quantity, price, item))   # после ключевого
    # слова SET указываем поля,
    # которые хотим изменить
    conn.commit()
    conn.close()


# create_table()
# insert("Wine Glass", 8, 10)
# delete('Wine Glass')
# insert('Wine Glass', 5, 10)
update(6, 13, 'Wine Glass')
print(view())
