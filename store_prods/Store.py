class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def display_products(self):
        counter = 0
        for i in self.products:
            counter += 1
            print(f"{counter}:\nID: {i.id}\nName: {i.name}\nPrice: {i.price}\nCategory: {i.category}\n")
        return self

    def add_product(self, new_prod):
        self.products.append(new_prod)
        return self

    def sell_product(self, id):
        for i in self.products:
            if i.id == id:
                self.products.remove(i)
                print(f"The object with id '{id}' has been deleted\n")
        return self

    def inflation(self, percent_increase):
        for i in self.products:
            amount = i.price * percent_increase
            i.price += amount
        return self

    def set_clearance(self, category, percent_discount):
        for i in self.products:
            if i.category == category:
                i.increase_price(percent_discount, False)
        return self
