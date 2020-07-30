import sys
import csv

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

DMAX = 4000
IMIN = 0
IMAX = 50


class LidarLogReader(object):
    def __init__(self, fpath, delimitor='\t'):
        self._prev_offset = None
        self._prev_inten = None
        self._discriptor = open(fpath, 'r')
        self.reader = csv.reader(self._discriptor, delimiter=delimitor)

    def __iter__(self):
        return self

    def __next__(self):
        offsets = []
        intens = []
        if self._prev_offset:
            offsets.append(self._prev_offset)
            intens.append(self._prev_inten)
        while True:
            row = next(self.reader)
            offset = [np.radians(float(row[2])), float(row[3])]
            inten = float(row[1])
            if self._prev_offset and self._prev_offset[0] > 3.14 and offset[0] < 3.14:
                # æ¬¡ã®å‘¨æœŸã¸
                self._prev_offset = offset
                self._prev_inten = inten
                break
            self._prev_offset = offset
            self._prev_inten = inten
            offsets.append(offset)
            intens.append(inten)
        return np.array(offsets), np.array(intens)


def update_line(num, iterator, line):
    offsets, intens = next(iterator)
    line.set_offsets(offsets)
    line.set_array(intens)
    return line,


def run(fpath):
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                           cmap=plt.cm.Greys_r, lw=0)
    ax.set_rmax(DMAX)
    ax.grid(True)

    iterator = LidarLogReader(fpath)
    ani = animation.FuncAnimation(fig, update_line,
        fargs=(iterator, line), interval=30)
    plt.show()

if __name__ == '__main__':
    run(sys.argv[1])