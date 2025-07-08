from core.ConsoleImage import ConsoleImage
from core.Config import Config
import core.Export
from core.Export import exportJson


def main():
    try:
        import sys
        sys.argv = ["main.py","--input", "assets/image.jpg", "--output", "image.json"]
        config = Config()
        filename = config.getInputFilename()
        effects = config.getEffectsArgs()

        img = ConsoleImage(filename)
        img.display(effects)

        target = config.getTargetFilename()
        if target != None:
            exportJson(target, filename, effects)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()