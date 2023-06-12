import pytest
from src.keyboard import KeyBoard, Mixin


def test_keyboard():
    """Pytest класс KeyBoard"""
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert kb.name == "Dark Project KD87A"
    kb.name = "New Keyboard"
    assert kb.name == "New Keyboard"


def test_mixin():
    """Pytest класса Mixin"""
    mixin = Mixin()
    assert str(mixin) == "EN"
    assert mixin.language == "EN"

    mixin.change_lang()
    assert str(mixin) == "RU"
    assert mixin.language == "RU"

    mixin.change_lang().change_lang()
    assert str(mixin) == "RU"
    assert mixin.language == "RU"
