from flask import Flask
import constant as con
# from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host=con.HOST, debug=con.DEBUG)             # For development
    # serve(app, port=con.PORT, threads=con.THREADS)    # For deploy
