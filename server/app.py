from flask import Flask, make_response, jsonify


app = Flask(__name__)



if __name__ == '__main__':
    app.run(port=5555)