from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    borrowings = relationship('Borrowing', back_populates='member')

    def __repr__(self):
        return f"Member(id={self.id}, name={self.name})"

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    
    borrowings = relationship('Borrowing', back_populates='book')

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, author={self.author})"

class Borrowing(Base):
    __tablename__ = 'borrowings'
    
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    
    member = relationship('Member', back_populates='borrowings')
    book = relationship('Book', back_populates='borrowings')

    def __repr__(self):
        return f"Borrowing(id={self.id}, member_id={self.member_id}, book_id={self.book_id})"
