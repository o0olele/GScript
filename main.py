from common import *
import cv2

if __name__ == '__main__':
    win = WindowMgr('BlueStacks')
    temps = TemplMgr('./img')

    while True:
        time.sleep(1)

        img = win.cap()

        res = temps.detect(img)

        if len(res) > 0:
            print(res)

        for item in res:
            if item[0] == Btn_Attack_Again:
                win.click(item[1][0] + 10, item[1][1] + 10)
