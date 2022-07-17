from flask import Flask
from src.main import solve

app = Flask(__name__)



@app.route('/check/<img_label_encoded>/<img_encoded>')
def hello_world(img_label_encoded, img_encoded):  # put application's code here
    return str(solve(img_label_encoded, img_encoded))


if __name__ == '__main__':
    app.run()
