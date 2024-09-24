from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Book,Member,Borrowing

engine = create_engine('sqlite:///library.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
 
member = Member(name="Mercy")
session.add(member)
session.commit()