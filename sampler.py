from flask import Flask,render_template,request
from  models import Product
from  peewee import OperationalError
app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def index():
    products = Product.select()
    if request.method=="POST":
        name = request.form["name"]
        quantity = request.form["quantity"]
        price = request.form["price"]
        Product.create(name=name,quantity=quantity,price=price)
    return render_template("index.html",products=products)


if __name__ == '__main__':
    try:
       Product.create_table()
    except OperationalError:
       pass
    app.run()
