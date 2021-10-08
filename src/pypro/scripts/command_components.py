from binascii import crc32
import struct
import errors


CRC_LEN = 4


class ReqHeader:
    LEN = 3

    def __init__(self, dest_id, body_len, req_type):
        self.dest_id = dest_id
        self.body_len = body_len 
        self.req_type = req_type
        self._calc_len()
    
    def _calc_len(self):
        self.whole_len = 1 + 1 + 1 + self.body_len + CRC_LEN    # id, len, type, body, crc
        return self.whole_len

    def as_bytes(self):
        return struct.pack('<BBB', self.dest_id, self.whole_len, self.req_type)
        

class RespHeader:
    LEN = 4

    def __init__(self, resp_bytes):
        self.parse(resp_bytes)
    
    def parse(self, resp_bytes):
        self.src_id = resp_bytes[0].encode('hex')
        self.whole_len = resp_bytes[1].encode('hex')
        self.err = resp_bytes[2].encode('hex')
        self.resp_type =  resp_bytes[3].encode('hex')
        #print(struct.unpack('<BBBB', resp_bytes[:RespHeader.LEN]).encode('hex'))


class ReqPacket:
    def __init__(self, dest_id, body_len, req_type, body, binarize_func):
        self.header = ReqHeader(dest_id, body_len, req_type)
        self.body = body
        self._bin_func = binarize_func
    
    def as_bytes(self, byteorder='little'):
        header = self.header.as_bytes()
        body = self._bin_func(self.body, byteorder)
        crc = self._crc_as_bytes(body, byteorder)
        return header + body + crc

    def to_bytes(self,n,length, endianess='big'):
        h = '%x' % n
        s = ('0'*(len(h)%2) +h).zfill(length*2).decode('hex')
        return s if endianess == 'big' else s[::-1]
    
    def _crc_as_bytes(self, body_bytes, byteorder):
        crc = 0 #crc32(self.header.as_bytes() + body_bytes)
        new = self.to_bytes(crc,4,endianess='little')#struct.pack('>H',crc)#self.to_bytes(crc,4,endianess='little')
        return new#crc.to_bytes(4, byteorder=byteorder)
        

class RespPacket:
    LEN_POS = 1

    def __init__(self, resp_bytes):
        self.raw_bytes = resp_bytes
        if (len(resp_bytes) < RespPacket.LEN_POS
                or len(resp_bytes) != int(resp_bytes[RespPacket.LEN_POS].encode('hex'),16)):
            raise errors.LengthMismatchError('Length field value is {}, but the whole lentgh is {}'.format(resp_bytes[RespPacket.LEN_POS], len(resp_bytes)))
        self.header = RespHeader(resp_bytes)
        self.crc = 0 #crc32(resp_bytes[:-CRC_LEN])
        self.body = None

    def get_body_bytes(self):
        return self.raw_bytes[RespHeader.LEN:-CRC_LEN]
