class Soda:
    def __init__(self, ingridient=None):
        self.ingridient = ingridient

    def show_my_drink(self):
        if self.ingridient:
            if isinstance(self.ingridient, str):
                print(f"Газировка и {self.ingridient}")
            else:
                print("Добавка введена неверно")
        else:
            print("Обычная газировка")

    def __call__(self):
        self.show_my_drink()

    def __str__(self):
        if self.ingridient:
            if isinstance(self.ingridient, str):
                return f"Газировка и {self.ingridient}"
            else:
                return "Добавка введена неверно"
        else:
            return "Обычная газировка"

    def __repr__(self):
        return f"Soda(additive = {repr(self.ingridient)})"


drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)

print(str(drink1))
print(str(drink2))
print(str(drink3))

print(repr(drink1))
print(repr(drink2))
print(repr(drink3))