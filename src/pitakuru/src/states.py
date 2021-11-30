#!/usr/bin/env python
# coding: utf-8

from transitions import Machine

import rospy
from pitakuru.msg import State, TriggerAction


"""PitakuruState
"""
# シャットダウン（非通電）
STATE_SHUTDOWN = "SHUTDOWN"
# アイドル状態
STATE_IDLE = "IDLE"
# 動作アクティブ:カルガモ
STATE_ACTIVE_KARUGAMO = "ACTIVE_KARUGAMO"
# 動作アクティブ:マニュアル
STATE_ACTIVE_MANUAL = "ACTIVE_MANUAL"
# エラー:近傍に障害物あり
STATE_ERROR_OBSTACLE = "ERROR_OBSTACLE"
# エラー:ガードバンパー衝突検知
STATE_ERROR_COLLISION = "ERROR_COLLISION"

states = [
    STATE_SHUTDOWN,
    STATE_IDLE,
    STATE_ACTIVE_KARUGAMO,
    STATE_ACTIVE_MANUAL,
    STATE_ERROR_OBSTACLE,
    STATE_ERROR_COLLISION,
]

"""PitakuruTrigger
"""
# 非常停止ボタン解除
TRIGGER_EMERGENCY_BUTTON_OFF = "emergency_button_off"
# 非常停止ボタン押下
TRIGGER_EMERGENCY_BUTTON_ON = "emergency_button_on"
# カルガモボタン押下
TRIGGER_KARUGAMO_BUTTON_ON = "karugamo_button_on"
# リモコン:カルガモボタン押下
TRIGGER_REMOTE_KARUGAMO_BUTTON_ON = "remote_karuamo_button_on"
# リモコン:マニュアルボタン押下
TRIGGER_REMOTE_MANUAL_BUTTON_ON = "remote_manual_button_on"
# リモコン:アイドルボタン押下
TRIGGER_REMOTE_IDLE_BUTTON_ON = "remote_idle_button_on"
# アイドルボタン押下
TRIGGER_IDLE_BUTTON_ON = "idle_button_on"
# 進行方向 2000 mm 以内に障害物を発見
TRIGGER_DETECT_OBSTACLE = "detect_obstacle"
# 前方近傍に障害物を発見（LIDAR進行方向 500 mm以内）
TRIGGER_DETECT_DANGER_OBSTACLE = "detect_danger_obstacle"
# ガードバンパー接触
TRIGGER_COLLISION = "collision"
# ブレーキ解除ボタン押下
TRIGGER_BREAK_RELEASE_BUTTON_ON = "break_release_button_on"
# 対象ロストから10秒経過
TRIGGER_LONG_LOST = "long_lost"

transitions = [
    dict(trigger=TRIGGER_EMERGENCY_BUTTON_OFF, source=STATE_SHUTDOWN, dest=STATE_IDLE),
    dict(trigger=TRIGGER_EMERGENCY_BUTTON_ON, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_KARUGAMO_BUTTON_ON, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_REMOTE_KARUGAMO_BUTTON_ON, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_REMOTE_MANUAL_BUTTON_ON, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_REMOTE_IDLE_BUTTON_ON, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_IDLE_BUTTON_ON, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_BREAK_RELEASE_BUTTON_ON, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_DETECT_OBSTACLE, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_COLLISION, source=STATE_SHUTDOWN, dest=STATE_SHUTDOWN),

    dict(trigger=TRIGGER_EMERGENCY_BUTTON_ON, source=STATE_IDLE, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_EMERGENCY_BUTTON_OFF, source=STATE_IDLE, dest=STATE_IDLE),
    dict(trigger=TRIGGER_KARUGAMO_BUTTON_ON, source=STATE_IDLE, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_REMOTE_KARUGAMO_BUTTON_ON, source=STATE_IDLE, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_REMOTE_MANUAL_BUTTON_ON, source=STATE_IDLE, dest=STATE_ACTIVE_MANUAL),
    dict(trigger=TRIGGER_REMOTE_IDLE_BUTTON_ON, source=STATE_IDLE, dest=STATE_IDLE),
    dict(trigger=TRIGGER_IDLE_BUTTON_ON, source=STATE_IDLE, dest=STATE_IDLE),
    dict(trigger=TRIGGER_BREAK_RELEASE_BUTTON_ON, source=STATE_IDLE, dest=STATE_IDLE),
    dict(trigger=TRIGGER_DETECT_OBSTACLE, source=STATE_IDLE, dest=STATE_IDLE),
    dict(trigger=TRIGGER_COLLISION, source=STATE_IDLE, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_DETECT_DANGER_OBSTACLE, source=STATE_IDLE, dest=STATE_ERROR_OBSTACLE),

    dict(trigger=TRIGGER_EMERGENCY_BUTTON_ON, source=STATE_ACTIVE_KARUGAMO, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_KARUGAMO_BUTTON_ON, source=STATE_ACTIVE_KARUGAMO, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_REMOTE_KARUGAMO_BUTTON_ON, source=STATE_ACTIVE_KARUGAMO, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_BREAK_RELEASE_BUTTON_ON, source=STATE_ACTIVE_KARUGAMO, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_REMOTE_MANUAL_BUTTON_ON, source=STATE_ACTIVE_KARUGAMO, dest=STATE_ACTIVE_MANUAL),
    dict(trigger=TRIGGER_REMOTE_IDLE_BUTTON_ON, source=STATE_ACTIVE_KARUGAMO, dest=STATE_IDLE),
    dict(trigger=TRIGGER_IDLE_BUTTON_ON, source=STATE_ACTIVE_KARUGAMO, dest=STATE_IDLE),
    dict(trigger=TRIGGER_DETECT_OBSTACLE, source=STATE_ACTIVE_KARUGAMO, dest=STATE_ERROR_OBSTACLE),
    dict(trigger=TRIGGER_DETECT_DANGER_OBSTACLE, source=STATE_ACTIVE_KARUGAMO, dest=STATE_ERROR_OBSTACLE),
    dict(trigger=TRIGGER_COLLISION, source=STATE_ACTIVE_KARUGAMO, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_LONG_LOST, source=STATE_ACTIVE_KARUGAMO, dest=STATE_IDLE),

    dict(trigger=TRIGGER_EMERGENCY_BUTTON_ON, source=STATE_ACTIVE_MANUAL, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_KARUGAMO_BUTTON_ON, source=STATE_ACTIVE_MANUAL, dest=STATE_IDLE),
    dict(trigger=TRIGGER_REMOTE_KARUGAMO_BUTTON_ON, source=STATE_ACTIVE_MANUAL, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_REMOTE_MANUAL_BUTTON_ON, source=STATE_ACTIVE_MANUAL, dest=STATE_ACTIVE_MANUAL),
    dict(trigger=TRIGGER_REMOTE_IDLE_BUTTON_ON, source=STATE_ACTIVE_MANUAL, dest=STATE_IDLE),
    dict(trigger=TRIGGER_IDLE_BUTTON_ON, source=STATE_ACTIVE_MANUAL, dest=STATE_IDLE),
    dict(trigger=TRIGGER_DETECT_OBSTACLE, source=STATE_ACTIVE_MANUAL, dest=STATE_ERROR_OBSTACLE),
    dict(trigger=TRIGGER_COLLISION, source=STATE_ACTIVE_MANUAL, dest=STATE_ERROR_COLLISION),

    dict(trigger=TRIGGER_EMERGENCY_BUTTON_ON, source=STATE_ERROR_OBSTACLE, dest=STATE_ERROR_OBSTACLE),
    dict(trigger=TRIGGER_KARUGAMO_BUTTON_ON, source=STATE_ERROR_OBSTACLE, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_REMOTE_KARUGAMO_BUTTON_ON, source=STATE_ERROR_OBSTACLE, dest=STATE_ACTIVE_KARUGAMO),
    dict(trigger=TRIGGER_REMOTE_MANUAL_BUTTON_ON, source=STATE_ERROR_OBSTACLE, dest=STATE_ACTIVE_MANUAL),
    dict(trigger=TRIGGER_REMOTE_IDLE_BUTTON_ON, source=STATE_ERROR_OBSTACLE, dest=STATE_IDLE),
    dict(trigger=TRIGGER_IDLE_BUTTON_ON, source=STATE_ERROR_OBSTACLE, dest=STATE_ERROR_OBSTACLE),
    dict(trigger=TRIGGER_COLLISION, source=STATE_ERROR_OBSTACLE, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_DETECT_OBSTACLE, source=STATE_ERROR_OBSTACLE, dest=STATE_ERROR_OBSTACLE),
    dict(trigger=TRIGGER_COLLISION, source=STATE_ERROR_OBSTACLE, dest=STATE_ERROR_COLLISION),

    dict(trigger=TRIGGER_EMERGENCY_BUTTON_ON, source=STATE_ERROR_COLLISION, dest=STATE_SHUTDOWN),
    dict(trigger=TRIGGER_KARUGAMO_BUTTON_ON, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_REMOTE_KARUGAMO_BUTTON_ON, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_REMOTE_MANUAL_BUTTON_ON, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_REMOTE_IDLE_BUTTON_ON, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_IDLE_BUTTON_ON, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_COLLISION, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_DETECT_OBSTACLE, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_DETECT_DANGER_OBSTACLE, source=STATE_ERROR_COLLISION, dest=STATE_ERROR_COLLISION),
    dict(trigger=TRIGGER_BREAK_RELEASE_BUTTON_ON, source=STATE_ERROR_COLLISION, dest=STATE_IDLE),
]


class PitakuruStateModel(object):
    def __init__(self):
        self.machine = Machine(
            model=self,
            states=states,
            transitions=transitions,
            initial=STATE_SHUTDOWN,
            auto_transitions=False
        )
        self.emergency_button_off()


class PitakuruState(object):
    def __init__(self, model):
        rospy.init_node('PitakuruState')
        self.sub = rospy.Subscriber('trigger_action', TriggerAction, self.callback)
        self.pub = rospy.Publisher('state', State, queue_size=2)
        self.model = model

    def callback(self, data):
        rospy.logwarn(data.trigger)
        getattr(self.model, data.trigger)()
        self.update_state()

    def update_state(self):
        current_state = getattr(State, 'STATE_{}'.format(self.model.state))
        self.pub.publish(current_state)


if __name__ == "__main__":
    model = PitakuruStateModel()
    
    state = PitakuruState(model)
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()




    # from controllers import JoyStickController
    # from switches import SwitchInput

    # # 2. ボタンにステートマシンを関連付け
    # switch = SwitchInput()
    # switch.add_button_event_cb('karugamo', lambda _: model.karugamo_button_on())
    # switch.add_button_event_cb('idle', lambda _: model.remote_idle_button_on())
    # switch.add_button_event_cb('brake', lambda _: model.collision())
    # switch.add_button_event_cb('release', lambda _: model.break_release_button_on())

    # # 3. コントローラにステートマシンを関連付け
    # controller = JoyStickController()
    # controller.add_button_event_cb('circle', lambda _: model.remote_karuamo_button_on()) # とりあえずcircle
    # controller.add_button_event_cb('triangle', lambda _: model.remote_manual_button_on()) # とりあえずtriangle
    # controller.add_button_event_cb('square', lambda _: model.remote_idle_button_on()) # とりあえずsquare

    # # 4. イベントループ
    # current_state = model.state
    # model.emergency_button_off()
    # while True:
    #     controller.next_iter()
    #     switch.next_iter()
    #     if model.state != current_state:
    #         current_state = model.state
    #         print(current_state)
    #         switch.set_LED_color(current_state)
