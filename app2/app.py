from flask import Flask

from db import save_item, RandomDatabaseModel

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    save_item(RandomDatabaseModel(random_text="test"))
    return "Hello", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
