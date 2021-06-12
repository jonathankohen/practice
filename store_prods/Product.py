import uuid


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = uuid.uuid4()

    def increase_price(self, percentage, is_increasing):
        amount = self.price * percentage
        if is_increasing:
            self.price += amount
        else:
            self.price -= amount
        return self

    def display(self):
        print(f"ID: {self.id}\nName: {self.name},\nPrice: {self.price}\nCategory: {self.category}")
        return self
