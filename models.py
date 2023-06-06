class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"'{self.username}', '{self.password}'"

class Product:
    def __init__(self, nombre, precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    def __repr__(self):
        return f"'{self.nombre}', {self.precio_unitario}"

class ShoppingCart:
    def __init__(self, user : User):
        self.user = user
        self.products = dict()

    def add_product(self, product : Product):
        if product.nombre in self.products:
            self.products[product.nombre] += 1
        else:
            self.products[product.nombre] = 1
    
    def __repr__(self):
        return f"'{self.user}', {self.products}"