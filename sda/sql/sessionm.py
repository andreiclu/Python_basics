from sqlalchemy.orm import sessionmaker

from sda.sql.ex1 import eng
from sda.sql.sql_alchemy import Product

Session = sessionmaker(bind=eng)
session = Session()
products = session.query(Product).all()
print(products)
