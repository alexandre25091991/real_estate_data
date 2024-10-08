from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/extract", methods=['POST'])
def extract():
    address = request.form['address']
    address_json = json.dumps({"address": address})
    print(address_json)
    return "Adresse traitée"

if __name__ == "__main__":
    app.run(debug=True)

