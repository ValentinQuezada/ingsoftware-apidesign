from flask import Flask, request, jsonify, abort, redirect
import datetime
from flask_cors import CORS
import json
import requests
from models import *

active_user = None

def create_app():
    app = Flask(__name__)
    CORS(app, origin="*")

    @app.route("/api/v1/user_signup", methods=["POST"])
    def signup():
        try:
            body = request.get_json()

            correo =  body.get("correo", None)
            password = body.get("password", None)

            if correo is None or password is None:
                abort(422)

            user = User(correo, password)

            user.append(user)

            return jsonify({
                "success": True,
                "correo": correo,
                "password": password
            })
        except:
            abort(500)

    @app.route("/api/v1/login", methods=["GET"])
    def login():

        body = request.get_json()

        correo = body.get_json()
        password = body.get_json()

        if correo is None or password is None:
            abort(422)

        user = User(correo,password)

        if user not in users:
            abort(404)



        return jsonify({
            "success": True
        })






    @app.route("/api/v1/products", methods=["GET"])
    def get_products():
        if products is None:
            abort(404)

        return jsonify({
            "success": True,
            "productos": products
        })

    @app.route("/api/v1/products/<product_id>", methods=["GET"])
    def get_product_by_id(product_id):

        for p in products:
            if(p.id == product_id):
                product = p

        if product is None:
            abort(404)

        return jsonify({
            "success": True,
            "producto": product.format(),
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
            carts[active_user].add_product(product)

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
            carts[active_user].remove_product(product)
            return redirect("/api/v1/shoppingcart")
        except Exception as e:
            abort(500)

    @app.route("/api/v1/shoppingcart", methods=["GET"])
    def ver_carrito():
        return jsonify({
            "success": True,
            "carrito": carts[active_user]
        })
        

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
