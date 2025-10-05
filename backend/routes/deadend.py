#For Debugging of routes.... Might be removed in the future.....

from flask import Blueprint

deadend = Blueprint("deadend",__name__)

@deadend.route("/")
def deadend_home():
    return "Hello from deadend"
