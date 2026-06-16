from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    products = [
        {"name": "Laptop", "price": 800},
        {"name": "Phone", "price": 500},
        {"name": "Headphones", "price": 100}
    ]
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
