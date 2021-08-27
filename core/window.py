import cv2
import numpy
import win32gui, win32api, win32con

from PIL import ImageGrab


class Window:
    def __init__(self, window_name: str):
        '''
        window of the aim application
        :param window_name: name of window
        '''
        assert len(window_name) > 0

        toplist, winlist = [], []

        def enum_cb(hwnd, results):
            winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

        win32gui.EnumWindows(enum_cb, toplist)

        win = [(hwnd, title) for hwnd, title in winlist if window_name.lower() in title.lower()]
        win = win[0]

        self.hwnd = win[0]

    def cap_pil(self):
        '''
        capture image from window
        :return: pil image
        '''
        # win32gui.SetForegroundWindow(self.hwnd)
        bbox = win32gui.GetWindowRect(self.hwnd)
        img = ImageGrab.grab(bbox)

        return img

    def cap(self):
        '''
        capture image from window
        :return: cv mat
        '''
        # win32gui.SetForegroundWindow(self.hwnd)
        bbox = win32gui.GetWindowRect(self.hwnd)
        img = ImageGrab.grab(bbox)

        return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

    def size(self):
        bbox = win32gui.GetWindowRect(self.hwnd)
        return bbox

    def click(self, x, y):
        lParam = win32api.MAKELONG(x, y)

        hWnd1 = win32gui.FindWindowEx(self.hwnd, None, None, None)
        win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)


def WinList():
    '''
    get names of all windows
    :return: list of names
    '''
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        text = win32gui.GetWindowText(hwnd)

        if len(text) <= 0:
            return

        winlist.append(text)

    win32gui.EnumWindows(enum_cb, toplist)

    return winlist
