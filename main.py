from common import *
import time
import cv2

if __name__ == '__main__':
    # init window mgr
    # features include capture image and send click event
    win = WindowMgr('BlueStacks')
    # init template mgr
    # templates are used to detect the click area
    temps = TemplMgr('./img/AzurLane')

    while True:
        # detect every 1 sec
        time.sleep(1)
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
