
# Online Python - IDE, Editor, Compiler, Interpreter
from datetime import date


def ontrack_reading(books_goal: int, books_read: int, day_of_year: int = None) -> bool:
    if not day_of_year:
        day_of_year = int(date.today().strftime('%j'))
    expected_books_read = books_goal / 365 * day_of_year
    return books_read >= expected_books_read


if __name__ == "__main__":
    print(ontrack_reading(60, 2, 3))
