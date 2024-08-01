import pytest

from src.pytemplate.service.burger import BurgerBuilder


def test_bread_not_implemented():

    class ConcreteBurgerBuilder(BurgerBuilder):
        def bread(self, bread: str):
            return super().bread(bread)

        def patty(self, patty: str):
            pass

        def sauce(self, sauce: str):
            pass

        def toppings(self, toppings: list[str]):
            pass

        def build(self):
            pass

    builder = ConcreteBurgerBuilder()

    with pytest.raises(NotImplementedError):
        builder.bread(bread="Whole Wheat")


def test_patty_not_implemented():

    class ConcreteBurgerBuilder(BurgerBuilder):
        def bread(self, bread: str):
            pass

        def patty(self, patty: str):
            return super().patty(patty)

        def sauce(self, sauce: str):
            pass

        def toppings(self, toppings: list[str]):
            pass

        def build(self):
            pass

    builder = ConcreteBurgerBuilder()

    with pytest.raises(NotImplementedError):
        builder.patty(patty="Beef")


def test_sauce_not_implemented():

    class ConcreteBurgerBuilder(BurgerBuilder):
        def bread(self, bread: str):
            pass

        def patty(self, patty: str):
            pass

        def sauce(self, sauce: str):
            return super().sauce(sauce)

        def toppings(self, toppings: list[str]):
            pass

        def build(self):
            pass

    builder = ConcreteBurgerBuilder()

    with pytest.raises(NotImplementedError):
        builder.sauce(sauce="Ketchup")


def test_toppings_not_implemented():

    class ConcreteBurgerBuilder(BurgerBuilder):
        def bread(self, bread: str):
            pass

        def patty(self, patty: str):
            pass

        def sauce(self, sauce: str):
            pass

        def toppings(self, toppings: list[str]):
            return super().toppings(toppings)

        def build(self):
            pass

    builder = ConcreteBurgerBuilder()

    with pytest.raises(NotImplementedError):
        builder.toppings(toppings=["Lettuce", "Tomato"])


def test_build_not_implemented():

    class ConcreteBurgerBuilder(BurgerBuilder):
        def bread(self, bread: str):
            pass

        def patty(self, patty: str):
            pass

        def sauce(self, sauce: str):
            pass

        def toppings(self, toppings: list[str]):
            pass

        def build(self):
            return super().build()

    builder = ConcreteBurgerBuilder()

    with pytest.raises(NotImplementedError):
        builder.build()
