from functools import partial
from core.Effects import Effects
class ConsoleItem:
    gradient = " .:!/r(l1Z4H9W8$@"
    syblos_per_pixel = 2
    max_width = 60

    def __init__(self, path: str):
        self.path = path

    @staticmethod
    def effects_chain(
            cls,
            effects: dict={
                "negative": False, 
                "shift": 0,
                "gray": False,
            }
        ):
        effects_chain = []
        if effects.get("negative"):
            effects_chain.append(Effects.negative)
        if effects.get("gray"):
            effects_chain.append(Effects.gray)
        shift_val = effects.get("shift", 0)
        if shift_val:
            effects_chain.append(partial(Effects.shift, shift=shift_val))
        return effects_chain