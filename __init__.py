from flask import Flask, request, jsonify, abort
import datetime
from flask_cors import CORS
import json
import requests
from models import User, Product, ShoppingCart, products, users, carts

active_user = None


def create_app():
    app = Flask(__name__)
    CORS(app, origin="*")

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
    @app.route("/api/v1/product/<int:id>", methods=["GET"])
    def agregar_producto(id):
        body = request.get_json()
        id = body.get("id", None)

        if id is None:
            abort(422)

        product = products[id]
        carts[active_user].add_product(product)

    @app.route("/api/v1/shoppingcart", methods=["GET"])
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
