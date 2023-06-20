"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
from src.item import Item
from src.phone import Phone
from src.exception import InstantiateCSVError


@pytest.fixture
def item1_2():
    Item.pay_rate = 1.1
    return Item("Декстоп", 400000, 2), Item("Клавиатура", 5000, 5)


def test_calculate_total_price(item1_2):

    assert item1_2[0].calculate_total_price() == 800000
    assert item1_2[1].calculate_total_price() == 25000


def test_apply_discount(item1_2):
    item1_2[0].apply_discount()
    item1_2[1].apply_discount()
    assert int(item1_2[0].price) == 440000
    assert int(item1_2[1].price) == 5500


def test_names(item1_2):

    assert item1_2[0].name == "Декстоп"
    assert item1_2[1].name == "Клавиатура"


def test_string_to_number():
    assert Item.string_to_number("42") == 42
    assert Item.string_to_number("3.14") == 3
    assert Item.string_to_number("abc") is None


@pytest.fixture
def csv_data():
    # Чтение данных из csv-файла
    items = []
    with open("../src/items.csv", newline='', encoding="cp1251") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            price = float(row['price'])
            quantity = int(row['quantity'])
            items.append((name, price, quantity))
    return items


def test_instantiate_from_csv(csv_data):
    # Вызов метода instantiate_from_csv()
    Item.instantiate_from_csv()
    # Получение экземпляров класса Item
    items = Item.all
    # Проверка количества экземпляров класса Item
    assert len(items) == len(csv_data)

    # Проверка соответствия данных
    for item, (name, price, quantity) in zip(items, csv_data):
        assert item.name == name
        assert item.price == price
        assert item.quantity == quantity


def test_repr():
    item = Item("Test Item", 10.0, 5)
    assert repr(item) == "Item('Test Item', 10.0, 5)"


def test_str():
    item = Item("Test Item", 10.0, 5)
    assert str(item) == "Test Item"


def test_add_valid_types():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone X", 50_000, 13, 1)
    item1 = Item("Смартфон", 15000, 10)
    assert phone1 + phone2 == 18
    assert item1 + phone2 == 23


class ItemTest1(Item):

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []

        try:
            with open('./src/items.csv', newline='', encoding="cp1251") as csvfile:  # некорректный путь
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError('_Файл item.csv поврежден_')
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('_Отсутствует файл item.csv_')


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        ItemTest1.instantiate_from_csv()


class ItemTest2(Item):

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []

        try:
            with open('test_items.csv', newline='', encoding="cp1251") as csvfile:  # некорректный файл
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError('_Файл item.csv поврежден_')
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('_Отсутствует файл item.csv_')


def test_instantiate_from_csv_missing_column():
    with pytest.raises(InstantiateCSVError) as exc_info:
        ItemTest2.instantiate_from_csv()
    assert str(exc_info.value) == '_Файл item.csv поврежден_'
