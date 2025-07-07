class Effects:

    @classmethod
    def brightness(cls, pixel: tuple=(0,0,0)):
        return sum(pixel)/(3*255)

    @classmethod
    def gray(cls, pixel: tuple=(0,0,0)):
        color = int(sum(pixel)/3)
        return tuple(color for _ in range(3))
    
    @classmethod
    def negative(cls, color: tuple=(0,0,0)):
        return (255 - color[0], 255 - color[1], 255 - color[2])
