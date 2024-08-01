from dataclasses import dataclass

import marshmallow

from src.pytemplate.domain.validators import BurgerSchema


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


def burger_factory(data):
    try:
        validated_data = BurgerSchema().load(data)
    except marshmallow.ValidationError as err:
        raise marshmallow.ValidationError(f"Invalid input data: {err.messages}") from err
    return Burger(**validated_data)
