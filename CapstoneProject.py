import  sqlite3

conn=sqlite3.connect("database_library")
#
c= conn.cursor()


# create table library programming

c.execute("""CREATE TABLE library  (
        id INTEGER ,
        title TEXT,
        autor TEXT,
        qty INTEGER)""")

# insert records into the library table

c.execute("""INSERT INTO library VALUES(?,?,?,?)""",(3001,'A Tale of Two Cities',"Charles Dickensen",30))
c.execute("""INSERT INTO library VALUES(?,?,?,?)""",(3002,'Harry Potter and the Philosopher Stone',"J.K Rowling",40))
c.execute("""INSERT INTO library VALUES(?,?,?,?)""",(3003,'The Lion, the Witch and the Wardrobe',"C.S. Lewis",25))
c.execute("""INSERT INTO library VALUES(?,?,?,?)""",(3004,'The Lord of the Rings',"J.R.R. Tolkien",37))
c.execute("""INSERT INTO library VALUES(?,?,?,?)""",(3005,'Alice in Wonderlands',"Lewis Carroll",12))

conn.commit()

# define function to add a new collection of books
def enter_book():
    # loop until the user types a numeric value for the id number
    while True:
        try:
            id = int(input("Select an id number \n"))
            break
        except:
            print("Please enter a numeric value \n")
            continue
    # enter title of the book
    title = input("Select title \n")
    # enter autor of the book
    autor = input("Enter the autor \n")

    # loop until the user types a numeric value for the quantity
    while True:
        try:
            qty = int(input("Enter the quantity \n"))
            break
        except:
            print("Please enter a numeric value \n")
            continue
    # insert new record into library table and show
    c.execute("""INSERT INTO library VALUES(?,?,?,?)""", (id, title, autor, qty))
    conn.commit()
    print(f"Your book  {id, title, autor, qty} has been added to the database")

# define function to update book
def update_book():
    # get variables from the user for the name of the present book,the place where to replace the value and the new value
    book_update=input("Select the name of the book that you want to update \n")
    change=input("Select what do you want to change: title, autor or quantity \n")
    new_value=input("select the new value to replace \n")

    # condition statements on what the user chooses to replace the value
    if change == "title" :
        c.execute("""UPDATE  library SET title = ? WHERE  title = ? """, (new_value, book_update,))
        conn.commit()
    elif change == "autor":
        c.execute("""UPDATE  library SET autor = ? WHERE  title = ? """, (new_value, book_update,))
        conn.commit()
    # if the user select quantity to change, make sure that he types a valid numeric variable
    elif change == "quantity":
        while True:
            try:
                new_value = int(new_value)
                break
            except:
                print("Please enter a numeric value \n")
                new_value = input("select the numeric new value to replace the quantity \n")
                continue
        # replace the old value with the new one and show the title of the book chosen
        c.execute("""UPDATE  library SET qty = ? WHERE  title = ? """, (new_value, book_update,))
        conn.commit()
        print(f"The book {book_update} has been updated to successfully")

def delete_book():
    # ask the user the title of the book to delete and delete the record
    delete=input("Write the name title that you want to delete \n")
    c.execute("""DELETE FROM library WHERE  title = ? """, (delete,))
    conn.commit()
    print(f"The book {delete} has been deleted from the table")

def search_book():
    # ask the user the title of the book to view and show the record
    book=input("Select the book title that you want to view")
    c.execute("""SELECT * FROM library WHERE  title = ? """, (book,))
    print(c.fetchone())


# Make a while loop that connects all the above functions and stops when the user types something different
while True:
    select=input("Select the action you want to do: enter, update, delete, search or anything else to exit \n")
    if select == "enter":
        enter_book()
    elif select == "update":
        update_book()
    elif select == "delete":
        delete_book()
    elif select == "search":
        search_book()
    else:
        break


