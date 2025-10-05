from flask import Flask,Blueprint,redirect,url_for
from routes import admin,customer,seller,auth,general,deadend


app = Flask(__name__)

app.register_blueprint(admin.admin,url_prefix='/admin')
app.register_blueprint(customer.customer,url_prefix='/customer')
app.register_blueprint(seller.seller,url_prefix='/seller')
app.register_blueprint(auth.auth,url_prefix='/auth')
app.register_blueprint(general.general,url_prefix='/general')
app.register_blueprint(deadend.deadend,url_prefix='/deadend')

@app.route('/')
def home():
    return redirect(url_for('general.general_home'))

if __name__ == '__main__':
    app.run(debug=True,port=5000)
