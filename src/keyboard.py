from src.item import Item


class Mixin:
    langs = ["EN", "RU"]
    __language = langs[0]

    def __str__(self):
        return self.__language

    @property
    def language(self):
        return self.__language

    @classmethod
    def change_lang(cls):
        cls.langs = [cls.langs[1], cls.langs[0]]
        cls.__language = cls.langs[0]
        return cls


class KeyBoard(Mixin, Item):
    def __init(self, __name: str, price: float, quantity: int):
        super().__init__(__name, price, quantity)

    def __str__(self):
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
