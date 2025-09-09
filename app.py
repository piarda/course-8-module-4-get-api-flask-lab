from flask import Flask, jsonify, request, abort
from data import products

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"})

# GET /products, returns all products or filtered by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [p for p in products if p.get("category") == category]
        return jsonify(filtered)
    return jsonify(products)

# GET /products/<id>, returns product by ID or 404 if not found
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p.get("id") == id), None)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product)

if __name__ == "__main__":
    app.run(debug=True)
