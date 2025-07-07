import argparse

EFF_NEGATIVE = "negative"
EFF_GRAY = "gray"
EFF_SHIFT = "shift"

CALLBACKS = {
    EFF_NEGATIVE,
    EFF_GRAY,
    EFF_SHIFT
}

class Config:
    def __init__(self):
        self.parser = self.getParser()

        # parsing args -> argparse.Namespace
        # noexcept(false) vvv
        self.args = self.parser.parse_args()


    def getArgs(self) -> argparse.Namespace:
        return self.args


    def getEffectsArgs(self) -> dict:
        return {
            EFF_SHIFT : self.args.shift,
            EFF_NEGATIVE : self.args.negative,
            EFF_GRAY : self.args.gray
        }


    def getInputFilename(self) -> str:
        return self.args.input


    """ vvv noexcept(false) vvv """
    @staticmethod
    def getParser() -> argparse.ArgumentParser:
        # initialize parser environment
        parser = argparse.ArgumentParser(
            add_help=True,      # add '--help' arg
            prog="echoart",     # program name
            description="console graphics CRUD util")
        parser.add_argument("-I", "-input", type=str, required=True,
                                 help="input filename")
        parser.add_argument("-o", "--output", type=str,
                                 help="target filename")
        parser.add_argument("-n", "--negative", action="store_true",
                                 help="set a negative effect flag in true")
        parser.add_argument("-sh", "--shift", type=int,
                                 help="set a brightness shift effect value")
        parser.add_argument("-g", "--gray", action="store_true",
                                 help="set a only gray effect flag in true")

        return parser


    # returns names of effects to use (e.g. "shift", ...)
    def getEffectCallbacks(self) -> list[str]:
        callbacks_names = []
        effects = self.getEffectsArgs()

        for callback in CALLBACKS:
            if effects[callback] != None:
                callbacks_names.append(callback)

        return callbacks_names