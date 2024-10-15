class Icecream:
    def __init__(self, ingredient = None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def compostion(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')

iceream = Icecream()
iceream.compostion()
iceream = Icecream('шоколадом')
iceream.compostion()
iceream = Icecream(5)
iceream.compostion()