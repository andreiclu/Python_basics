import pymysql

with pymysql.connect(host="localhost", password='Fcsbnuesteaua8532', database='car_rental_agency') as connection:
    print("connected!")

    create_database = "create database if not exists e_shop"
    open_database = "use e_shop"
    create_table_categories = "create table if not exists categories(id int primary key auto_increment, name varchar(100), description text)"
    create_table_products = "create table if not exists products(id int primary key auto_increment, name varchar(100), description text, stock int, price decimal(10,2), category_id int, foreign key (category_id) references categories(id))"
    create_photos = "create table if not exists photos(id int primary key auto_increment, url varchar(100))"
    create_products_photos = """create table if not exists products_photos(
    product_id int,
    photo_id int,
    primary key(product_id, photo_id),
    foreign key(product_id) references products(id),
    foreign key(photo_id) references photos(id)
    )"""
    if __name__ == '__main__':
        with pymysql.connect(host="localhost", password='Fcsbnuesteaua8532', database='car_rental_agency') as connection:
            print("connected!")

            with connection.cursor() as cursor:
                cursor.execute(create_database)
                cursor.execute(open_database)
                cursor.execute(create_table_categories)
                cursor.execute(create_table_products)
                cursor.execute(create_photos)
                cursor.execute(create_products_photos)

