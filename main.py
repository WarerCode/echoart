from core.ConsoleImage import ConsoleImage
from core.Config import Config
from core.Export import exportJson
from core.Import import importJson, saveImage


def main():
    try:
        import sys
        sys.argv = ["main.py","--input", "assets/image.jpg", "--output", "image.json"]
        config = Config()

        filename = config.getInputFilename()
        target = config.getTargetFilename()
        if config.isJsonInput():
            img = importJson(filename)
        else:
            img = ConsoleImage(filename)

        effects = config.getEffectsArgs()
        img.display(effects)

        if target != None:
            if not config.isJsonInput():
                exportJson(target, filename, effects)
            else:
                saveImage(img, target)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()