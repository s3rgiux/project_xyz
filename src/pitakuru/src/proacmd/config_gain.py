import commands as cmd
import msvcrt
import pyproacmd
from pyproacmd import Utils
import struct
import time


class GainConfigurator:
    def __init__(self, proacmd, id=1):
        self.pc = proacmd
        self.id = id
        self.GAIN_INC_DEC_VAL = 100

    def _error_occurred(self, resp_packet):
        if resp_packet == None:
            print("Error")
            return True

        elif resp_packet.resp.header.err != 0:    # if the SDK State is not IDLE
            print("Error: Controller is not IDLE (State:{})".format(resp_packet.resp.header.err))
            return True

        else:
            return False 
    
    def _prepare_target_vals(self, current_vals, Kx, direction):
        target_Kx_vals = list(current_vals.resp.body)

        if Kx == 'Kp':
            if direction == 'inc':
                target_Kx_vals[0] += self.GAIN_INC_DEC_VAL
            elif direction == 'dec':
                target_Kx_vals[0] -= self.GAIN_INC_DEC_VAL
        elif Kx == 'Ki':
            if direction == 'inc':
                target_Kx_vals[1] += self.GAIN_INC_DEC_VAL
            elif direction == 'dec':
                target_Kx_vals[1] -= self.GAIN_INC_DEC_VAL
        
        return target_Kx_vals
    
    def _print_new_vals(self, prev_result, new_result):
        print("Set (Kp, Ki): ({}, {}) -> ({}, {})".format(prev_result.resp.body[0], prev_result.resp.body[1], new_result.resp.body[0], new_result.resp.body[1]))

    def get_speed_gain_handler(self):
        result = self.pc.send_receive(cmd.GetSpeedGain(self.id))

        if self._error_occurred(result):
            return

        print("Kp: {}, Ki: {}".format(result.resp.body[0], result.resp.body[1]))
    
    def inc_dec_speed_Kx_handler(self, Kx, direction):  # Kx: 'Kp' or 'Ki', direction: 'inc' or 'dec'
        prev_result = self.pc.send_receive(cmd.GetSpeedGain(self.id))

        if self._error_occurred(prev_result):
            return

        target_vals = self._prepare_target_vals(prev_result, Kx, direction)
        self.pc.send_receive(cmd.SetSpeedGain(self.id, target_vals))

        new_result = self.pc.send_receive(cmd.GetSpeedGain(self.id))
        self._print_new_vals(prev_result, new_result)
    
    def set_speed_Kx_handler(self, Kx, gain):
        prev_result = self.pc.send_receive(cmd.GetSpeedGain(self.id))

        if self._error_occurred(prev_result):
            return
        
        vals = list(prev_result.resp.body)

        if Kx == 'Kp':
            vals[0] = gain
        elif Kx == 'Ki':
            vals[1] = gain
        else:
            print('Invalid Kx')
            return

        self.pc.send_receive(cmd.SetSpeedGain(self.id, vals))

        new_result = self.pc.send_receive(cmd.GetSpeedGain(self.id))
        self._print_new_vals(prev_result, new_result)

    def get_Iq_gain_handler(self):
        result = self.pc.send_receive(cmd.GetIqGain(self.id))

        if self._error_occurred(result):
            return

        print("Kp: {}, Ki: {}".format(result.resp.body[0], result.resp.body[1]))
    
    def inc_dec_Iq_Kx_handler(self, Kx, direction):  # Kx: 'Kp' or 'Ki', direction: 'inc' or 'dec'
        prev_result = self.pc.send_receive(cmd.GetIqGain(self.id))

        if self._error_occurred(prev_result):
            return

        target_vals = self._prepare_target_vals(prev_result, Kx, direction)
        self.pc.send_receive(cmd.SetIqGain(self.id, target_vals))

        new_result = self.pc.send_receive(cmd.GetIqGain(self.id))
        self._print_new_vals(prev_result, new_result)

    def set_Iq_Kx_handler(self, Kx, gain):
        prev_result = self.pc.send_receive(cmd.GetIqGain(self.id))

        if self._error_occurred(prev_result):
            return
        
        vals = list(prev_result.resp.body)

        if Kx == 'Kp':
            vals[0] = gain  
        elif Kx == 'Ki':
            vals[1] = gain
        else:
            print('Invalid Kx')
            return

        self.pc.send_receive(cmd.SetIqGain(self.id, vals))

        new_result = self.pc.send_receive(cmd.GetIqGain(self.id))
        self._print_new_vals(prev_result, new_result)

    def get_Id_gain_handler(self):
        result = self.pc.send_receive(cmd.GetIdGain(self.id))

        if self._error_occurred(result):
            return

        print("Kp: {}, Ki: {}".format(result.resp.body[0], result.resp.body[1]))
    
    def inc_dec_Id_Kx_handler(self, Kx, direction):  # Kx: 'Kp' or 'Ki', direction: 'inc' or 'dec'
        prev_result = self.pc.send_receive(cmd.GetIdGain(self.id))

        if self._error_occurred(prev_result):
            return

        target_vals = self._prepare_target_vals(prev_result, Kx, direction)
        self.pc.send_receive(cmd.SetIdGain(self.id, target_vals))

        new_result = self.pc.send_receive(cmd.GetIdGain(self.id))
        self._print_new_vals(prev_result, new_result)
    
    def set_Id_Kx_handler(self, Kx, gain):
        prev_result = self.pc.send_receive(cmd.GetIdGain(self.id))

        if self._error_occurred(prev_result):
            return
        
        vals = list(prev_result.resp.body)

        if Kx == 'Kp':
            vals[0] = gain
        elif Kx == 'Ki':
            vals[1] = gain
        else:
            print('Invalid Kx')
            return

        self.pc.send_receive(cmd.SetIdGain(self.id, vals))

        new_result = self.pc.send_receive(cmd.GetIdGain(self.id))
        self._print_new_vals(prev_result, new_result)


if __name__ == '__main__':
    port = Utils.select_port()
    baud = 1000000

    with pyproacmd.ProaCmd(port, baud) as pc:
        g = GainConfigurator(pc)

        get_handler = {'speed' : g.get_speed_gain_handler,
                          'Iq' : g.get_Iq_gain_handler,
                          'Id' : g.get_Id_gain_handler}
        inc_dec_handler = {'speed' : g.inc_dec_speed_Kx_handler,
                              'Iq' : g.inc_dec_Iq_Kx_handler,
                              'Id' : g.inc_dec_Id_Kx_handler}
        set_handler = {'speed' : g.set_speed_Kx_handler,
                          'Iq' : g.set_Iq_Kx_handler,
                          'Id' : g.set_Id_Kx_handler}
        
        target_loop = 'speed'
        target_coefficient = 'Kp'

        try:
            while True:
                time.sleep(0.01)
                if msvcrt.kbhit():
                    c = msvcrt.getwch()
                    print(c)

                    if c == 's':
                        target_loop = 'speed'
                        print('Target:{}, {}'.format(target_loop, target_coefficient))
                    elif c == 'q':
                        target_loop = 'Iq'
                        print('Target:{}, {}'.format(target_loop, target_coefficient))
                    elif c == 'd':
                        target_loop = 'Id'
                        print('Target:{}, {}'.format(target_loop, target_coefficient))

                    elif c == 'P':
                        target_coefficient = 'Kp'
                        print('Target:{}, {}'.format(target_loop, target_coefficient))
                    elif c == 'I':
                        target_coefficient = 'Ki'
                        print('Target:{}, {}'.format(target_loop, target_coefficient))

                    elif c == 'g':
                        get_handler[target_loop]()
                    elif c == 'i':
                        inc_dec_handler[target_loop](target_coefficient, 'inc')
                    elif c == ',':
                        inc_dec_handler[target_loop](target_coefficient, 'dec')
                    elif c == 'f':
                        gain = input('Gain <int16> : ')
                        gain = int(gain)
                        set_handler[target_loop](target_coefficient, gain)
                    
        except KeyboardInterrupt:
            print('Ctrl-C')