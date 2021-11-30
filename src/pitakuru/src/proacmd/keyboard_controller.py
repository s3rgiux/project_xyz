import commands as cmd
import msvcrt
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
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(1200)))
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


if __name__ == '__main__':
    port = Utils.select_port()
    baud = 1000000

    with pyproacmd.ProaCmd(port, baud) as pc:
        kc = KeyCtrlr(pc)

        continuous = False

        try:
            while True:
                time.sleep(0.01)
                if msvcrt.kbhit():
                    c = msvcrt.getwch()
                    print(c)

                    if c == 'e':
                        kc.enable_handler()
                    elif c == 'i':
                        kc.forward_handler()
                    elif c == ',':
                        kc.backward_handler()
                    elif c == 'j':
                        kc.left_rotate_handler()
                    elif c == 'l':
                        kc.right_rotate_handler()
                    elif c == 'k':
                        continuous = False
                        kc.disable_handler()
                    elif c == 'r':
                        kc.read_foc_handler()
                    elif c == 'c':
                        continuous = True
                    
                if continuous:
                    kc.forward_handler()

        except KeyboardInterrupt:
            print('Ctrl-C')