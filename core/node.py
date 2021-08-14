import time
import cv2
import numpy

class Node:
    def __init__(self, config: dict):
        """
        init node from dict
        :param config: json/node to dict
        """
        # property
        self.id = config['id']
        self.rects = config['rects']
        self.img = config['img']
        self.event = config['event']

        # temp mat
        self.temp_mat = None if len(self.img) <= 0 else config['temp_mat']

        # features
        self.features = []

        # prepare
        self.extract()

    def extract(self):
        """
        extract template features from src image
        :return: None
        """
        img_mat = cv2.imread(self.img) if len(self.img) > 0 else self.temp_mat

        for rect in self.rects:
            assert len(rect) == 4

            x1, y1, x2, y2 = rect[0], rect[1], rect[3], rect[4]

            image_roi = img_mat[y1:y2, x1:x2]

            self.features.append(image_roi)

    def events(self):
        return self.event

    def detect(self, aim_mat):
        """
        detect features from aim image
        :param aim_mat: image be detected
        :return: bool, whether detected features
        """
        cnt = 0

        for f in self.features:

            res = cv2.matchTemplate(aim_mat, f, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = numpy.where(res >= threshold)

            if len(loc[0]) <= 0:
                continue

            # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            cnt += 1

        return cnt == len(self.features)

    def save(self):
        """
        save the node to dict
        :return: dict contains basic info
        """
        return {
            'id': self.id,
            'rects': self.rects,
            'img': self.img,
            'event': self.event
        }

def NewNode(img, rects, event):
    """
    new node by mat
    :param img: mat data
    :param rects: feature rect
    :param event: click
    :return:
    """
    config = {
        'id': str(int(time.time())),
        'rects': rects,
        'temp_mat': img,
        'img': '',
        'event': event
    }

    return Node(config)