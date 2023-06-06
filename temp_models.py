class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return {
            "username": self.username,
            "password": self.password
        }

class Product:
    def __init__(self, id, nombre, precio_unitario):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    def __repr__(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio_unitario": self.precio_unitario
        }

class ShoppingCart:
    def __init__(self, user : User):
        self.user = user
        self.products = dict()

    def add_product(self, product : Product):
        if product.nombre in self.products:
            self.products[product.nombre] += 1
        else:
            self.products[product.nombre] = 1
    
    def remove_product(self, product : Product):
        if product.nombre in self.products:
            self.products[product.nombre] -= 1
            if self.products[product.nombre] == 0:
                del self.products[product.nombre]
    
    def __repr__(self):
        return {
            "user": self.user,
            "products": self.products
        }
