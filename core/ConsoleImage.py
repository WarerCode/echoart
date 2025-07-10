from PIL import Image
import math
from rich.console import Console
from core.Effects import Effects
from core.BaseClass import ConsoleItem

class ConsoleImage(ConsoleItem):

    def __init__(self, path: str="assets/image.jpg"):
        super().__init__(path)
        self.img = Image.open(self.path).convert("RGB")

    def display(
            self, 
            effects: dict={
                "negative": False, 
                "shift": 0,
                "gray": False,
            }
        ):
        console = Console()
        
        n = len(self.gradient)

        # Получаем ширину и высоту
        width, height = self.img.size
        k = math.ceil(width/self.max_width)

        effects_chain = self.effects_chain(effects)

        text_image = []

        pixels_data = self.img.load()
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
                row.append(f"[{insert_text}]{self.syblos_per_pixel*symbol}[/]")
            text_image.append(row)

        for i in range(len(text_image)):
            text_image[i] = "".join(text_image[i])

        print_str = "\n".join(text_image)
        console.print(print_str)
