'''
'''

import time

from config import config
from motor import TWDController
import time

from pyproacmd import commands as cmd
from pyproacmd.pyproacmd import Utils
from camera import ArucoTracker


tracker = ArucoTracker()
twd = TWDController()
lost = 0
while True:
    target = tracker.next_iter()
    if target is not None:
        lost = 0
        theta = target[0]
        dist = target[1]
        print("theta: {}, dist: {}".format(theta, dist))
        twd.follow(dist, theta)
    else:
        lost += 1
        if lost > 5:
            twd.send_rpm(0, 0)

