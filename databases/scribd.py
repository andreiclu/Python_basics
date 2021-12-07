import psycopg2
def create_table():
    conn=psycopg2.connect("dbname ='Database1' user='postgres' password='Fcsbnuesteaua8532' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity integer, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity,price):
    conn = psycopg2.connect("dbname ='Database1' user='postgres' password='Fcsbnuesteaua8532' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES('%s','%s','%s')", (item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname ='Database1' user='postgres' password='Fcsbnuesteaua8532' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM STORE")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname ='Database1' user='postgres' password='Fcsbnuesteaua8532' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("Delete from store where item=%s",(item,))
    conn.commit()
    conn.close()


def update(quantity,price,item):
    conn = psycopg2.connect("dbname ='Database1' user='postgres' password='Fcsbnuesteaua8532' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s where item=%s",(quantity,price,item))
    conn.commit()
    conn.close()






