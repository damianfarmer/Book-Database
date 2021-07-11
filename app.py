# import models
from models import Base, session, Book, engine


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
            \r4) Book Analysis
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


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 1:
            print('add book - coming soon')
            pass
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
    app()
# if delete
#   ask user for name of book they would like to delete (use search function)
#   display book
#   ask user to confirm
#   delete book
#   print deleted message


# data cleaning

