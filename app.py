from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>i am biswajit</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
