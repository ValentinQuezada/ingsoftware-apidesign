from flask import Flask, request, jsonify, abort, redirect
from flask_cors import CORS
from temp_models import *

def create_app():
    app = Flask(__name__)
    CORS(app, origin="*")
    active_user = None
    users = [
        User("admin", "admin")
    ] 
    carts = {
        users[0]: ShoppingCart(users[0])
    }
    products = [
        Product(0, "Sprite", 1.5),
        Product(1, "Fanta", 1.0),
        Product(2, "Coca Cola", 1.75),
        Product(3, "Pepsi", 2.0),
        Product(4, "7up", 1.5),
    ]


    @app.route("/api/v1/user_signup", methods=["POST"])
    def signup():
        try:
            body = request.get_json()

            correo = body.get("correo", None)
            password = body.get("password", None)

            if correo is None or password is None:
                abort(422)

            user = User(correo, password)

            if user in users:
                abort(400)

            users.append(user)

            return jsonify({
                "success": True,
                "correo": correo,
                "password": password
            })
        except:
            abort(500)

    @app.route("/api/v1/login", methods=["GET"])
    def login():
        try:
            body = request.get_json()

            correo = body.get_json("correo", None)
            password = body.get_json("password", None)

            if correo is None or password is None:
                abort(422)

            user = User(correo, password)

            if user not in users:
                abort(404)

            active_user = user

            return jsonify({
                "success": True
            })
        except:
            abort(500)

    @app.route("/api/v1/user_get", methods=["GET"])
    def get_user():
        try:
            body = request.get_json()

            correo = body.get_json("correo", None)

            if correo is None:
                abort(422)

            user = None

            for u in users:
                if correo == u.username:
                    user = User(correo, u.password)

            if user is None:
                abort(404)

            return jsonify({
                "sucess": True,
                "correo": user.username,
                "password": user.password
            })
        except:
            abort(500)

   
    @app.route("/api/v1/products", methods=["GET"])
    def get_products():
        if products is None:
            abort(404)

        p = []
        for product in products:
            p.append(product.__repr__())

        return jsonify({
            "success": True,
            "productos": p
        })

    @app.route("/api/v1/products/<int:product_id>", methods=["GET"])
    def get_product_by_id(product_id):
        product = None

        for p in products:
            if p.id == product_id:
                product = p

        if product is None:
            abort(404)

        return jsonify({
            "success": True,
            "id": product.id,
            "nombre": product.nombre,
            "precio_unitario": product.precio_unitario
        })

    @app.route("/api/v1/shoppingcart/<int:id>", methods=["POST"])
    def agregar_producto(id):
        try:
            body = request.get_json()
            id = body.get("product_id", None) 

            if id is None:
                abort(422)

            product = products[int(id)]
            cart = carts[active_user]
            cart.add_product(product)

            return redirect("/api/v1/shoppingcart")
        
        except Exception as e:
            abort(500)
        
    @app.route("/api/v1/shoppingcart/<int:id>", methods=["DELETE"])
    def eliminar_producto(id):
        try:
            body = request.get_json()
            id = body.get("product_id", None) 

            if id is None:
                abort(422)
            
            product = products[int(id)]
            cart = carts[active_user]
            cart.remove_product(product)
            return redirect("/api/v1/shoppingcart")
        except Exception as e:
            abort(500)

    @app.route("/api/v1/shoppingcart", methods=["GET"])
    def ver_carrito():
        return jsonify({
            "success": True,
            "carrito": carts[active_user]
        })

    @app.route("/api/v1/shoppingcart/buy", methods=["GET"])
    def comprar():
        carts[active_user] = dict()
        return redirect("/api/v1/shoppingcart")
        

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'statusCode': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'statusCode': 500,
            'message': 'Internal Server error'
        }), 500

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'statusCode': 422,
            'message': 'Unprocessable'
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "statusCode": 400,
            "message": "bad request"
        }), 400


    @app.route("/")
    def main():
        return "Api para compras"

    return app
