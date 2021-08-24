from .window import Window, WinList


class Controller:
    def __init__(self):
        """
        top controller
        """
        self.win = None

    def win_list(self):
        return WinList()

    def win_init(self, name: str):
        self.win = Window(name)

gcore = Controller()
