# create a database
from sqlalchemy import create_engine,  Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column('Published', Date)
    price = Column('Price', Integer)

    def __repr__(self):
        return f'Book ID: {self.id}' \
               f'\nTitle: {self.title}' \
               f'\nAuthor: {self.author}' \
               f'\nPublished: {self.published_date}' \
               f'\nprice: ${str(self.price)[:-2]}.{str(self.price)[-2:]}'
# -->books.db
# create a model
# -->title, author, date published, price
