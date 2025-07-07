from core.ConsoleImage import ConsoleImage
from core.Config import Config

def main():
    config = Config()
    filename = config.getInputFilename()
    effects = config.getEffectsArgs()

    img = ConsoleImage(filename)
    img.display(effects)

if __name__ == "__main__":
    main()