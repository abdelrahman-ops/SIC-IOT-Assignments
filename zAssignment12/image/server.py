from flask import Flask, request
from PIL import Image
from firebase import fetch_image, write_img

app = Flask(__name__)


@app.route("/img/<id>", methods=['GET'])
def get_image(id):
    img = fetch_image(id)
    return {"image": img}


@app.route("/img", methods=['POST'])
def post_image():
    image_data = request.json["image"]
    image_id = request.json["id"]
    write_img(image_data, image_id)
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
