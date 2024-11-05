# order-service/application.py
from flask import Flask
from flask import jsonify
from routes.orders import order_bp

app = Flask(__name__)

# Registering the orders blueprint
app.register_blueprint(order_bp, url_prefix='/orders')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Order Service!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
