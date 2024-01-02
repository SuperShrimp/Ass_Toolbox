import open3d
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QPushButton
import win32gui
import sys
import numpy as np
import Visualize_basics
from pc_recognition import pointcloud_recognize

def read_file(path):
    pcl = np.load(path)
    return pcl

class VisWindow(QtWidgets.QMainWindow):
    def __init__(self, file_path, bg_color, pt_color):
        super(VisWindow, self).__init__()
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        self.setCentralWidget(widget)

        exit_button = QPushButton('Exit Application', self)
        exit_button.clicked.connect(self.exit_application)
        exit_button.raise_()

        self.bg_color_rgb = Visualize_basics.color_transform(bg_color)
        self.pt_color_rgb = Visualize_basics.color_transform(pt_color)

        # pcl = np.load(file_path)
        pcl, _ = pointcloud_recognize(file_path)
        pts = open3d.geometry.PointCloud()
        pts.points = open3d.utility.Vector3dVector(pcl[:, :3])
        if pt_color == 'intensity':
            colors = Visualize_basics.intensity_transformation(pcl)
            pts.colors = open3d.utility.Vector3dVector(np.stack([1 - colors, colors, np.zeros_like(colors)], axis=-1))
        else:
            pts.paint_uniform_color(self.pt_color_rgb)
        self.vis = open3d.visualization.Visualizer()
        self.vis.create_window()
        opt = self.vis.get_render_option()
        opt.background_color = np.asarray(self.bg_color_rgb)
        self.vis.add_geometry(pts)



        hwnd = win32gui.FindWindowEx(0, 0, None, "Open3D")
        self.window = QtGui.QWindow.fromWinId(hwnd)
        self.window.setGeometry(100, 100, 600, 500)
        self.windowcontainer = self.createWindowContainer(self.window, widget)
        layout.addWidget(self.windowcontainer, 0, 0)
        layout.addWidget(exit_button)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_vis)
        timer.start(1)

    def exit_application(self):
        # 触发主窗口的关闭事件
        sys.exit(0)
    def update_vis(self):
        # self.vis.update_geometry()
        self.vis.poll_events()
        self.vis.update_renderer()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    form = VisWindow(file_path='data_sample/pcl_2.npy', bg_color='White', pt_color='Red')
    form.setWindowTitle('o3d Embed')
    form.setGeometry(100, 100, 600, 500)
    form.show()
    sys.exit(app.exec_())