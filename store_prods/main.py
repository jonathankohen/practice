from Store import *
from Product import *

cup = Product("Cup", 2.0, "Kitchen")
pencil = Product("Pencil", 0.5, "School")

kmart = Store("kmart")
kmart.add_product(cup).add_product(pencil).display_products()
kmart.sell_product(cup.id).display_products()
kmart.inflation(0.25).display_products()
kmart.set_clearance("School", 0.25).display_products()