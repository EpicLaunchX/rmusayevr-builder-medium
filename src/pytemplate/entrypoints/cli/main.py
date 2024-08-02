from src.pytemplate.service.burger import CheeseBurgerBuilder, ChickenBurgerBuilder, VeggieBurgerBuilder


def main():
    choice = input("What type of burger would you like? (Cheese, Vegan, Chicken)").strip().lower()

    if choice == "cheese":
        builder = CheeseBurgerBuilder()
        burger = builder.bread("Sesame Seed Bun").patty("Beef Patty").sauce("Ketchup").toppings([]).build()
    elif choice == "vegan":
        builder = VeggieBurgerBuilder()
        burger = builder.bread("Whole Wheat Bun").patty("Black Bean Patty").sauce("Vegan Mayo").toppings(["Lettuce", "Tomato"]).build()
    elif choice == "chicken":
        builder = ChickenBurgerBuilder()
        burger = builder.bread("Brioche Bun").patty("Chicken Patty").sauce("Mayo").toppings(["Pickles"]).build()
    else:
        return "Invalid choice!"

    return str(burger)
