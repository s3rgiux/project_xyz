'''
リモコンテスト用

別ターミナルで $sudo ds4drv
で、ペアリング待機モードが開始するので、ps4のoption+PSボタン長押ししてペアリング

デバイスファイルは　/dev/input/js1
'''

import time

from config import config
from controllers import JoyStickController
from motor import TWDController
import time

from proacmd import commands as cmd
from proacmd.pyproacmd import Utils


twd = TWDController()
ctrl = JoyStickController()
while True:
    ctrl.next_iter()
    left = ctrl.getButton("dpad_left")
    right = ctrl.getButton("dpad_right")
    up = ctrl.getButton("dpad_up")
    down = ctrl.getButton("dpad_down")
    print("left, right, up, down = ", left, right, up, down)
    twd.dpad_to_rpm(up, left, down, right)
    # twd.ctrlv_to_rpm(-hat["x"], hat["y"])
    # twd.pc_left.send_receive(cmd.RunAtVel(twd.id_L, Utils.RPMtoRADpS(1000)))
    # time.sleep(0.1)

