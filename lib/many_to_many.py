class Book:
    _all_books = []

    def __init__(self, title):
        self._title = title
        self._contracts = []
        self.__class__._all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title should be a string!")
        self._title = value

    def contracts(self):
        return self._contracts
    
    def authors(self):
        return list(set(contract.author for contract in self._contracts))

class Author:
    all = []

    def __init__(self, name):
        self._name = name
        self._contracts = []
        self.__class__.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name should be a string!")
        self._name = value

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")

        if not isinstance(book, Book):
            raise Exception("Book must be of type Book")

        self._author = author
        self._book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)

        author._contracts.append(self)
        book._contracts.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date should be a string!")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties should be an integer!")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

