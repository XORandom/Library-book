
import config_

class Book:
    def __init__(self, id_, name_, pages_):
        self.id = id_
        self.name = name_
        self.pages = pages_

    def __str__(self):
        return f'Книга \"{self.name}\"'

    def __repr__(self):
        return f'{self.__class__.__name__}(id_={self.id}, name_={self.name}\'' \
               f'pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if not books:
            self.data = []
        else:
            self.data = books

    def get_next_book_id(self):
        if not self.data:
            return 1
        sort_data = sorted(self.data, key=lambda book: book.id)
        print(sort_data[-1])
        return sort_data[-1]

    def get_index_by_book_id(self, index_):
        for i, book in enumerate(self.data):
            if book.id == index_:
                return i + 1
        raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    list_books = [Book(config_.BOOKS_DATABASE[i]["id"],
                       config_.BOOKS_DATABASE[i]["name"],
                       config_.BOOKS_DATABASE[i]["pages"]) for i in range(2)]
    print(list_books)
    list_books = [Book(book_dict["id"],
                       book_dict["name"],
                       book_dict["pages"]) for book_dict in config_.BOOKS_DATABASE]
    print(list_books)

    library = Library(list_books)
    # print(library.get_index_by_book_id(1))
    # print(library.get_next_book_id())
