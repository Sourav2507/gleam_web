from flask import Blueprint

customer = Blueprint("customer",__name__)

@customer.route("/")
def customer_home():
    return "Hello from Customer"