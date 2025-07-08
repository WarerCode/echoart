import json
from core.Export import split_basename_and_extension
from PIL import Image

def importJson(filename: str) -> Image.Image:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    width = data["width"]
    height = data["height"]
    pixel_data = data["data"]

    # Create a new image
    img = Image.new("RGB", (width, height))

    # Set each pixel
    for pixel in pixel_data:
        x, y = pixel["position"]
        r, g, b = pixel["rgb"]
        img.putpixel((x, y), (r, g, b))

    return img


def saveImage(img: Image.Image, filename: str) -> None:
    name, ext = split_basename_and_extension(filename)
    # If extension is not specified, set a default
    if not ext:
        ext = "png"

    # Save the image to the specified file and format
    img.save(filename, format=ext.upper())
