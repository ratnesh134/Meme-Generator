
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Testing Flask on Sunday"



if __name__ == '__main__':

    app.run(debug=True)
