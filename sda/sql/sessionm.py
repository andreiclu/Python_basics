from sqlalchemy.orm import sessionmaker

from sda.sql.sql_alchemy import Product, eng

Session = sessionmaker(bind=eng)
session = Session()
products = session.query(Product).all()
print(products)

