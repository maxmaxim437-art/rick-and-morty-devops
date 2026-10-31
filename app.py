from flask import Flask
import csv

app = Flask(__name__)


@app.route("/healthcheck")
def healthcheck():
    return {"status": "healthy"}


@app.route("/characters")
def get_characters():
    with open("characters.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        characters = list(reader)

    return characters


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
