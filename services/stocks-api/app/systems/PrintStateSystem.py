from app.systems.System import System


class PrintStateSystem(System):
    def __init__(self, state_printer):
        self.state_printer = state_printer

    def handle(self, entities):
        self.state_printer.print()