from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Quick Travel Spot Finder API!"})

if __name__ == '__main__':
    app.run(debug=True)

