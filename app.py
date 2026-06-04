from flask import Flask, render_template, request, jsonify
from sentiment import predict_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    result = predict_sentiment(data["text"])

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)