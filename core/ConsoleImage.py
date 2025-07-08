from PIL import Image
import math
from rich.console import Console
from core.Effects import Effects
from functools import partial

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
                "shift": 0,
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
        k = math.ceil(width/self.max_width)

        text_image = []

        effects_chain = []
        if effects.get("negative"):
            effects_chain.append(Effects.negative)
        if effects.get("gray"):
            effects_chain.append(Effects.gray)
        shift_val = effects.get("shift", 0)
        if shift_val:
            effects_chain.append(partial(Effects.shift, shift=shift_val))

        pixels_data = img.load()
        for y in range(0, height, k):
            row = []
            for x in range(0, width, k):
                pixel = pixels_data[x, y]
                for effect in effects_chain:
                    pixel = effect(pixel)
                r, g, b = pixel
                brightness = Effects.brightness(pixel)
                symbol = self.gradient[math.floor((n-1)*brightness)]
                if brightness > 0.75:
                    insert_text = f"bold rgb({r},{g},{b})"
                else:
                    insert_text = f"rgb({r},{g},{b})"
                row.append(f"[{insert_text}]{self.syblos_per_pixel*symbol}[/{insert_text}]")
            text_image.append(row)

        for i in range(len(text_image)):
            text_image[i] = "".join(text_image[i])

        print_str = "\n".join(text_image)
        console.print(print_str)
