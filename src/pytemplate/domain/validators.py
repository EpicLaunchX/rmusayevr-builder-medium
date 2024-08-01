import marshmallow


class BurgerSchema(marshmallow.Schema):
    bread = marshmallow.fields.Str(required=True)
    patty = marshmallow.fields.Str(required=True)
    sauce = marshmallow.fields.Str(required=False)
    toppings = marshmallow.fields.List(marshmallow.fields.Str(), required=False)

    @marshmallow.validates("bread")
    def validate_bread(self, value):
        if not value:
            raise marshmallow.ValidationError("Bread is required.")

    @marshmallow.validates("patty")
    def validate_patty(self, value):
        if not value:
            raise marshmallow.ValidationError("Patty is required.")
