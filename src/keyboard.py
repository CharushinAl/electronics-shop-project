from src.item import Item


class Mixin:
    """Класс для смены языка клавиатуры"""
    langs = ["EN", "RU"]
    __language = langs[0]

    def __str__(self):
        """Возвращает данные для пользователя"""
        return self.__language

    @property
    def language(self):
        """Возвращает приватную __language"""
        return self.__language

    @classmethod
    def change_lang(cls):
        """Меняет язык"""
        cls.langs = [cls.langs[1], cls.langs[0]]
        cls.__language = cls.langs[0]
        return cls


class KeyBoard(Mixin, Item):
    """Класс клавиатуры, потомок Mixin, Item"""
    def __init__(self, __name: str, price: float, quantity: int):
        """Конструктор класса"""
        super().__init__(__name, price, quantity)

    def __str__(self):
        """Возвращает данные для пользователя"""
        return self.name

    @property
    def name(self):
        """Возвращает приватную __name"""
        return self.__name

    @name.setter
    def name(self, string):
        """Получает string и записывает в __name"""
        if type(string) is str:
            self.__name = string
        else:
            print('Передана не строка')
