from binascii import crc32
import commands
from math import pi
import serial
import serial.tools.list_ports
import struct
import sys


class ProaCmd:  # Use 'with' statement
    RESP_TIMEOUT = 0.1 #[sec]
    
    def __init__(self, port, baud):
        self._port = port
        self._baud = baud
        self._ser = serial.Serial(self._port,self._baud,timeout=ProaCmd.RESP_TIMEOUT,write_timeout=1)

    def __enter__(self):
        self._ser = serial.Serial(self._port, 
                                  self._baud, 
                                  timeout=ProaCmd.RESP_TIMEOUT, 
                                  write_timeout=1)
        return self

    def __exit__(self, type, value, traceback):
        self._ser.close()
    
    def sclose(self):
        self._ser.close()

    def send_receive(self, command):
        # Prepare command packet (bytes)
        raw_req = command.as_bytes()
        print('>', raw_req.encode('hex'))

        # Flush
        self._ser.reset_input_buffer()

        # Send
        self._ser.write(raw_req)

        # Wait response
        src_id = self._ser.read(1) # expecting bytes including one character

        if len(src_id) != 1:
            print('**** Timeout ****')
            return None #TODO

        # Read remaining (Assuming that a packet comes continuously (i.e. without breaks))
        length = self._ser.read(1)
        raw_resp = src_id + length + self._ser.read(int(length[0].encode('hex'),16) - 2)
        

        # Parse
        try:
            command.parse(raw_resp)
            print('<',command.resp.header.src_id.encode('hex'),
                command.resp.header.err.encode('hex'),
                command.resp.header.resp_type.encode('hex'),
                command.resp.body)
            #print('<', 
            #    command.resp.header.src_id.encode('hex'), 
            #    command.resp.header.err.encode('hex'), 
            #    command.resp.header.resp_type.encode('hex'), 
            #    command.resp.body, 
            #    command.resp.crc.encode('hex'))
            #print('mdfg')
        
        except:
            print('Error occurred')
            print('<', raw_resp.encode('hex'))

        return command

class Utils:
    @classmethod
    def RPMtoRADpS(cls, rpm):
        return rpm / 60.0 * 2.0 * pi

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

        print(portdev)

        return portdev
