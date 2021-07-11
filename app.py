# import models
from models import Base, session, Book, engine
import csv
import datetime


# begin main loop

# print main menu - add, search, analysis, exit, view
def menu():
    while True:
        print(
            '''
            \nPROGRAMMING BOOKS
            \r1) Add book
            \r2) View all books
            \r3) Search for book
            \r4) Book Analysis`
            \r5) Exit
            ''')
        choice = input('What would you like to do? ')
        if int(choice) in range(1, 6):
            return int(choice)
        else:
            input('''
            \rPlease choose on of the options above
            \rA number from 1-5.
            \rPress ENTER to try again''')


#   if confirm
#       print changes made and add input (press any key to continue to exit to main menu)
#   endif

#   if edit
#   ask user for name of book they would like to edit (use search function)
#   ask user for input (title, author, date published, price) while displaying queued value
#   endif

# if search
#   ask user how they would like to search (title, author, date published, price)
#   endif

#   if option not in option list
#       print that is not an option
#   endif

# if add
#   ask user for input (title, author, date published, price)
#   display added book on screen with confirm or edit message
# endif


def clean_date(date_str):
    # convert string witten as April 6, 1992 to datetime
    months = ['January', 'February',
              'March', 'April',
              'May', 'June',
              'July', 'August',
              'September', 'October',
              'November', 'December']
    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].replace(',', ''))
        year = int(split_date[2])
        date = datetime.date(year, month, day)
    except ValueError:
        input('''
        \n************* DATE ERROR *************
        \rThe date format should include a valid Month Day, Year
        \rEx. April 6, 1992
        \rPress ENTER to try again.
        \r**************************************''')
        return None
    else:
        return date


def clean_price(price_str):
    # convert price string to integer
    try:
        price = float(price_str)
    except ValueError:
        input('''
        \n************* PRICE ERROR *************
        \rThe price should be a number without a currency symbol
        \rEx. 24.89  <-- do not include $
        \rPress ENTER to try again.
        \r***************************************''')
        return None
    else:
        return int(price * 100)


def add_csv():
    # add books in csv to database
    with open('suggested_books.csv') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title == row[0]).one_or_none()
            if book_in_db is None:
                title = row[0]
                author = row[1]
                published_date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, published_date=published_date, price=price)
                session.add(new_book)
        session.commit()


def add_book():
    title = input('Title: ')
    author = input('Author: ')
    while True:
        published_date = input('Published Date (Ex: April 6, 1992): ')
        published_date = clean_date(published_date)
        if type(published_date) == datetime.date:
            break
    while True:
        price = input('Price (Ex: 25.99): ')
        price = clean_price(price)
        if type(price) == int:
            break
    new_book = Book(title=title, author=author, published_date=published_date, price=price)


def main():
    app_running = True
    while app_running:
        # main loop
        choice = menu()
        if choice == 1:
            add_book()
        elif choice == 2:
            print('view book - coming soon')
            pass
        elif choice == 3:
            print('search book - coming soon')
            pass
        elif choice == 4:
            print('book analysis - coming soon')
            pass
        else:
            print('Good Bye!!!')
            break


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    main()

# if delete
#   ask user for name of book they would like to delete (use search function)
#   display book
#   ask user to confirm
#   delete book
#   print deleted message


# data cleaning
