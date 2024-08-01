import marshmallow
import pytest

from src.pytemplate.domain.validators import BurgerSchema


def test_burger_schema_valid_data():
    data = {"bread": "Wheat", "patty": "Beef", "sauce": "Ketchup", "toppings": ["Lettuce", "Tomato"]}
    try:
        BurgerSchema().load(data)
    except marshmallow.ValidationError:
        pytest.fail("ValidationError raised unexpectedly!")


def test_burger_schema_invalid_bread():
    data = {"bread": "", "patty": "Beef", "sauce": "Ketchup", "toppings": ["Lettuce", "Tomato"]}
    with pytest.raises(marshmallow.ValidationError) as excinfo:
        BurgerSchema().load(data)
    assert "Bread is required." in str(excinfo.value)


def test_burger_schema_invalid_patty():
    data = {"bread": "Whole Wheat", "patty": "", "sauce": "Ketchup", "toppings": ["Lettuce"]}
    with pytest.raises(marshmallow.ValidationError) as excinfo:
        BurgerSchema().load(data)
    assert "Patty is required." in str(excinfo.value)


def test_burger_schema_optional_fields():
    data = {"bread": "Whole Wheat", "patty": "Beef"}
    try:
        BurgerSchema().load(data)
    except marshmallow.ValidationError:
        pytest.fail("ValidationError raised unexpectedly!")
