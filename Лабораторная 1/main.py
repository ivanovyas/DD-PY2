# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class NationalFootballTeam:
    def __init__(self, players_accept: int, players_avaliable : int):
        """
        Создание и подготовка к работе объекта "Сборная по футболу"
        :param players_accept: Число игроков в заявке
        :param players_avaliable: Число игрков, способных выйти на поле после вечеринки накануне
        Примеры:
        >>> team_1 = NationalFootballTeam(25, 11)  # инициализация экземпляра класса
        """
        if not isinstance(players_accept, (int)):
            raise TypeError("Количество игроков в заявке должно быть типа int")
        if players_accept != 25:
            raise ValueError("Количество игроков в заявке должно быть равно 25")
        self.players_accept = players_accept

        if not isinstance(players_avaliable, (int)):
            raise TypeError("Количество игроков в заявке должно быть типа int")
        if players_avaliable > players_accept:
            raise ValueError("Готовых игрков должно быть не больше, чем в заявке")
        self.occupied_volume = players_avaliable

    def is_team_ready(self) -> bool:
        """
        Функция которая проверяет допускается ли команда к матчу
        с учетом регламента по минимальному количеству игроков (минимум 11 живых человек)
        :return: Допущена ли команда
        Примеры:
        >>> team_2 = NationalFootballTeam(25, 24)
        >>> team_2.is_team_ready()
        """
        ...

    def red_cards(self, cards: int) -> None:
        """
        Происходит удаление в команде.
        :param cards: Количество полученных красных карточек
        :raise ValueError: Если количество игроков, способных играть, с учетом удалений становится менее 7, то вызываем ошибку
        Примеры:
        >>> team_1 = NationalFootballTeam(25, 11)
        >>> team_1.red_cards(2)
        """
        if not isinstance(cards, (int,)):
            raise TypeError("Количество красных карточек должно быть типа int")
        if cards < 0:
            raise ValueError("Количество карточек должно быть положительным числом")
        ...

class Ustav:
    def __init__(self, errors: int, errors_allowed: int):
        """
        Создание и подготовка к работе объекта "Устав"
        :param errors: Количество отступлений от устава, допущенных при обращенийй к старшему по званию
        :param errors_allowed: Количество отступлений от устава при обращении,
        которое под силу выдержать старшему по званию
        Примеры:
        >>> ustav_1 = Ustav(1, 0)  # инициализация экземпляра класса
        """
        if not isinstance(errors, (int)):
            raise TypeError("Количество ошибок должно быть типа int")
        if errors < 0:
            raise ValueError("Количество ошибок не может быть меньше 0")
        self.errors = errors

        if not isinstance(errors_allowed, (int)):
            raise TypeError("Количество допустимых ошибок должно быть типа int")
        if errors_allowed != 0:
            raise ValueError("Количество допустимых ошибок должно равняться 0")
        self.errors_allowed = errors_allowed

    def is_starshina_happy(self) -> bool:
        """
        Функция которая проверяет, не допущено ли ошибок больше, чем сможет принять старший по званию
              :return: Допустимо ли обращение
        Примеры:
        >>> ustav_1 = Ustav(5, 0)
        >>> ustav_1.is_starshina_happy()
        """
        ...

    def metod_vospitaniya(self, povtor: int):
        """
        Сколько повторных обращений по уставу необходимо произвести.
        :param povtor: Количество повторений обращения на одну допущенную ошибку
              :return: Количество повторных обращений.
        Примеры:
        >>> ustav_1 = Ustav(15, 0)
        >>> ustav_1.metod_vospitaniya(2)
        """
        if not isinstance(povtor, (int,)):
            raise TypeError("Количество повторений должно быть типа int")
        if povtor < 0:
            raise ValueError("Количество повторений должно быть положительным числом")
        ...


class Laboratornaya:
    def __init__(self, time_to_deadline: Union[int, float], execution_time: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Лабораторная"
        :param time_to_deadline: Время до дедлайна (в часах)
        :param execution_time: Примерное время на выполнения задания (в часах)
        Примеры:
        >>> laboratornaya_1 = Laboratornaya(1.5, 1.5)  # инициализация экземпляра класса
        """
        if not isinstance(time_to_deadline, (int, float)):
            raise TypeError("Количество времени до дедлайна должно быть типа int или float")
        if time_to_deadline < 0:
            raise ValueError("Количество времени до дедлайна не может быть меньше 0")
        self.time_to_deadline = time_to_deadline

        if not isinstance(execution_time, (int, float)):
            raise TypeError("Количество времени выполнения должно быть типа int или float")
        if execution_time < 0:
            raise ValueError("Количество времени выполнения не может быть меньше 0")
        self.execution_time = execution_time

    def timing(self) -> bool:
        """
        Функция которая проверяет, успеем ли мы сделать лабораторную, выполняя ее со средней скоростью
              :return: Успеем ли выполнить лабораторную
        Примеры:
        >>> lab_1 = Laboratornaya(5, 5)
        >>> lab_1.timing()
        """
        ...

    def over_the_plan(self, slip: Union[int, float]) -> (int, float):
        """
        Во сколько раз быстрее среднего нужно делать работу, чтоб успеть к дедлайну,
        если случайно уснул на количство часов = slip.
        :param slip: Количество часов непредвиденного сна.
              :return: Кратность ускорения процесса выполнение работы (если ускорение требуется).
        Примеры:
        >>> lab_1 = Laboratornaya(24, 5)
        >>> lab_1.over_the_plan(12)
        """
        if not isinstance(slip, (int, float)):
            raise TypeError("Количество часов сна должно быть типа int или float")
        if slip < 0:
            raise ValueError("Количество часов сна должно быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass

