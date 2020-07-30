from controllers import JoyStickController
from switches2 import SwitchInput
import states


# 1. ステートマシンを初期化
model = states.model

# 2. ボタンにステートマシンを関連付け
switch = SwitchInput()
switch.add_button_event_cb('karugamo', lambda _: model.karugamo_button_on())
switch.add_button_event_cb('idle', lambda _: model.remote_idle_button_on())
switch.add_button_event_cb('break', lambda _: model.collision())
switch.add_button_event_cb('release', lambda _: model.break_release_button_on())

# 3. コントローラにステートマシンを関連付け
controller = JoyStickController()
controller.add_button_event_cb('circle', lambda _: model.remote_karuamo_button_on()) # とりあえずcircle
controller.add_button_event_cb('triangle', lambda _: model.remote_manual_button_on()) # とりあえずtriangle
controller.add_button_event_cb('square', lambda _: model.remote_idle_button_on()) # とりあえずsquare

# 4. イベントループ
current_state = model.state
model.emergency_button_off()
while True:
    controller.next_iter()
    switch.next_iter()
    if model.state != current_state:
        current_state = model.state
        print(current_state)
        switch.set_LED_color(current_state)
