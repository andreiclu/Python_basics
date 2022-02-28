import pymysql
from e_shop import *

with pymysql.connect(host="localhost", password='Fcsbnuesteaua8532', database='car_rental_agency') as connection:
    print("connected!")

    drop_database = "drop database if exists e_shop"
    create_database = "create database if not exists e_shop"
    open_database = "use e_shop"
    print("use_e_shop!")
    create_table_users = """create table if not exists users(
    id int primary key auto_increment, 
    username varchar(100), 
    password varchar(100), 
    first_name text, 
    last_name text, 
    email varchar(100)
    )"""
    create_table_carts = """create table if not exists carts(
    id int auto_increment primary key, 
    user_id int,
    status varchar(25), 
    foreign key (user_id) references users(id)
    )"""
    create_table_cart_items = """create table if not exists cart_items(
    id int auto_increment primary key, 
    quantity int, 
    product_id int,
    cart_id int,
    foreign key (cart_id) references carts(id),
    foreign key (product_id) references products(id)
    )"""
    create_table_tags = """create table if not exists tags(
    id int auto_increment primary key, 
    tag varchar(100)    
    )"""
    create_table_products_tags= """create table if not exists products_tags(
    product_id int,
    tag_id int,
    foreign key (tag_id) references tags(id),
    foreign key (product_id) references products(id)
    )"""
    create_table_discounts = """create table if not exists discounts(
    id int auto_increment primary key,
    nth int default 1, 
    value decimal(10,2), 
    percent int, 
    product_id int,
    foreign key (product_id) references products(id)
    )"""
    with connection.cursor() as cursor:
        cursor.execute(drop_database)
        cursor.execute(create_database)
        cursor.execute(open_database)
        cursor.execute(create_table_categories)
        cursor.execute(create_table_products)
        cursor.execute(create_photos)
        cursor.execute(create_products_photos)
        cursor.execute(create_table_users)
        cursor.execute(create_table_carts)
        cursor.execute(create_table_cart_items)
        cursor.execute(create_table_tags)
        cursor.execute(create_table_products_tags)
        cursor.execute(create_table_discounts)