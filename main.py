from common import *
import time
import cv2

def WinScript():
    # print(GetWindows())
    # init window mgr
    # features include capture image and send click event
    win = WindowMgr('雷电模拟器')
    # init template mgr
    # templates are used to detect the click area
    temps = TemplMgr('./img/AzurLane')

    while True:
        # detect every 1 sec
        time.sleep(0.5)
        # cap image
        img = win.cap()
        # detect the aim
        res = temps.detect(img)
        # if have aims
        if len(res) > 0:
            print(res)
        # click scheduler
        for item in res:
            if item[0] == Btn_Attack_Again:
                # click
                win.click(item[1][0] + 10, item[1][1] + 10)
            elif item[0] == Btn_All_Retire:
                win.click(item[1][0] + 10, item[1][1] + 10)
                time.sleep(0.7)
                win.click(item[1][0] + 400, item[1][1] + 10)
            elif item[0] == Btn_Run:
                win.click(item[1][0] + 70, item[1][1] - 150)
            else:
                win.click(item[1][0] + 10, item[1][1] + 10)

def AdbScript():
    adbMgr = AdbMgr('D:\\leidian\\LDPlayer9\\adb.exe')

    temps = TemplMgr('./img/AzurLane')

    while True:
        # detect every 1 sec
        time.sleep(0.5)
        # cap image
        img = adbMgr.cap()
        # detect the aim
        res = temps.detect(img)
        # if have aims
        if len(res) > 0:
            print(res)
        # click scheduler
        for item in res:
            if item[0] == Btn_Attack_Again:
                # click
                adbMgr.click(item[1][0] + 10, item[1][1] + 10)
            elif item[0] == Btn_All_Retire:
                adbMgr.click(item[1][0] + 10, item[1][1] + 10)
                time.sleep(0.7)
                adbMgr.click(item[1][0] + 400, item[1][1] + 10)
            elif item[0] == Btn_Run:
                adbMgr.click(item[1][0] + 70, item[1][1] - 150)
            else:
                adbMgr.click(item[1][0] + 10, item[1][1] + 10)

if __name__ == '__main__':
    AdbScript()