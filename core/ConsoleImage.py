import numpy as np
from PIL import Image
import math
from rich.console import Console
from core.Effects import Effects

class ConsoleImage:
    gradient = " .:!/r(l1Z4H9W8$@"
    syblos_per_pixel = 2
    max_width = 60

    def __init__(self, path: str="assets/image.jpg"):
        self.path = path


    def display(
            self, 
            effects: dict={
                "negative": False, 
                "shift": False,
                "gray": False,
            }
        ):
        console = Console()

        # Открываем изображение
        img = Image.open(self.path)
        
        n = len(self.gradient)

        # Преобразуем в RGB (если это не RGB уже)
        img = img.convert("RGB")

        # Получаем ширину и высоту
        width, height = img.size
        k = width/self.max_width

        text_image = []

        for y in range(0, height, math.ceil(k)):
            row = []
            for x in range(0, width, math.ceil(k)):
                pixel = img.getpixel((x, y))
                if effects.get("negative"):
                    pixel = Effects.negative(pixel)
                if effects.get("gray"):
                    pixel = Effects.gray(pixel)
                r, g, b = pixel
                brightness = Effects.brightness(pixel)
                symbol = self.gradient[math.floor((n-1)*brightness)]
                if brightness > 0.75:
                    row.append(f"[bold rgb({r},{g},{b})]{symbol}[/]")
                else:
                    row.append(f"[rgb({r},{g},{b})]{symbol}[/]")
            text_image.append(row)

        text_image = np.array(text_image)
        text_image = np.char.multiply(text_image, 2)
        length = text_image.size
        text_image[:, -1] += "\n"
        text_image = text_image.reshape(length)
        print_str = "".join(text_image)
        console.print(print_str)