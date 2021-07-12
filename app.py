from models import Base, session, Book, engine
import csv
import datetime
import time


########################################################################################################################
# Data clean up -
########################################################################################################################
def clean_date(date_str):
    """
    Converts string witten as April 6, 1992 to datetime
    :param date_str:
    :return: datetime
    """
    months = ['January', 'February',
              'March', 'April',
              'May', 'June',
              'July', 'August',
              'September', 'October',
              'November', 'December']
    split_date = date_str.split(' ')  # date becomes 3 element list ['January', '31,', '2021' ]
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
    """
    Cleans up price string takes price in format 10.99 and converts to integer
    takes
    :param price_str:
    :return:
    """
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
        return int(price * 100)  # __repr__ adds decimal place back in for printing


########################################################################################################################
########################################################################################################################


########################################################################################################################
# book methods -
########################################################################################################################
def add_book():
    """
    Adds book to the database.

    User is able to enter book object.

        MAIN MENU
        1) Add book
        2) View all books
        3) Search for a book
        4) Book analysis
        5) Exit
        What would you like to do? 1 <-- user input
        Title: Bible <-- user input
        Author: God <-- user input
        Published Date (Ex: April 6, 1992): January 1, 1900 <-- user input
        Price (Ex: 25.99): 1.99 <-- user input


        New Book Added:
        ------------------------------
        ------------------------------
        Book ID: 14
        Title: Bible
        Author: God
        Published: 1900-01-01
        price: $1.99
    :return:
    """
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
    print('\n\n\nNew Book Added: ')
    print_book(new_book)
    time.sleep(1.5)


def view_books():
    """
    Prints all books in a nice format. Uses the __repr__ method in the Book class
    Example:
        ------------------------------
        ------------------------------
        Book ID: 10
        Title: Data Analytics Made Accessible
        Author: Dr. Anil Maheshwari
        Published: 2014-05-01
        price: $9.99
        ------------------------------
        ------------------------------
        Book ID: 11
        Title: Hatchet
        Author: Gary Paulsen
        Published: 1992-04-06
        price: $34.89
        ------------------------------
        ------------------------------
    :return:
    """
    for book in session.query(Book):
        print_book(book)


def print_book(book):
    """
    Prints a book object in a nice format. Uses the __repr__ method in the Book class
    Example:
        ------------------------------
        ------------------------------
        Book ID: 11
        Title: Hatchet
        Author: Gary Paulsen
        Published: 1992-04-06
        price: $34.89
        ------------------------------
        ------------------------------
    :param book:
    :return:
    """
    print('-' * 30, '\n', '-' * 30, sep='')
    print(book)


def search_book(choice):
    """
    Takes choice (integer) and queries the Book class for a given attribute.
    Returns a Book class object
    :param choice:
    :return:
    """
    while True:
        if choice == 1:
            book_id = input('Book ID: ')
            book = session.query(Book).filter(Book.id == book_id).one()
            return book
        if choice == 2:
            title = input('Title: ')
            book = session.query(Book).filter(Book.title == title).one()
            return book
        if choice == 3:
            book_id = input('Book ID: ')
            book = session.query(Book).filter(Book.id == book_id).one()
            return book


########################################################################################################################
########################################################################################################################


########################################################################################################################
# Menus - All program menus and menu template
########################################################################################################################
def menu_template(heading, option_list):
    """
    Creates a menu template. Takes menu title (heading) and a list of menu options (option_list).
    User chooses a function by entering corresponding number.

    Example:
            MENU NAME --> heading
            1) Item1 --> option_list[0]
            2) Item2 --> option_list[1]
            3) Item3 --> option_list[2]
            ....

            What would you like to do?
    :param heading:
    :param option_list:
    :return:
    """
    while True:

        print(f'\n{heading}')
        for i in range(len(option_list)):
            print(f'\r{i + 1}) {option_list[i]}')

        choice = input('What would you like to do? ')
        if int(choice) in range(1, len(option_list) + 1):
            return int(choice)
        else:
            input(f'''
            \rPlease choose on of the options above
            \rA number from 1-{len(option_list)}.
            \rPress ENTER to try again''')


def main_menu():
    """
    Creates the main menu. User chooses a function by entering corresponding number.

    Example:
            MAIN MENU
            1) Add book
            2) View all books
            3) Search for a book
            4) Book analysis
            5) Exit
            What would you like to do?
    """
    menu_list = ('Add book', 'View all books', 'Search for a book', 'Book analysis', 'Exit')
    while True:
        choice = menu_template('MAIN MENU', menu_list)
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
    """
    Creates the search menu. User chooses a function by entering corresponding number.

    Example:
                SEARCH MENU
            1) ID
            2) Title
            3) Author
            4) Published Date
            5) Return to Main Menu
            What would you like to do?

    :return: Book class object
    """
    menu_list = ('ID', 'Title', 'Author', 'Published Date', 'Return to Main Menu')
    while True:
        choice = menu_template('SEARCH MENU', menu_list)
        search_term = input(f'Enter the Book\'s {menu_list[choice - 1]}: ')
        if choice == 1:
            book = session.query(Book).filter(Book.id == search_term).one()
        elif choice == 2:
            book = session.query(Book).filter(Book.title == search_term).one()
        elif choice == 3:
            book = session.query(Book).filter(Book.author == search_term).one()
        elif choice == 4:
            book = session.query(Book).filter(Book.published_date == search_term).one()
        else:
            return main_menu()
        print_book(book)
        return edit_menu(book)


def edit_menu(book):
    """

    :param book:
    :return:
    """
    menu_list = ('Edit', 'Delete', 'Return to search', 'Return to Main Menu')
    while True:
        choice = menu_template('EDIT MENU', menu_list)
        if choice == 1:
            before = book.boo
            user_input = input(f'Book ID: {book.id}-->')
            if user_input == '':
                book.id = int(user_input)
            user_input = input(f'Title: {book.title}-->')
            if user_input == '':
                book.title = user_input
            book.author = input(f'Author: {book.author}-->')
            if user_input == '':
                book.author = user_input
            book.published_date = input(f'Published Date: {book.published_date}-->')
            if user_input == '':
                book.published_date = datetime.date(user_input)
            book.price = input(f'Price: {book.price}-->')
            if user_input == '':
                book.price = int(user_input)
            session.add(book)
            session.commit()
            print_book(book)
            return edit_menu(book)
        if choice == 2:
            book.delete(book)
            print('Deleted.')
            return main_menu()
        if choice == 3:
            search_menu()
        else:
            main_menu()


########################################################################################################################
########################################################################################################################

########################################################################################################################
# Menus - All program menus and menu template
########################################################################################################################
def add_csv():
    """
        adds books in suggested_books.csv to database
    """
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


########################################################################################################################
########################################################################################################################

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    main_menu()

#   if edit
#   ask user for name of book they would like to edit (use search function)
#   ask user for input (title, author, date published, price) while displaying queued value
#   endif

# if delete
#   ask user for name of book they would like to delete (use search function)
#   display book
#   ask user to confirm
#   delete book
#   print deleted message
