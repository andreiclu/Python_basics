# Sa se creeze structura de tabele pentru un blog cu:
# utilizatori,
# articole, fiecare cu autor (utilizator)
# comentarii separate pe fiecare articol
# bonus: comentarii la comentarii
from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(Text)
    author_id = Column(Integer, ForeignKey(User.id))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer, ForeignKey(Article.id), nullable=True)
    content = Column(Text)
    parent_comment_id = Column(Integer, ForeignKey('comment.id'))


user = 'root'
password = 'Fcsbnuesteaua8532'
host = '127.0.0.1'
db = 'sqlalchemy_demo'
eng = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")
Base.metadata.create_all(eng)
