import commands as cmd
import pyproacmd
from pyproacmd import Utils
import msvcrt
import datetime
import time
import logging

file_name = "log_angle_id.log"
fmt = "%(asctime)s %(message)s"
logging.basicConfig(level=logging.DEBUG, filename=file_name, format=fmt)

port = Utils.select_port()
baud = 1000000
id = 1

with pyproacmd.ProaCmd(port, baud) as pc:
    try:
        pc.send_receive(cmd.Enable(id))
        pc.send_receive(cmd.RunAtVel(id, Utils.RPMtoRADpS(120)))
        while True:
            time.sleep(0.01)
            resp = pc.send_receive(cmd.ReadFOC(id))
            logging.debug("{} {}".format(resp.resp.body[0], resp.resp.body[1])) #angle, speed

    except KeyboardInterrupt:
        pc.send_receive(cmd.Disable(id))
        print('Ctrl-C')