class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def author(self):
        return self._author  # внутри класса обращаемся к защищенному атрибуту


class PaperBook(Book):
    """ Подкласс бумажной книги. """
    def __init__(self, name: str, author: str, page: int):
        super().__init__(name, author)
        self.page = page

    def __str__(self):
        """Перегружаем метод, если необходимо отразить новую информацию (количество страниц)"""
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"

    def __repr__(self) -> str:
        """Перегружаем метод, если необходимо отразить новую информацию (количество страниц)"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = new_pages


class AudioBook(Book):
    """ Подкласс аудио-книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        """Перегружаем метод, если необходимо отразить ноую информацию (продолжительность)"""
        return f"Книга {self._name}. Автор {self._author}. Длительность {self.duration}"

    def __repr__(self) -> str:
        """Перегружаем метод, если необходимо отразить новую информацию (продолжительность)"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def durations(self) -> float:
        return self.durations

    @durations.setter
    def durations(self, new_durations: float) -> None:
        if not isinstance(new_durations, float):
            raise TypeError("Продолжительность должна быть типа Float")
        if new_durations <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.durations = new_durations

