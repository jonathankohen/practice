import Product as other_products


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def display_product_names(self):
        counter = 0
        for i in self.products:
            counter += 1
            print(f"{counter}: {i.name}")
        return self

    def add_product(self, new_prod):
        self.products.append(new_prod)
        return self

    def sell_product(self, index):
        print(f"The '{self.products[index].name}' object has been deleted\n")
        del self.products[index]
        return self

    def display(self):
        print(f"Name: {self.name}\n")
        return self


kmart = Store("kmart")
kmart.add_product(other_products.cup).add_product(other_products.pencil).display_product_names()
kmart.sell_product(0).display_product_names()

# sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
# inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
# set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)