import ctypes

import cv2
import numpy
import win32gui, win32api, win32con, win32ui

from io import BytesIO
from PIL import ImageGrab


class Window:
    def __init__(self, window_name: str, use_pyauto: bool = False):
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

        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                hwnds[win32gui.GetClassName(hwnd)] = hwnd
            return True

        self.child_hwnds = {}
        win32gui.EnumChildWindows(self.hwnd, callback, self.child_hwnds)

        self.use_pyauto = use_pyauto

    def cap_pil(self):
        '''
        capture image from window
        :return: pil image
        '''
        bytes = BytesIO()

        # win32gui.SetForegroundWindow(self.hwnd)
        bbox = win32gui.GetWindowRect(self.hwnd)
        img = ImageGrab.grab(bbox)

        img.save(bytes, "PNG")
        bytes.seek(0)

        return bytes

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

    def inner_click(self, hwnd, abs_x, abs_y):
        bbox = win32gui.GetWindowRect(hwnd)

        if not InBBox(bbox, abs_x, abs_y):
            return

        param = win32api.MAKELONG(abs_x - bbox[0], abs_y - bbox[1])

        pywin = win32ui.CreateWindowFromHandle(hwnd)

        pywin.SendMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, param)
        pywin.SendMessage(win32con.WM_LBUTTONUP, 0, param)

    def click(self, x, y):
        bbox = win32gui.GetWindowRect(self.hwnd)

        abs_x = bbox[0] + x
        abs_y = bbox[1] + y

        # for some application like mumu andriod simulation,
        # you need run in admin
        if self.use_pyauto:
            win32api.SetCursorPos([abs_x, abs_y])
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            return

        self.inner_click(self.hwnd, abs_x, abs_y)

        for val in self.child_hwnds.values():
            self.inner_click(val, abs_x, abs_y)

def InBBox(bbox, x, y):
    assert len(bbox) == 4

    if x <= bbox[0] or x >= bbox[2]:
        return False

    if y <= bbox[1] or y >= bbox[3]:
        return False

    return True


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
