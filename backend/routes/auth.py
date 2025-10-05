from flask import Blueprint

auth = Blueprint("auth",__name__)

@auth.route("/")
def auth_home():
    return "Hello from Auth"