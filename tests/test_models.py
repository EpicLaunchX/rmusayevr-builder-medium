from src.pytemplate.domain.models import Burger


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
