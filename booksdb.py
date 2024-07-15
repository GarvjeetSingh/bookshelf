from google.cloud import firestore


def read(book_id):
    """
    Return the details for a single book.
    """

    # retrieve a book from the database by ID
    data = db[str(book_id)]
    return data


def create(data):
    """
    Create a new book and return the book details.
    """

    # get a new ID for the book
    book_id = get_next_id()

    # set the ID in the book data
    data['id'] = book_id

    # store book in database
    db[book_id] = data
    return data


def update(data, book_id):
    """
    Update an existing book, and return the updated book's details.
    """

    # book ID should always be a string
    book_id_str = str(book_id)

    # add ID to the book data
    data['id'] = book_id_str

    # update book in the database
    db[book_id_str] = data
    return data


def delete(book_id):
    """
    Delete a book in the database.
    """

    # remove book from database
    del db[str(book_id)]

    # no return required


def list():
    """
    Return a list of all books in the database.
    """

    # empty list of books
    books = []

    # retrieve each item in database and add to the list
    for k in db:
        books.append(db[k])

    # return the list
    return books
