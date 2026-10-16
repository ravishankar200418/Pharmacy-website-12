
from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {
        "id": 1,
        "name": "Digital Thermometer",
        "category": "Health Devices",
        "price": 150,
        "description": "Digital temperature checking device",
        "icon": "🌡️"
    },
    {
        "id": 2,
        "name": "First Aid Kit",
        "category": "Healthcare",
        "price": 299,
        "description": "Basic first aid supplies",
        "icon": "🩹"
    },
    {
        "id": 3,
        "name": "Hand Sanitizer",
        "category": "Personal Care",
        "price": 99,
        "description": "Hand hygiene product",
        "icon": "🧴"
    },
    {
        "id": 4,
        "name": "Vitamin C Tablets",
        "category": "Supplements",
        "price": 180,
        "description": "Vitamin supplement",
        "icon": "🍊"
    },
    {
        "id": 5,
        "name": "Face Mask Pack",
        "category": "Personal Care",
        "price": 120,
        "description": "Protective face masks",
        "icon": "😷"
    },
    {
        "id": 6,
        "name": "Digital Weighing Scale",
        "category": "Health Devices",
        "price": 650,
        "description": "Personal weight measurement",
        "icon": "⚖️"
    }
]


@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)


@app.route("/health")
def health():
    return {"status": "ok", "application": "Ravi Pharmacy"}


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080, debug=False)