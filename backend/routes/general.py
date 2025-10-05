from flask import Blueprint

general = Blueprint("general",__name__)

@general.route("/")
def general_home():
    return "Hello from General"
