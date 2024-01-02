from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedWidget
from PySide6.QtWidgets import QFileDialog, QScrollArea
# from pcd_Window import VisWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QPushButton, QLabel
from pcdWindow import VisWindow
from SettingWindow import SelectWindow
from pc_recognition import pointcloud_recognize
class SubWindow(QDialog):
    def __init__(self):
        super(SubWindow, self).__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('子窗口')

        layout = QVBoxLayout(self)

        label = QLabel('这是一个弹出的新窗口', self)
        layout.addWidget(label)

        btn_close = QPushButton('关闭窗口', self)
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.file_path = 'None'
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 357, 378)
        self.setWindowTitle('MainWindow')

        self.btn_select_file = QPushButton('choose a file', self)
        self.btn_select_file.setGeometry(110, 90, 131, 51)
        self.btn_select_file.clicked.connect(self.show_file_dialog)
        self.path_label = QLabel('Path: ' + self.file_path, self)
        self.path_label.setGeometry(120, 160, 211, 31)
        self.path_label.setWordWrap(True)
        self.path_label.setToolTip('Path: ' + self.file_path)

        self.btn_open_subwindow = QPushButton('Visualize', self)
        self.btn_open_subwindow.setGeometry(110, 210, 131, 51)
        self.btn_open_subwindow.clicked.connect(self.open_subwindow)
        # self.setCentralWidget(self.btn_open_subwindow)

    def open_subwindow(self):
        self.sub_window = SelectWindow(file_path=self.file_path)
        self.sub_window.setGeometry(100, 100, 600, 500)
        self.sub_window.show()  # 使用 exec_() 方法以模态方式显示窗口

    def show_file_dialog(self):
        # 创建文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', 'All Files (*);;Text Files (*.txt)')

        # 如果用户选择了文件，则在控制台中打印路径
        if file_path:
            print(f'选择的文件路径：{file_path}')
            self.file_path = file_path
            _, signal = pointcloud_recognize(file_path)
            if signal:
                self.path_label.setText('file path: Confirmed')
            else:
                self.path_label.setText('Please select another file!')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
