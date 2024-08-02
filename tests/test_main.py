from unittest.mock import patch

import pytest

from src.pytemplate.entrypoints.cli.main import main


@pytest.mark.parametrize(
    "choice, expected_result",
    [
        ("cheese", "Burger with Sesame Seed Bun, Beef Patty, Ketchup, no toppings."),
        ("vegan", "Burger with Whole Wheat Bun, Black Bean Patty, Vegan Mayo, Lettuce, Tomato."),
        ("chicken", "Burger with Brioche Bun, Chicken Patty, Mayo, Pickles."),
        ("invalid", "Invalid choice!"),
    ],
)
def test_main(choice, expected_result):
    with patch("builtins.input", return_value=choice):
        result = main()
        assert result == expected_result
