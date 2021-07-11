# import models
from models import Base, session, Book, engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)
# begin main loop
# print main menu - add, search, analysis, exit, view

# if add
#   ask user for input (title, author, date published, price)
#   display added book on screen with confirm or edit message
# endif

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

# if delete
#   ask user for name of book they would like to delete (use search function)
#   display book
#   ask user to confirm
#   delete book
#   print deleted message


# data cleaning

