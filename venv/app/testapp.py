# Adapted from - http://flask.pocoo.org/
import flask as fl

app = fl.Flask(__name__)

@app.route("/")
def root():
    return "Hello World!"

if __name__ == "__main__":
    app.run()