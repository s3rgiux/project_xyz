from rplidar import RPLidar
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

from config import config
from movement import AntiGravityMovement

# -> offsetsを返すだけのクラスに変更
class Lidar(object):
    def __init__(self, C=config(), wait_startup=2):
        self.C = C
        self.DMAX = C['rplidar']['dmax']
        self.IMIN = C['rplidar']['imin']
        self.IMAX = C['rplidar']['imax']
        self.ignore_min = C['rplidar']['ignore_min']
        self.ignore_max = C['rplidar']['ignore_max']
        self.IN = C['rplidar']['ignore_neighborhood']

        self._lidar = RPLidar(C['rplidar']['port_name'])
        # https://github.com/SkoltechRobotics/rplidar/issues/10
        import time; time.sleep(wait_startup)
        self.iterator = self._lidar.iter_scans(max_buf_meas=1000, min_len=1)

    """データを読み取って、極座標で返す
    """
    def next_iter(self, iterator=None, filter=None):
        scan = next(iterator or self.iterator)
        offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
        if filter:
            offsets = self.filter_neighbor(offsets)
        return offsets


    '''データを読み取って、回避ベクトルと障害物のデータを返す -> movement
    offsetsの取得のみに変更
    '''
    # def next_iter(self, iterator=None, target=None):
    #     scan = next(iterator or self.iterator)
    #     offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
    #     offsets = self.ignore_backward(offsets)
    #     if target is not None:
    #         offsets = self.ignore_neighborhood(offsets, target)
    #     power = self.anti_gravity(offsets)
    #     # print("pow: {}, deg: {}".format(power[1], power[0]*180/np.pi))
    #     return power, offsets, scan

    '''RPLidarのデスクリプタ削除とモーターの停止
    '''
    def release(self):
        self._lidar.stop()
        self._lidar.stop_motor()
        self._lidar.disconnect()

    '''matplotlibアニメーションフレーム処理関数
    '''
    def update_line(self, num, iterator, line):
        offsets = self.next_iter(iterator)

        line.set_offsets(offsets)
        #line.set_array(offsets)
        return line

    '''matplotlibで極座標表示する
    '''
    def run(self):
        fig = plt.figure()
        ax = plt.subplot(111, projection='polar')
        line = ax.scatter([0, 0], [0, 0], s=5, c=[self.IMIN, self.IMAX],
                            cmap=plt.cm.Greys_r, lw=0)
        ax.set_rmax(self.DMAX)
        ax.grid(True)
        ani = animation.FuncAnimation(fig, self.update_line,
            fargs=(self.iterator, line), interval=50)
        plt.show()
        self.release()


if __name__ == '__main__':
    lidar = Lidar()
    movement = AntiGravityMovement()
    """while True:
        try:
            offsets = lidar.next_iter()
            offsets = movement.check_danger_neighbor(offsets)
            print(offsets)
        except KeyboardInterrupt:
            lidar.release()
            break"""
    lidar.run()