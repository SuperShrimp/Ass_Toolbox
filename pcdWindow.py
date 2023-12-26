import open3d
from PySide6 import QtWidgets, QtGui, QtCore
import win32gui
import sys
import numpy as np

def read_file(path):
    pcl = np.load(path)
    return pcl

class VisWindow(QtWidgets):
    def __init__(self):
        super(VisWindow, self).__init__()
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        self.setCentralWidget(widget)

        pcd = open3d.io.read_point_cloud(read_file("pcl_2.npy"))
        self.vis = open3d.visualization.Visualizer()
        self.vis.create_window()
        self.vis.add_geometry(pcd)

        hwnd = win32gui.FindWindowEx(0, 0, None, "Open3D")
        self.window = QtGui.QWindow.fromWinId(hwnd)
        self.windowcontainer = self.createWindowContainer(self.window, widget)
        layout.addWidget(self.windowcontainer, 0, 0)
        timer = QtCore.QTimer(self)
        timer.connect(self.update_vis)
        timer.start(1)

    def update_vis(self):
        # self.vis.update_geometry()
        self.vis.poll_events()
        self.vis.update_renderer()

