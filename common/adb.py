import subprocess

import cv2
import numpy
from ppadb.client import Client as AdbClient
from ppadb.device import Device

class AdbMgr:
    def __init__(self, adb_path: str):
        assert len(adb_path) > 0

        # device
        self.device = None

        # start adb
        self.adb_path = adb_path

        if self.start() == 0:
            # new adb client
            self.client = AdbClient(host="127.0.0.1", port=5037)
            # init device
            self.devices()

    def start(self):

        return subprocess.check_call([self.adb_path, "start-server"])

    def devices(self):
        assert self.client

        devices = self.client.devices()

        if len(devices) > 0:
            self.device = devices[0]

        return devices

    def cap(self):
        if not isinstance(self.device, Device):
            return None

        dev_img = self.device.screencap()
        cv2_img = cv2.imdecode(numpy.frombuffer(dev_img, numpy.uint8), cv2.IMREAD_COLOR)

        # test img show
        # cv2.imshow('image', cv2_img)
        # cv2.waitKey(0)

        # with open("screen.png", "wb") as fp:
        #     fp.write(dev_img)

        return cv2_img #cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)

    def click(self, x, y):
        if not isinstance(self.device, Device):
            return None

        self.device.input_tap(x, y)
