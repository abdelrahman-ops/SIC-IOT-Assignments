from PIL import Image
from io import BytesIO
import base64


def decode_image(image_data: str):
    # Decode the base64 image data
    new_bytes = base64.b64decode(image_data)

    # Read the bytes back into an image
    new_photo = Image.open(BytesIO(new_bytes))

    # Display the image
    new_photo.show()


def encode_img(path: str) -> str:
    image = Image.open(path)

    stream = BytesIO()
    image.save(stream, format='JPEG')
    photo_bytes = stream.getvalue()

    image_string = base64.b64encode(photo_bytes).decode('utf-8')

    return image_string
