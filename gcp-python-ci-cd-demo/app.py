from flask import Flask, request
from shipping import calculate_shipping_category

app = Flask(__name__)

@app.route("/")
def home():
    return "GCP Python CI/CD Demo is running"

@app.route("/shipping")
def shipping():
    weight = float(request.args.get("weight", "0"))
    return calculate_shipping_category(weight)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)