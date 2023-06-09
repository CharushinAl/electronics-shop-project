import pytest
from src.phone import Phone


def test_phone_repr():
    phone = Phone("iPhone X", 50000, 13, 1)
    assert repr(phone) == "Phone('iPhone', 50000, 13, 1)"


def test_phone_str():
    phone = Phone('Samsung Galaxy', 20000, 3, 1)
    assert str(phone) == "Samsung Galaxy"


def test_phone_add():
    phone1 = Phone("iPhone X", 50000, 13, 3)
    phone2 = Phone('Samsung Galaxy', 20000, 3, 1)
    assert phone1 + phone2 == 16


def test_phone_valid_number_of_sim():
    phone = Phone("iPhone X", 50000, 13, 1)
    assert phone.valid_number_of_sim(3) == 3


def test_phone_invalid_number_of_sim():
    phone = Phone("iPhone X", 50000, 13, 1)
    with pytest.raises(ValueError):
        phone.valid_number_of_sim(0)


def test_phone_invalid_add():
    phone = Phone('iPhone', 999.99, 5, 2)
    with pytest.raises(TypeError):
        phone + 'string'
