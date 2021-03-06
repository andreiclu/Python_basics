from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker

from sda.sql.sessionm import session

Base = declarative_base()
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(Text)

    def __str__(self):
        return f'category {self.id}, {self.name}'

    def __init__(self, name):
        self.name = name


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(Text)
    stock = Column(Integer)
    price = Column(Float(2))
    category_id = Column(Integer, ForeignKey(Category.id))


class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100))

    def __str__(self):
        return f'photo {self.id}, {self.url}'


    def __int__(self, url):
        self.url = url

class ProductPhoto(Base):
    __tablename__ = 'products_photos'
    product_id = Column(Integer, ForeignKey(Product.id), primary_key=True)
    photo_id = Column(Integer, ForeignKey(Photo.id), primary_key=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100))
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id))
    status = Column(String(25))

class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey(Product.id))
    cart_id = Column(Integer, ForeignKey(Cart.id))


    def __init__(self, name, category_id, price, stock):
        self.name = name
        self.category_id = category_id
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'product {self.id}, {self.name}, {self.category_id}, {self.price}, {self.stock}'

    def __repr__(self):
        return str(self)



def add_product():
    pr_1 = Product('HP', 1, 1400, 15)
    pr_2 = Product('Dell', 1, 1700, 10)
    session.add_all([pr_1, pr_2])
    session.commit()


def show_products():
    products = session.query(Product).all()
    print(products)

def cart_value(cart_id):
    cart_items = session.query(CartItem).filter(CartItem.cart_id == cart_id).all()
    suma = 0
    for cart_item in cart_items:
        product = session.query(Product).filter(Product.id == cart_item.product_id).all()[0]
        suma = suma + cart_item.quantity * product.price

    return suma


if __name__ == '__main__':
    # add_product()
    # show_products()
    suma = cart_value(2)

