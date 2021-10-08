import commands as cmd
import msvcrt
import pyproacmd
from pyproacmd import Utils
import struct
import time


class AbsencManager:
    def __init__(self, proacmd, id=1):
        self.pc = proacmd
        self.id = id
        self.OFFSET_INC_DEC_VAL = 100

    def get_offset_handler(self):
        result = self.pc.send_receive(cmd.GetAbsencOffset(self.id))

        if result == None:
            print("Error")
        elif result.resp.header.err != 0:    # if the SDK State is not IDLE
            print("Error: Controller is not IDLE (State:{})".format(result.resp.header.err))
        else:
            print("Offset: {}".format(result.resp.body[0]))
    
    def increment_offset_handler(self):
        result = self.pc.send_receive(cmd.GetAbsencOffset(self.id))
        current_offset = result.resp.body[0]

        if result == None:
            print("Error")
        elif result.resp.header.err != 0:    # if the SDK State is not IDLE
            print("Error: Controller is not IDLE (State:{})".format(result.resp.header.err))
        else:
            self.pc.send_receive(cmd.SetAbsencOffset(self.id, current_offset + self.OFFSET_INC_DEC_VAL))

            result = self.pc.send_receive(cmd.GetAbsencOffset(self.id))
            new_offset = result.resp.body[0]
            print("Set: {} -> {}".format(current_offset, new_offset))

    def decrement_offset_handler(self):
        result = self.pc.send_receive(cmd.GetAbsencOffset(self.id))
        current_offset = result.resp.body[0]

        if result == None:
            print("Error")
        elif result.resp.header.err != 0:    # if the SDK State is not IDLE
            print("Error: Controller is not IDLE (State:{})".format(result.resp.header.err))
        else:
            self.pc.send_receive(cmd.SetAbsencOffset(self.id, current_offset - self.OFFSET_INC_DEC_VAL))

            result = self.pc.send_receive(cmd.GetAbsencOffset(self.id))
            new_offset = result.resp.body[0]
            print("Set: {} -> {}".format(current_offset, new_offset))


if __name__ == '__main__':
    port = Utils.select_port()
    baud = 1000000

    with pyproacmd.ProaCmd(port, baud) as pc:
        ae = AbsencManager(pc)

        try:
            while True:
                time.sleep(0.01)
                if msvcrt.kbhit():
                    c = msvcrt.getwch()
                    print(c)

                    if c == 'g':
                        ae.get_offset_handler()
                    elif c == 'i':
                        ae.increment_offset_handler()
                    elif c == ',':
                        ae.decrement_offset_handler()
                    
        except KeyboardInterrupt:
            print('Ctrl-C')