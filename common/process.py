import os
import cv2
import numpy

Btn_Confirm = 'confirm'
Btn_All_Retire = 'all_retire'
Btn_Attack_Again = 'attack_again'
Btn_Full_Quary = 'full_quary'
Btn_Run = "run"
Btn_GetObj = "get_obj"

Aims = [Btn_Confirm, Btn_All_Retire, Btn_Attack_Again, Btn_Full_Quary, Btn_GetObj, Btn_Run]

class TemplMgr:
    def __init__(self, dir: str):
        # template dir
        self.dir = dir

        # template map
        self.templs = dict()

        # init
        self.load_basic()

    def load_basic(self):
        subfix = '.png'

        for aim in Aims:
            filepath = '{0}/{1}{2}'.format(self.dir, aim, subfix)

            assert os.path.exists(filepath)

            self.templs[aim] = cv2.imread(filepath)

    def detect(self, mat):
        result = []

        for key, temp in self.templs.items():

            res = cv2.matchTemplate(mat, temp, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = numpy.where(res >= threshold)

            if len(loc[0]) <= 0:
                continue

            # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            result.append((key, (loc[1][0], loc[0][0])))

        return result


from PIL import ImageGrab
import win32gui, win32api, win32con

class WindowMgr:
    def __init__(self, window_name: str):
        assert len(window_name) > 0

        toplist, winlist = [], []
        def enum_cb(hwnd, results):
            winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

        win32gui.EnumWindows(enum_cb, toplist)

        win = [(hwnd, title) for hwnd, title in winlist if window_name.lower() in title.lower()]
        win = win[0]

        self.hwnd = win[0]

    def cap(self):
        # win32gui.SetForegroundWindow(self.hwnd)
        bbox = win32gui.GetWindowRect(self.hwnd)
        img = ImageGrab.grab(bbox)

        return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

    def click(self, x, y):
        lParam = win32api.MAKELONG(x, y)

        hWnd1 = win32gui.FindWindowEx(self.hwnd, None, None, None)
        win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)

def GetWindows():
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_cb, toplist)

    return winlist