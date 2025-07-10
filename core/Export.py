import json
from pathlib import Path
from PIL import Image

def split_basename_and_extension(path: str) -> (str, str):
    pathObj = Path(path)
    basename = pathObj.stem
    ext = pathObj.suffix.lstrip('.')    #split and removes '.'
    return basename, ext

def exportJson(target: str, filename: str, effects: dict) -> None: #noexcept(false)
    name, format = split_basename_and_extension(filename)

    data = {"name": name, "format": format, "effects": effects}
    img = Image.open(filename).convert("RGB")   # opening RGB image
    width, height = img.size    # get size
    data["width"] = width       # store
    data["height"] = height

    pixels = []
    pixels_data = img.load()
    for y in range(0, height):
        for x in range(0, width):
            r, g, b = pixels_data[x,y]
            pixels.append({"rgb": [r,g,b]})
    data["data"] = pixels

    with open(target, "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
