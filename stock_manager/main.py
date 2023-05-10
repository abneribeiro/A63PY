class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
        else:
            print(f"{name} is not available in the store.")

    def update_stock(self, name, quantity):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            print(f"{name} is not available in the store.")

    def generate_report(self):
        total_sold = 0
        for name, product in self.products.items():
            sold = product.quantity
            total_sold += sold
            print(f"{name}: {sold} unit(s) sold")
        print(f"Total Sold: {total_sold}")

    def display_products(self):
        print("Available products:")
        for name, product in self.products.items():
            print(f"{name}: {product.quantity} unit(s) in stock")


store = Store()

# add some products to the store
product1 = Product("T-shirt", 29.90, 50)
product2 = Product("Jeans", 99.90, 20)
product3 = Product("Sneakers", 79.90, 30)
product4 = Product("Hoodie", 49.90, 40)
product5 = Product("Backpack", 39.90, 25)

store.add_product(product1)
store.add_product(product2)
store.add_product(product1)
store.add_product(product2)
store.add_product(product1)
store.add_product(product2)
while True:
    store.display_products()
    name = input("Enter product name (or q to quit): ")
    if name == 'q':
        break
    elif name not in store.products:
        print(f"{name} is not available in the store.")
    else:
        quantity = int(input("Enter quantity to sell: "))
        if quantity > store.products[name].quantity:
            print(
                f"Only {store.products[name].quantity} unit(s) of {name} is available.")
        else:
            store.products[name].quantity -= quantity
            print(f"{quantity} unit(s) of {name} sold.")

store.generate_report()
