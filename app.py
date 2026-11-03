from flask import Flask, jsonify, render_template
import csv
from pathlib import Path

app = Flask(__name__)

# Get the path to characters.csv
CSV_FILE = Path(__file__).with_name("characters.csv")


# Load characters once when the application starts
def load_characters():
    with open(CSV_FILE, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Store characters in memory
CHARACTERS = load_characters()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "healthy"})


@app.route("/characters")
def get_characters():
    return jsonify(CHARACTERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
