class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = False
        self.reserved_by = None
        self.is_given = False
        self.is_given_to = None

    def reserve(self, reader):
        if not self.is_reserved and not self.is_given:
            self.is_reserved = True
            self.reserved_by = reader
            return True
        return False

    def cancel_reserve(self, reader):
        if self.reserved_by == reader:
            self.is_reserved = False
            self.reserved_by = None
            return True
        return False

    def get_book(self, reader):
        if self.is_given or (self.is_reserved and self.reserved_by != reader):
            return False

        self.is_given = True
        self.is_reserved = False
        self.is_given_to = reader
        return True

    def return_book(self, reader):
        if self.is_given_to == reader:
            self.is_given = False
            self.is_given_to = None
            return True
        return False
