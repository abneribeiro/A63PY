# Store Inventory Management System

This is a Python project that implements a store inventory management system. It allows the user to add and remove products, update the stock quantity, and generate a sales report. The program uses object-oriented programming concepts and a dictionary to store the product information.

## Technologies Used

The project was developed using Python 3. It does not use any external libraries or frameworks.

## How to Use

To use the program, simply run the `main.py` file in a Python environment. The program will display the available products and ask the user for the product name and quantity to sell. If the requested product is not available or the requested quantity is more than the available stock, an appropriate message is displayed. Otherwise, the quantity is subtracted from the stock and a success message is displayed. Finally, the program generates a sales report that shows the quantity of each product sold and the total amount sold.

## Program Structure

The program consists of two classes: `Product` and `Store`. The `Product` class represents a single product and has three attributes: name, price, and quantity. The `Store` class represents the store inventory and has four methods: `add_product`, `remove_product`, `update_stock`, and `generate_report`. The `add_product` method adds a new product to the inventory, the `remove_product` method removes a product from the inventory, the `update_stock` method updates the stock quantity of a product, and the `generate_report` method generates a sales report.

The program uses a dictionary to store the product information, with the keys being the product names and the values being instances of the `Product` class. The `display_products` method is used to display the available products to the user.

The main program uses a while loop that repeatedly displays the available products and asks the user for the product name and quantity to sell. If the requested product is not available or the requested quantity is more than the available stock, an appropriate message is displayed. Otherwise, the quantity is subtracted from the stock and a success message is displayed. Finally, the `generate_report` method is called to show the updated sales report.

```python
def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

```

```python
class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product
```


## Future Improvements

Possible future improvements for this program include adding a graphical user interface (GUI), implementing data persistence using a database, and adding support for multiple store locations.


