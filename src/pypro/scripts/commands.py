import struct
import command_components as compo
from binascii import crc32


class Disable:
    TYPE = 0x50
    REQ_BODY_LEN = 0

    def __init__(self, dest_id):
        self.req = compo.ReqPacket(dest_id, Disable.REQ_BODY_LEN, Disable.TYPE, None, Disable.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return b''
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO


class Enable:
    TYPE = 0x51
    REQ_BODY_LEN = 0

    def __init__(self, dest_id):
        self.req = compo.ReqPacket(dest_id, Enable.REQ_BODY_LEN, Enable.TYPE, None, Enable.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return b''
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO


class RunAtVel:
    TYPE = 0x62
    REQ_BODY_LEN = 4

    def __init__(self, dest_id, velocity): # velocity:[rad/s]
        self.req = compo.ReqPacket(dest_id, RunAtVel.REQ_BODY_LEN, RunAtVel.TYPE, velocity, RunAtVel.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return struct.pack('<f', body)
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO


class ReadFOC:
    TYPE = 0x63
    REQ_BODY_LEN = 0

    def __init__(self, dest_id):
        self.req = compo.ReqPacket(dest_id, ReadFOC.REQ_BODY_LEN, ReadFOC.TYPE, None, ReadFOC.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return b''
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = struct.unpack('<fff', self.resp.get_body_bytes())
        return self.resp.body #TODO


class GetAbsencOffset:
    TYPE = 0x64
    REQ_BODY_LEN = 0

    def __init__(self, dest_id):
        self.req = compo.ReqPacket(dest_id, GetAbsencOffset.REQ_BODY_LEN, GetAbsencOffset.TYPE, None, GetAbsencOffset.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return b''
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = struct.unpack('<H', self.resp.get_body_bytes())
        return self.resp.body #TODO


class SetAbsencOffset:
    TYPE = 0x65
    REQ_BODY_LEN = 2

    def __init__(self, dest_id, offset):    # 0 ~ 0x3FFF
        self.req = compo.ReqPacket(dest_id, SetAbsencOffset.REQ_BODY_LEN, SetAbsencOffset.TYPE, offset, SetAbsencOffset.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return struct.pack('<H', body)
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO


class GetSpeedGain:
    TYPE = 0x66
    REQ_BODY_LEN = 0

    def __init__(self, dest_id):
        self.req = compo.ReqPacket(dest_id, GetSpeedGain.REQ_BODY_LEN, GetSpeedGain.TYPE, None, GetSpeedGain.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return b''
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = struct.unpack('<HH', self.resp.get_body_bytes())
        return self.resp.body #TODO


class SetSpeedGain:
    TYPE = 0x67
    REQ_BODY_LEN = 4

    def __init__(self, dest_id, gains):     # (Kp, Ki)
        self.req = compo.ReqPacket(dest_id, SetSpeedGain.REQ_BODY_LEN, SetSpeedGain.TYPE, gains, SetSpeedGain.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return struct.pack('<HH', *body)
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO


class GetIqGain:
    TYPE = 0x68
    REQ_BODY_LEN = 0

    def __init__(self, dest_id):
        self.req = compo.ReqPacket(dest_id, GetIqGain.REQ_BODY_LEN, GetIqGain.TYPE, None, GetIqGain.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return b''
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = struct.unpack('<HH', self.resp.get_body_bytes())
        return self.resp.body #TODO


class SetIqGain:
    TYPE = 0x69
    REQ_BODY_LEN = 4

    def __init__(self, dest_id, gains):     # (Kp, Ki)
        self.req = compo.ReqPacket(dest_id, SetIqGain.REQ_BODY_LEN, SetIqGain.TYPE, gains, SetIqGain.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return struct.pack('<HH', *body)
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO


class GetIdGain:
    TYPE = 0x6a
    REQ_BODY_LEN = 0

    def __init__(self, dest_id):
        self.req = compo.ReqPacket(dest_id, GetIdGain.REQ_BODY_LEN, GetIdGain.TYPE, None, GetIdGain.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return b''
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = struct.unpack('<HH', self.resp.get_body_bytes())
        return self.resp.body #TODO


class SetIdGain:
    TYPE = 0x6b
    REQ_BODY_LEN = 4

    def __init__(self, dest_id, gains):     # (Kp, Ki)
        self.req = compo.ReqPacket(dest_id, SetIdGain.REQ_BODY_LEN, SetIdGain.TYPE, gains, SetIdGain.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return struct.pack('<HH', *body)
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO


class MoveTo:
    TYPE = 0x6c
    REQ_BODY_LEN = 4

    def __init__(self, dest_id, position): # position:[rad]
        self.req = compo.ReqPacket(dest_id, MoveTo.REQ_BODY_LEN, MoveTo.TYPE, position, MoveTo.body_binarizer)

    @classmethod
    def body_binarizer(cls, body, byteorder='little'):
        return struct.pack('<f', body)
    
    def as_bytes(self, byteorder='little'):
        return self.req.as_bytes(byteorder)

    def parse(self, raw_bytes):
        self.resp = compo.RespPacket(raw_bytes)
        self.resp.body = None
        return self.resp.body #TODO
