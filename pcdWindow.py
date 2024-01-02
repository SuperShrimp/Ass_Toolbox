import open3d
from PySide6 import QtWidgets, QtGui, QtCore
import win32gui
import sys
import numpy as np

def read_file(path):
    pcl = np.load(path)
    return pcl

class VisWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(VisWindow, self).__init__()
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        self.setCentralWidget(widget)

        pcl = np.load('pcl_2.npy')
        pcl = pcl[:, :3]
        pts = open3d.geometry.PointCloud()
        pts.points = open3d.utility.Vector3dVector(pcl)
        self.vis = open3d.visualization.Visualizer()
        self.vis.create_window()
        self.vis.add_geometry(pts)

        hwnd = win32gui.FindWindowEx(0, 0, None, "Open3D")
        self.window = QtGui.QWindow.fromWinId(hwnd)
        self.window.setGeometry(100, 100, 600, 500)
        self.windowcontainer = self.createWindowContainer(self.window, widget)
        layout.addWidget(self.windowcontainer, 0, 0)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_vis)
        timer.start(1)

    def update_vis(self):
        # self.vis.update_geometry()
        self.vis.poll_events()
        self.vis.update_renderer()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    form = VisWindow()
    form.setWindowTitle('o3d Embed')
    form.setGeometry(100, 100, 600, 500)
    form.show()
    sys.exit(app.exec_())