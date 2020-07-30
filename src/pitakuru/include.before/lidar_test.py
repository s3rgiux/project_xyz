import datetime
import pickle
import math
import time
import sys, traceback
import concurrent.futures
import numpy as np
from serial.serialutil import SerialException
from rplidar import RPLidarException

from lidar import Lidar
from camera import ArucoTracker
from config import config
from controllers import JoyStickController
from graph import PolarGraph
from motor import TWDController
from movement import AntiGravityMovement
import states
from sounds import SoundPlayer
from switches import SwitchInput
from utils import checkpoint, print_time

def is_danger(movement, offsets):
	neighbor = movement.check_danger_neighbor(offsets)
	danger = neighbor is not None #and neighbor[1] < self.C['rplidar']['danger_obstacle']
	return danger

def main():
	C = config()
	lidar = Lidar()
	switch = SwitchInput()

	offsets = None
	should_reload = True

	while True:
		try:
			# データ取得
			offsets = lidar.next_iter()
			if offsets is not None:
				break
		except (RPLidarException, IOError) as e:
			# lidarへの接続エラー。リトライする
			print("waiting lidar...")
			print(traceback.format_exc())
			time.sleep(C['pitakuru']['reload_wait'])

	while True:
		try:
			offsets = lidar.next_iter()
			movement = AntiGravityMovement()
			danger = is_danger(movement, offsets)
			if danger:
				switch.set_LED_color("ERROR_OBSTACLE")
			else:
				switch.set_LED_color("IDLE")
			print(danger)
		except (RPLidarException, IOError) as e:
                	print("reload lidar...")
                	print(traceback.format_exc())
                	time.sleep(C['pitakuru']['reload_wait'])


main()
