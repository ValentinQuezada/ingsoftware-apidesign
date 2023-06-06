class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"'{self.username}', '{self.password}'"

class Product:
    def __init__(self, id, nombre, precio_unitario):
        self.id = id
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
    

products = [
    Product(1, "Sprite", 1.5),
    Product(2, "Fanta", 1.0),
    Product(3, "Coca Cola", 1.5),
    Product(4, "Pepsi", 2.0),
    Product(5, "7up", 1.5),
]

users = [
    User("paolov", "1234"),
    User("paolov2", "1234")
]

carts = [
    ShoppingCart(users[0]),
    ShoppingCart(users[1])
]