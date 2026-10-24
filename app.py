
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary product data for LACHI
products = [
    {
        "id": 1,
        "name": "The Evening Muse",
        "category": "Fashion",
        "price": 2499
    },
    {
        "id": 2,
        "name": "Golden Aura Hoops",
        "category": "Jewellery",
        "price": 699
    },
    {
        "id": 3,
        "name": "Rose Glow Cream",
        "category": "Beauty",
        "price": 549
    },
    {
        "id": 4,
        "name": "The Heritage Bag",
        "category": "Accessories",
        "price": 1899
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the LACHI backend!",
        "status": "running"
    })


@app.route("/api/products")
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
