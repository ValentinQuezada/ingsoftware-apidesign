from flask import Flask, request, jsonify, abort
import datetime
from flask_cors import CORS
import json
import requests
from models import User, Product, ShoppingCart, products, users

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

    

    @app.route("/api/v1/products", methods=["GET"])

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
