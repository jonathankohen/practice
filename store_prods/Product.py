class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def increase_price(self, percentage, is_increasing):
        amount = self.price * percentage
        if is_increasing:
            self.price += amount
        else:
            self.price -= amount
        return self

    def display(self):
        print(f"Name: {self.name},\nPrice: {self.price}\nCategory: {self.category}")
        return self


cup = Product("Cup", 2.0, "Kitchen")
pencil = Product("Pencil", 0.5, "School")