from .window import Window, WinList


class Controller:
    def __init__(self):
        """
        top controller
        """
        self.win = None
        self.pil = None

    def win_list(self):
        return WinList()

    def win_init(self, name: str, use_pyauto: bool):
        self.win = Window(name, use_pyauto)

    def win_cap(self):
        assert isinstance(self.win, Window)
        self.pil = self.win.cap_pil()

        return self.pil

    def win_size(self):
        assert isinstance(self.win, Window)
        return self.win.size()

    def win_ok(self):
        return self.win is not None

    def win_click(self, x, y):
        assert isinstance(self.win, Window)
        self.win.click(x, y)

gcore = Controller()
