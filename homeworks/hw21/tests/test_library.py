import pytest
from loguru import logger
from homeworks.hw21.library.book import Book
from homeworks.hw21.library.reader import Reader


@pytest.fixture
def book_fixture():
    logger.info("Создание экземпляра книги 'Title' от автора 'Author'")
    return Book("Title", "Author", 100, "12345")


@pytest.fixture
def reader_vasyl_fixture():
    logger.info("Создание читателя Vasyl")
    return Reader("Vasyl")


@pytest.fixture
def reader_maria_fixture():
    logger.info("Создание читателя Maria")
    return Reader("Maria")


def test_book_creation(book):
    logger.info("Проверяем создание книги")
    assert book.book_name == "Title"
    assert book.author == "Author"
    assert book.num_pages == 100
    assert book.isbn == "12345"
    assert book.is_reserved is False
    assert book.is_given is False
    assert book.current_user is None
    logger.debug(f"Созданная книга: {vars(book)}")


def test_reader_creation(reader_vasyl):
    logger.info("Проверяем создание читателя Vasyl")
    assert reader_vasyl.name == "Vasyl"


def test_reserve_book_success(book, reader_vasyl):
    logger.info("Vasyl резервирует книгу")
    result = reader_vasyl.reserve_book(book)
    logger.debug(f"Состояние книги после резервирования: {vars(book)}")

    assert result is True
    assert book.is_reserved is True
    assert book.current_user == reader_vasyl


def test_reserve_book_already_reserved(book, reader_vasyl, reader_maria):
    logger.info("Vasyl резервирует книгу, затем Maria пытается зарезервировать ту же")
    reader_vasyl.reserve_book(book)
    result = reader_maria.reserve_book(book)
    logger.debug(f"Результат попытки Maria: {result}, текущее состояние: {vars(book)}")

    assert result is False
    assert book.current_user == reader_vasyl


def test_reserve_book_already_given(book, reader_vasyl, reader_maria):
    logger.info("Vasyl берёт книгу, Maria пытается её зарезервировать")
    reader_vasyl.get_book(book)
    result = reader_maria.reserve_book(book)
    logger.debug(f"Результат: {result}, книга: {vars(book)}")

    assert result is False
    assert book.is_given is True
    assert book.current_user == reader_vasyl


def test_cancel_reserve_success(book, reader_vasyl):
    logger.info("Vasyl резервирует и отменяет резервирование книги")
    reader_vasyl.reserve_book(book)
    result = reader_vasyl.cancel_reserve(book)
    logger.debug(f"Состояние после отмены: {vars(book)}")

    assert result is True
    assert book.is_reserved is False
    assert book.current_user is None


def test_cancel_reserve_wrong_user(book, reader_vasyl, reader_maria):
    logger.info("Vasyl резервирует книгу, Maria пытается отменить резервирование")
    reader_vasyl.reserve_book(book)
    result = reader_maria.cancel_reserve(book)
    logger.debug(f"Результат: {result}, книга: {vars(book)}")

    assert result is False
    assert book.is_reserved is True
    assert book.current_user == reader_vasyl


def test_get_book_success_free(book, reader_vasyl):
    logger.info("Vasyl получает свободную книгу")
    result = reader_vasyl.get_book(book)
    logger.debug(f"После получения книги: {vars(book)}")

    assert result is True
    assert book.is_given is True
    assert book.current_user == reader_vasyl
    assert book.is_reserved is False


def test_get_book_reserved_by_same_user(book, reader_vasyl):
    logger.info("Vasyl резервирует и затем получает книгу")
    reader_vasyl.reserve_book(book)
    result = reader_vasyl.get_book(book)
    logger.debug(f"После получения книги: {vars(book)}")

    assert result is True
    assert book.is_given is True
    assert book.current_user == reader_vasyl
    assert book.is_reserved is False


def test_get_book_reserved_by_other_user(book, reader_vasyl, reader_maria):
    logger.info("Vasyl резервирует книгу, Maria пытается получить её")
    reader_vasyl.reserve_book(book)
    result = reader_maria.get_book(book)
    logger.debug(f"Результат: {result}, книга: {vars(book)}")

    assert result is False
    assert book.is_given is False
    assert book.current_user == reader_vasyl
    assert book.is_reserved is True


def test_get_book_already_given(book, reader_vasyl, reader_maria):
    logger.info("Vasyl берёт книгу, Maria пытается получить её")
    reader_vasyl.get_book(book)
    result = reader_maria.get_book(book)
    logger.debug(f"Результат: {result}, книга: {vars(book)}")

    assert result is False
    assert book.is_given is True
    assert book.current_user == reader_vasyl


def test_return_book_success(book, reader_vasyl):
    logger.info("Vasyl возвращает книгу")
    reader_vasyl.get_book(book)
    result = reader_vasyl.return_book(book)
    logger.debug(f"После возврата книги: {vars(book)}")

    assert result is True
    assert book.is_given is False
    assert book.current_user is None


def test_return_book_wrong_user(book, reader_vasyl, reader_maria):
    logger.info("Vasyl берёт книгу, Maria пытается вернуть её")
    reader_vasyl.get_book(book)
    result = reader_maria.return_book(book)
    logger.debug(f"Результат: {result}, книга: {vars(book)}")

    assert result is False
    assert book.is_given is True
    assert book.current_user == reader_vasyl
