from flask import Flask, request, make_response, render_template

import fasttext
import os

app = Flask(__name__)
model = fasttext.load_model('src/models/fasttext.ftz')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/hello-world")
def hello_world():
    return "Hello, World!"

@app.route("/list")
def list():
    directories = os.listdir()
    return ','.join(directories)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        request_dict = request.form if request.form else request.get_json()
        prediction = model.predict(request_dict["message"])
        res = {"predicted": prediction[0][0], "probability": prediction[1][0]}
        return make_response(res, 200)
    except Exception as e:
        return make_response(str(e), 500)

if __name__ == "__main__":
    app.run()
