import automationhat
class SwitchInput(object):

    def __init__(self):
        self.callbacks = dict()
        self.button_states = dict()
        self.current_bumper=0
    
    def update(self):
        tmp = automationhat.input[2].read()
        if self.current_bumper == tmp:
            self.button_states["brake"]=0
            self.button_states["release"]=0
        elif self.current_bumper < tmp:
            self.button_states["brake"]=1
            self.button_states["release"]=0
        elif self.current_bumper > tmp:
            self.button_states["brake"]=0
            self.button_states["release"]=1
        self.current_bumper=tmp
        self.button_states["karugamo"]=automationhat.input[0].read()
        self.button_states["idle"]=automationhat.input[1].read()

    def getButton(self,name):
        return self.button_states[name]

    def add_button_event_cb(self, button_name, callback):
        print("add callback")
        self.callbacks[button_name] = callback
        print(self.callbacks)

    def next_iter(self):
        self.update()
        for btn, callback in self.callbacks.items():
            if self.getButton(btn) :
                callback(btn)

    def set_LED_color(self,state):
        if state=="ACTIVE_KARUGAMO":
            automationhat.relay.one.on()
            automationhat.relay.two.on()
            automationhat.relay.three.off()
        elif state=="IDLE":
            automationhat.relay.one.off()
            automationhat.relay.two.on()
            automationhat.relay.three.off()
        elif state=="ACTIVE_MANUAL":
            automationhat.relay.one.off()
            automationhat.relay.two.off()
            automationhat.relay.three.on()
        elif state=="ERROR_OBSTACLE":
            automationhat.relay.one.on()
            automationhat.relay.two.off()
            automationhat.relay.three.on()
        elif state=="ERROR_COLLISION":
            automationhat.relay.one.on()
            automationhat.relay.two.off()
            automationhat.relay.three.off()
        else:
            automationhat.relay.one.off()
            automationhat.relay.two.off()
            automationhat.relay.three.off()


if __name__ == "__main__":
    hat = SwitchInput()
    while True:
        hat.update()
        if hat.getButton("one"):
            print("pressed one")
        elif hat.getButton("two"):
            print("pressed two")
        elif hat.getButton("three"):
            print("pressed three")
        elif hat.getButton(""):
            print("pressed ")
