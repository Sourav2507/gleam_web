from flask import Blueprint,render_template

auth = Blueprint("auth",__name__)

@auth.route("/")
def auth_home():
    return render_template("auth/auth.html")