from abc import ABC, abstractmethod

from src.pytemplate.domain.models import Burger, burger_factory


class BurgerBuilder(ABC):
    @abstractmethod
    def bread(self, bread: str):
        raise NotImplementedError("The bread method must be overridden.")

    @abstractmethod
    def patty(self, patty: str):
        raise NotImplementedError("The patty method must be overridden.")

    @abstractmethod
    def sauce(self, sauce: str):
        raise NotImplementedError("The sauce method must be overridden.")

    @abstractmethod
    def toppings(self, toppings: list[str]):
        raise NotImplementedError("The toppings method must be overridden.")

    @abstractmethod
    def build(self):
        raise NotImplementedError("The build method must be overridden.")


class CheeseBurgerBuilder(BurgerBuilder):
    def __init__(self):
        self._bread = None
        self._patty = None
        self._sauce = None
        self._toppings = None

    def bread(self, bread: str):
        self._bread = bread
        return self

    def patty(self, patty: str):
        self._patty = patty
        return self

    def sauce(self, sauce: str):
        self._sauce = sauce
        return self

    def toppings(self, toppings: list[str]):
        self._toppings = toppings
        return self

    def build(self) -> Burger:
        data = {"bread": self._bread, "patty": self._patty, "sauce": self._sauce, "toppings": self._toppings}
        return burger_factory(data)
