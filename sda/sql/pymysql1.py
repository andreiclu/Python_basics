import pymysql

with pymysql.connect(host="localhost", password='Fcsbnuesteaua8532', database='car_rental_agency') as connection:
    print("connected!")
    connection: pymysql.Connection = connection
    sql_statement = "select * from contact_request"

    with connection.cursor() as cursor:
        cursor.execute(sql_statement)
        print(cursor.fetchall())

    sql_statement2 = 'create table if not exists contact_request (id int primary key auto_increment, name varchar(100), phone varchar(20), email varchar(100), message text)'
    with connection.cursor() as cursor:
        cursor.execute(sql_statement2)
        print(cursor.fetchall())

    insert_statament = "insert into contact_request(name, phone, email, message) values(%s, %s, %s, %s)"
    value_tuple = ('John', '0755445466', 'johnmail@mail.com', 'message test something')
    with connection.cursor() as cursor:
        cursor.execute(insert_statament, value_tuple)
        connection.commit()

    insert_statament4 = "insert into contact_request(name, phone, email, message) values(%s, %s, %s, %s)"
    value_tuple_list = [
        ('John', '0755445466', 'johnmail@mail.com', 'message test something'),
        ('Johnny', '0722445466', 'johnnymail@mail.com', 'message test something else')
    ]
    with connection.cursor() as cursor:
        cursor.executemany(insert_statament4, value_tuple_list)
        connection.commit()


