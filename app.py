from models import Base, session, Book, engine
import csv
import datetime


def menu(heading, option_list):
    while True:

        print(f'\n{heading}')
        for i in range(len(option_list)):
            print(f'\r{i+1}) {option_list[i]}')

        choice = input('What would you like to do? ')
        if int(choice) in range(1, 6):
            return int(choice)
        else:
            input('''
            \rPlease choose on of the options above
            \rA number from 1-5.
            \rPress ENTER to try again''')


def print_book(book):
    print('-' * 30, '\n', '-' * 30, sep='')
    print(book)


def search_book(choice):
    while True:
        if choice == 1:
            book_id = input('Book ID: ')
            book = session.query(Book).filter(Book.id == book_id).one()
            return book


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
    session.add(new_book)
    session.commit()


def view_books():
    for book in session.query(Book):
        print_book(book)


def main_menu():
    menu_list = ('Add book', 'View all books', 'Search for a book', 'Book analysis', 'Exit')
    while True:
        choice = menu('PROGRAMMING BOOKS', menu_list)
        if choice == 1:
            add_book()
            continue
        elif choice == 2:
            view_books()
            continue
        elif choice == 3:
            search_menu()
            continue
        elif choice == 4:
            print('book analysis - coming soon')
            continue
        else:
            print('Good Bye!!!')
            break
    return choice


def search_menu():
    menu_list = ('By Book ID', 'By Title', 'By Author', 'By Date', 'Return to Main Menu')
    while True:
        choice = menu('How would you like to search for a book?', menu_list)
        if choice == 1:
            book = search_book(1)
            print_book(book)
            continue
        elif choice == 2:
            book = search_book(2)
            print_book(book)
            continue
        elif choice == 3:
            book = search_book(3)
            print_book(book)
            continue
        elif choice == 4:
            book = search_book(4)
            print_book(book)
            continue
        elif choice == 5:
            return main_menu()
        return choice


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    main_menu()


#   if edit
#   ask user for name of book they would like to edit (use search function)
#   ask user for input (title, author, date published, price) while displaying queued value
#   endif

# if search
#   ask user how they would like to search (title, author, date published, price)
#   endif

# if delete
#   ask user for name of book they would like to delete (use search function)
#   display book
#   ask user to confirm
#   delete book
#   print deleted message
