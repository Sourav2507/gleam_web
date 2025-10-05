from flask import Blueprint

admin = Blueprint("admin",__name__)

@admin.route("/")
def admin_home():
    return "Hello from Admin"