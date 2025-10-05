from flask import Blueprint

seller = Blueprint("seller",__name__)

@seller.route("/")
def seller_home():
    return "Hello from Seller"