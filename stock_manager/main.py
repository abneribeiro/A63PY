class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                break

    def update_estock(self, name, quantity):
        for product in self.products:
            if product.name == name:
                product.quantity += quantity
                break

    def generate_report(self):
        total_sold = 0
        for product in self.products:
            sold = product.quantity
            total_sold += sold
            print(f"{product.name}: {sold} unit sold")
        print(f"Total Sold: {total_sold}")


Store = store()
product1 = product("Camiseta", 29.90, 50)
product2 = product("Calça Jeans", 99.90, 20)
Store.add_product(product1)
Store.add_product(product2)
#Store.update_estock("Camiseta", -10)
#Store.remove_product("Calça Jeans")
Store.generate_report()


#Adicionar entrada de valores (input)
#Já ter um conjunto de valores em stock e fazer a verificação se não existem produtos exibir uma mensagem, caso contrário fazer a vendar e subtrair no stock
#Usar dicionarios com as suas chaves ao invés de listas
# Fazer um loop que mostra sempre os produtos disponiveis para o usúario depois de cada venda