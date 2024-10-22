from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,World!</p>"


@app.route("/products")
def products():
    response = jsonify([

        {
           "title": "Caneca personalizada de Porcelana do backend",
            "amount": 456.45,
            "Installments":{"Number":3,"total":41.15}
        },
        {
            "title": "Caneca de Tulipa",
            "amount": 789.45,
            "Installments":{"Number":6,"total":41.15,"hasFee": True}
        }
    ])
    response.headers.add('Access-Control-Allow-Origin','*')

    return response