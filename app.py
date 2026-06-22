from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data["text"]
    lang = data["language"]

    result = GoogleTranslator(source='auto', target=lang).translate(text)

    return jsonify({"translation": result})

if __name__ == "__main__":
    app.run(debug=True)