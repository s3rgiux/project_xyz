from binascii import crc32
import commands
from math import pi
import serial
import serial.tools.list_ports
import struct
import sys
import codecs


class ProaCmd:  # Use 'with' statement
    RESP_TIMEOUT = 0.1 #[sec]
    
    def __init__(self, port, baud):
        self._port = port
        self._baud = baud
    
    def setup(self):
        self._ser = serial.Serial(self._port, 
                                  self._baud, 
                                  timeout=ProaCmd.RESP_TIMEOUT, 
                                  write_timeout=1)
        return self

    def close(self):
        self._ser.close()

    def send_receive(self, command):
        # Prepare command packet (bytes)
        raw_req = command.as_bytes()
        print('> ' + codecs.encode(raw_req, 'hex_codec'))

        # Flush
        self._ser.reset_input_buffer()

        # Send
        self._ser.write(raw_req)

        # Wait response
        src_id = self._ser.read(1) # expecting bytes including one character
        # print(src_id)

        if len(src_id) != 1:
            print('**** Timeout ****')
            print('> ' + codecs.encode(raw_req, 'hex_codec'))
            return None #TODO

        # Read remaining (Assuming that a packet comes continuously (i.e. without breaks))
        length = self._ser.read(1)
        raw_resp = src_id + length + self._ser.read(ord(length) - 2)

        # Parse
        try:
            command.parse(raw_resp)
            print('<', 
                command.resp.header.src_id, 
                hex(command.resp.header.err), 
                hex(command.resp.header.resp_type), 
                command.resp.body, 
                hex(command.resp.crc))
        
        except:
            print('Error occurred')
            print('< ' + codecs.encode(raw_req, 'hex_codec'))

        return command

class Utils:
    @classmethod
    def RPMtoRADpS(cls, rpm):
        return rpm / 60.0 * 2.0 * pi

    @classmethod
    def RADpStoRPM(cls, rad):
        return rad / (2.0 * pi) * 60.0

    @classmethod
    def select_port(cls):
        print('- available COM ports')

        portlist = serial.tools.list_ports.comports()

        if not portlist:
            print('No available port')
            sys.exit()

        print('i : name')
        print('--------')
        for i, port in enumerate(portlist):
            print(i, ':', port.device)
        
        print('- Enter the port number ( not the name )')
        portnum = input()
        portnum = int(portnum)

        portdev = None
        if portnum in range(len(portlist)):
            portdev= portlist[portnum].device

        return portdev
