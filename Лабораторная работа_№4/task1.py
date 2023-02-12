import doctest


class Chess:
    """ Базовый класс: шахматная партия."""
    def __init__(self, time: int, time_off_1: float, time_off_2: float, player_1: str, player_2: str):
        """
        :param time: время на игру для каждого игрока (мин)
        :param time_off_1: время, потраченное игроком 1
        :param time_off_2: время, потраченное игроком 2
        :param player_1: уровень игрока 1
        :param player_2: уровень игрока 2
        Необходимо провести проверки типов аргументов.
        Также необходима проверка (time_off_1 и time_off_2) < time
        Пример:
        >>> chess_1 = Chess(20, 10.0, 10.0, "любитель", "гроссмейстер")
        """
        self.time = time
        self.time_off_1 = time_off_1
        self.time_off_2 = time_off_2
        self.player_1 = player_1
        self.player_2 = player_2

    def __str__(self):
        """Магический метод __str__"""
        return f"Игра между {self.player_1} и {self.player_2}. Время на игру {self.time}"

    def __repr__(self):
        """Магический метод __repr__"""
        return f"{self.__class__.__name__}(player_1={self.player_1!r}, player_2={self.player_2!r}, time={self.time!r})"

    def chances(self):
        """Метод на основании базы данных историй патрий просчитывает шансы игроков на победу на основании
        их уровня игры и оставшегося времени.
        :return: Шансы игрока 1 = ...% Шансы игрока 2 = ...%
        Пример:
        >>> chess_1 = Chess(20, 10.0, 10.0, "любитель", "гроссмейстер")
        >>> chess_1.chances()
        """
        ...

    def time_to_end(self):
        """ Метод вычисляет, сколько времени осталось у 1 и 2 игроков соответственно.
        :return:    Оставшееся время 1 игрока. Оставшееся время воторого игрока
        Пример:
        >>> chess_1 = Chess(20, 10.0, 10.0, "любитель", "гроссмейстер")
        >>> chess_1.time_to_end()
        'Оставшееся время 1 игрока 10.0. Оставшееся время 2 игрока 10.0.'
        """
        return f"Оставшееся время 1 игрока {self.time - self.time_off_1}. Оставшееся время 2 игрока {self.time - self.time_off_2}."


class Blitz(Chess):
    """ Подкласс блиц партии.
    Уровни игроков остаются преждними. Шансы на победу тоже. Значит метод chance наследуется.
    Информации, необходимой для передачи пользователю нет. Значит методы str и repr наследуются
    Правила подсчета оставшегося времени изменились. Данный метод перегружаем.
    Необходимые проверки - аналогично базовому методу"""
    def __init__(self, time: int, time_off_1: float, time_off_2: float, player_1: str, player_2: str, move_num: int):
        """
        :param time: время на игру для каждого игрока (мин)
        :param time_off_1: время, потраченное игроком 1
        :param time_off_2: время, потраченное игроком 2
        :param player_1: уровень игрока 1
        :param player_2: уровень игрока 2
        Необходимо провести проверки типов аргументов.
        Также необходима проверка (time_off_1 и time_off_2) < time
        Пример:
        >>> chess_2 = Blitz(5, 2.0, 2.0, "любитель", "гроссмейстер", 10)
        """
        super().__init__(time, time_off_1, time_off_2, player_1, player_2)
        self.time = time
        self.time_off_1 = time_off_1
        self.time_off_2 = time_off_2
        self.player_1 = player_1
        self.player_2 = player_2
        self.move_num = move_num

    def time_to_end(self):
        """ Метод вычисляет, сколько времени осталось у 1 и 2 игроков соответственно.
        Метод необходимо перегрузить, так как в блице за каждый ход начисляется дополнительное время.
        :return:    Оставшееся время 1 игрока. Оставшееся время воторого игрока
        Пример:
        >>> chess_2 = Blitz(5, 2.0, 2.0, "любитель", "гроссмейстер", 10)
        >>> chess_2.time_to_end()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass

