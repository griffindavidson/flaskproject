from application import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    productsData = [{"id": 1, "name": "Product 1", "description": "Description 1", "price": 100},
                    {"id": 2, "name": "Product 2", "description": "Description 2", "price": 200},
                    {"id": 3, "name": "Product 3", "description": "Description 3", "price": 300},
                    {"id": 4, "name": "Product 4", "description": "Description 4", "price": 400},
                    {"id": 5, "name": "Product 5", "description": "Description 5", "price": 500},
                    {"id": 6, "name": "Product 6", "description": "Description 6", "price": 600},
                    {"id": 7, "name": "Product 7", "description": "Description 7", "price": 700},
                    {"id": 8, "name": "Product 8", "description": "Description 8", "price": 800},
                    {"id": 9, "name": "Product 9", "description": "Description 9", "price": 900},
                    {"id": 10, "name": "Product 10", "description": "Description 10", "price": 1000}
    ]
    return render_template("products.html", productsData=productsData)

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/suppliers")
def suppliers():
    return render_template("suppliers.html")

@app.route("/inventories")
def inventories():
    return render_template("inventories.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/sales_items")
def sales_items():
    return render_template("sales_items.html")

@app.route("/customers")
def customers():
    return render_template("customers.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")













