import commands as cmd
#import msvcrt
import keyboard
import pyproacmd
from pyproacmd import Utils
import struct
import time


class KeyCtrlr:
    def __init__(self, proacmd, id_L=1, id_R=2):
        self.pc = proacmd
        self.id_L = id_L
        self.id_R = id_R

    def forward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(60)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def backward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(-1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def left_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(-1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def right_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def enable_handler(self):
        result = self.pc.send_receive(cmd.Enable(self.id_L))
        #result = self.pc.send_receive(cmd.Disable(self.id_R))

    def disable_handler(self):
        result = self.pc.send_receive(cmd.Disable(self.id_L))
        #result = self.pc.send_receive(cmd.Disable(self.id_R))
    
    def read_foc_handler(self):
        result = self.pc.send_receive(cmd.ReadFOC(self.id_L))
        #result = self.pc.send_receive(cmd.ReadFOC(self.id_R))
    
    def move_to_handler(self, pos):
        result = self.pc.send_receive(cmd.MoveTo(self.id_L, pos))


if __name__ == '__main__':
    port = Utils.select_port()
    baud = 1000000

    with pyproacmd.ProaCmd(port, baud) as pc:
        kc = KeyCtrlr(pc)

        continuous = False

        try:
            while True:
                time.sleep(0.01)
                #if msvcrt.kbhit():
                    #c = msvcrt.getwch()
                    #print(c)

                if keyboard.is_pressed('e'): #if c == 'e':
                    kc.enable_handler()
                elif keyboard.is_pressed('i'): #elif c == 'i':
                    kc.forward_handler()
                elif keyboard.is_pressed(','):#elif c == ',':
                    kc.backward_handler()
                elif keyboard.is_pressed('j'):#elif c == 'j':
                    kc.left_rotate_handler()
                elif keyboard.is_pressed('l'):#elif c == 'l':
                    kc.right_rotate_handler()
                elif keyboard.is_pressed('k'):#elif c == 'k':
                    continuous = False
                    kc.disable_handler()
                elif keyboard.is_pressed('r'):#elif c == 'r':
                    kc.read_foc_handler()
                elif keyboard.is_pressed('c'):#elif c == 'c':
                    continuous = True
                elif keyboard.is_pressed('0') or keyboard.is_pressed('1') or keyboard.is_pressed('2') or keyboard.is_pressed('3') or keyboard.is_pressed('4') or keyboard.is_pressed('5') or keyboard.is_pressed('6') or keyboard.is_pressed('7'):#elif c >= '0' and c <= '9':
                    kc.move_to_handler(int(c) * 2 * 3.14159 / 10 - 3.14159)
                    
                if continuous:
                    kc.forward_handler()

        except KeyboardInterrupt:
            print('Ctrl-C')
