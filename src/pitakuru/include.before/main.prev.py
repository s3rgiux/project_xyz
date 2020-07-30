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


class AVGMain(object):
    def __init__(self, C=config()):
        self.C = C
        self.setup()
        self.movement = AntiGravityMovement()
        self.thread_executor = None

    '''起動時のセンサー関連初期動作テスト
    '''
    def setup(self):
        print("setup instances")
        self.tracker = ArucoTracker()
        self.lidar = Lidar()
        self.sound = None
        self.beep = None
        self.twd = TWDController()

        # lidar result in result (stack)
        self.current_obstacle = None
        self.current_target = None
        self.current_gravity = None

        # デバッグ用
        self.target = None
        self.gravity = None

        # aruco lost count
        self.lost = 0

        if self.C['pitakuru']['show_graph']:
            self.graph = PolarGraph()

        print("setup lidar")
        self.setup_lidar()
    
        print("setup controllers")
        # 1. ステートマシンを初期化
        self.model = states.model
        # 2. ボタンにステートマシンを関連付け
        self.switch = SwitchInput()
        #self.switch.add_button_event_cb('idle', lambda _: self.model.remote_idle_button_on())
        #self.switch.add_button_event_cb('karugamo', lambda _: self.model.karugamo_button_on())
        self.switch.add_button_event_cb('karugamo', lambda _: self.model.remote_idle_button_on())
        self.switch.add_button_event_cb('brake', lambda _: self.model.collision())
        self.switch.add_button_event_cb('release', lambda _: self.model.break_release_button_on())

        # 3. コントローラにステートマシンを関連付け

        self.controller = JoyStickController()
        self.controller.add_button_event_cb('circle', lambda _: self.model.remote_karuamo_button_on()) # とりあえずcircle
        self.controller.add_button_event_cb('triangle', lambda _: self.model.remote_manual_button_on()) # とりあえずtriangle
        self.controller.add_button_event_cb('square', lambda _: self.model.remote_idle_button_on()) # とりあえずsquare

        self.model.emergency_button_off()

        print("setup done!")

    def reload(self):
        self.lidar = Lidar(self.C)

    def release(self, log_data):
        if self.C['pitakuru']['capture']:
            with open('{}.pickle'.format(datetime.datetime.now().isoformat()), 'wb+') as f:
                pickle.dump(log_data, f)
                print("save done!")
        self.thread_executor.shutdown(wait=False)
        self.lidar.release()

    def is_danger(self, offsets):
        neighbor = self.movement.check_danger_neighbor(offsets)
        danger = neighbor is not None #and neighbor[1] < self.C['rplidar']['danger_obstacle']
        print(danger)
        return danger

    def update_state(self, offsets):
        if self.beep and self.beep.done:
            self.beep = None

        # if offsets is close to robot then update state warning
        if offsets is not None and self.is_danger(offsets):
            if self.current_state != states.STATE_ERROR_OBSTACLE:
                self.twd.send_rpm(0, 0)
            self.model.detect_obstacle()
            #if self.model.state == states.STATE_ACTIVE_KARUGAMO and not self.beep:
            #    self.beep = SoundPlayer('warning_3s')
            #    self.beep.play_once()
        self.controller.next_iter()
        self.switch.next_iter()

    def manual_mode_loop(self):
        self.controller.next_iter()
        dpad = self.controller.get_dpad()
        self.twd.dpad_to_rpm(*dpad)

    def obstacle_mode_loop(self):
        self.controller.next_iter()
        dpad = self.controller.get_dpad()
        self.twd.dpad_to_rpm(0, *dpad[1:])

    def collision_mode_loop(self):
        self.twd.send_rpm(0, 0)

    def karugamo_mode_loop(self):
        target = self.current_target
        if target is not None:
            self.lost = 0
            theta = target[0]
            dist = target[1]
            print("theta: {}, dist: {}".format(theta, dist))
            self.twd.follow(dist, theta)
        else:
            self.lost += 1
            if self.lost > self.C['pitakuru']['max_lost']:
                print("lost")
                self.twd.send_rpm(0, 0)

    def setup_lidar(self):
        offsets = None
        should_reload = True

        while True:
            try:
                # データ取得
                offsets = self.lidar.next_iter()
                if offsets is not None:
                    break
            except (RPLidarException, IOError) as e:
                # lidarへの接続エラー。リトライする
                print("waiting lidar...")
                print(traceback.format_exc())
                time.sleep(self.C['pitakuru']['reload_wait'])

    def lidar_loop(self):
        while True:
            try:
                offsets = self.lidar.next_iter()
                self.current_obstacle = offsets
            except (RPLidarException, IOError) as e:
                print("reload lidar...")
                print(traceback.format_exc())
                time.sleep(self.C['pitakuru']['reload_wait'])

    def tracker_loop(self):
        while True:
            try:
                target = self.tracker.next_iter()
                self.current_target = target
                if target is not None:
                    offsets = self.current_obstacle
                    gravity = self.movement.anti_gravity(target, offsets)
                    # 描画用のデバッグモード
                    if self.C['pitakuru']['show_graph']:
                        self.graph.update(offsets, target=target, power=gravity)                        
                    self.current_target = gravity
                # デバッグ用
                if target is not None:
                    self.target = target
                    self.gravity = gravity
                else:
                    self.target = None
                    self.gravity = None
            except Exception as e:
                print(traceback.format_exc())

    def run(self):
        self.current_state = None
        self.thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        self.thread_executor.submit(self.lidar_loop)
        self.thread_executor.submit(self.tracker_loop)

        log_data = []

        while True:
            try:
                offsets = self.current_obstacle

                # スイッチの取得と状態の更新 (スイッチの取得時にイベントハンドラで自動的に状態が更新される)
                self.update_state(offsets)

                current_state = self.model.state
                if self.current_state != current_state:
                    print(current_state)
                    self.current_state = current_state
                    self.switch.set_LED_color(current_state)
                    
                    # play sound when karugamo mode
                    if current_state == states.STATE_ACTIVE_KARUGAMO:
                        self.sound = SoundPlayer("active_3s")
                        self.sound.play_forever()
                    else:
                        if self.sound:
                            self.sound.stop()
                            self.sound = None

                # info::ステートマシンの状態に応じて、処理を変更する
                # current_state = self.model.state

                if current_state == states.STATE_ACTIVE_KARUGAMO:
                    # スレッドなので、再生のたびに初期化する必要がある
                    self.karugamo_mode_loop()

                elif current_state == states.STATE_ACTIVE_MANUAL:
                    # コントローラから値を取って処理する
                    self.manual_mode_loop()
                
                elif current_state == states.STATE_ERROR_OBSTACLE:
                    self.obstacle_mode_loop()

                elif current_state == states.STATE_ERROR_COLLISION:
                    self.collision_mode_loop()

                if self.C['pitakuru']['capture']:
                    # 極座標グラフ表示用のログデータを作成する
                    d = {}
                    offsets = self.current_obstacle
                    d['offsets'] = offsets
                    d['power'] = self.gravity
                    d['target'] = self.target
                    d['danger_flg'] = self.is_danger(offsets) if offsets is not None else False
                    log_data.append(d)

            except KeyboardInterrupt:
                # Ctrl-Cによる正常終了
                self.release(log_data)
                break
            except Exception:
                # プロセスが正常に終了した際にもリリースする
                traceback.print_exc()
                self.release(log_data)
                break


if __name__ == '__main__':
    agv = AVGMain()
    agv.run()
