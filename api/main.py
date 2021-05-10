import io
import csv
import json
from flask import Flask
from flask import request, redirect
from flask import jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/file_upload", methods=["POST"])
@cross_origin(supports_credentials=True)
def upload():
    result = dict()
    if request.method == "POST":
        print("here")
        my_data = request.json
        result["success"] = "post request success"

        with open("data.json", "w") as fo:
            print("JSON FILE CREATED")
            json.dump(my_data, fo)

    return jsonify(result)


@app.route("/get_file", methods=["GET"])
def get_file():
    try:
        with open("data.json", "r") as rf:
            data = json.load(rf)
            return jsonify(data)
    except Exception as e:
        res = []
        return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)