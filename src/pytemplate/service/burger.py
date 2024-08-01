from abc import ABC, abstractmethod


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
