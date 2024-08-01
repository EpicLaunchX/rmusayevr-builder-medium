import marshmallow
import pytest

from src.pytemplate.domain.models import Burger, burger_factory


def test_burger_creation_required_fields():
    burger = Burger(bread="Whole Wheat", patty="Beef")
    assert burger.bread == "Whole Wheat"
    assert burger.patty == "Beef"
    assert burger.sauce == None
    assert burger.toppings == None


def test_burger_creation_all_fields():
    burger = Burger(bread="Whole Wheat", patty="Beef", sauce="Ketchup", toppings=["Lettuce", "Tomato"])
    assert burger.bread == "Whole Wheat"
    assert burger.patty == "Beef"
    assert burger.sauce == "Ketchup"
    assert burger.toppings == ["Lettuce", "Tomato"]


def test_burger_str_no_sauce_no_toppings():
    burger = Burger(bread="Whole Wheat", patty="Beef")
    expected_str = "Burger with Whole Wheat, Beef, no sauce, no toppings."
    assert str(burger) == expected_str


def test_burger_str_with_sauce_no_toppings():
    burger = Burger(bread="Whole Wheat", patty="Beef", sauce="Ketchup")
    expected_str = "Burger with Whole Wheat, Beef, Ketchup, no toppings."
    assert str(burger) == expected_str


def test_burger_str_no_sauce_with_toppings():
    burger = Burger(bread="Whole Wheat", patty="Beef", toppings=["Lettuce", "Tomato"])
    expected_str = "Burger with Whole Wheat, Beef, no sauce, Lettuce, Tomato."
    assert str(burger) == expected_str


def test_burger_str_with_sauce_with_toppings():
    burger = Burger(bread="Whole Wheat", patty="Beef", sauce="Ketchup", toppings=["Lettuce", "Tomato"])
    expected_str = "Burger with Whole Wheat, Beef, Ketchup, Lettuce, Tomato."
    assert str(burger) == expected_str


def test_burger_factory_valid_data():
    data = {"bread": "Whole Wheat", "patty": "Beef", "sauce": "Ketchup", "toppings": ["Lettuce", "Tomato"]}
    burger = burger_factory(data)
    assert isinstance(burger, Burger)
    assert burger.bread == "Whole Wheat"
    assert burger.patty == "Beef"
    assert burger.sauce == "Ketchup"
    assert burger.toppings == ["Lettuce", "Tomato"]


def test_burger_factory_missing_bread():
    data = {"bread": "", "patty": "Beef", "sauce": "Ketchup", "toppings": ["Lettuce", "Tomato"]}
    with pytest.raises(marshmallow.ValidationError) as excinfo:
        burger_factory(data)
    assert "Bread is required." in str(excinfo.value)


def test_burger_factory_missing_patty():
    data = {"bread": "Whole Wheat", "patty": "", "sauce": "Ketchup", "toppings": ["Lettuce", "Tomato"]}
    with pytest.raises(marshmallow.ValidationError) as excinfo:
        burger_factory(data)
    assert "Patty is required." in str(excinfo.value)


def test_burger_factory_optional_fields():
    data = {"bread": "Whole Wheat", "patty": "Beef"}
    burger = burger_factory(data)
    assert isinstance(burger, Burger)
    assert burger.bread == "Whole Wheat"
    assert burger.patty == "Beef"
    assert burger.sauce is None
    assert burger.toppings is None
