from dataclasses import dataclass


@dataclass
class Burger:
    bread: str
    patty: str
    sauce: str | None = None
    toppings: list[str] | None = None

    def __str__(self):
        sauce_str = self.sauce if self.sauce else "no sauce"
        toppings_str = ", ".join(self.toppings) if self.toppings else "no toppings"
        return f"Burger with {self.bread}, {self.patty}, {sauce_str}, {toppings_str}."
