import requests
from urllib.parse import urljoin
from utility import encode_img, decode_image 

server_url = "http://localhost:5000"


def fetch_image(image_id):
    response = requests.get(f"{server_url}/img/{image_id}")
    if response.status_code == 200:
        return response.json()["image"]
    else:
        return None


def post_image(image_data, image_id):
    data = {"image": image_data, "id": image_id}
    response = requests.post(f"{server_url}/img", json=data)
    if response.text == "OK":
        print("Added Successfully!")
    return response.text


if __name__ == "__main__":
    image_path = "logo.jpeg"
    image_id = "LOGO"
    image_data = encode_img(image_path)
    response = post_image(image_data, image_id)
    print(response)
