from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget, QVBoxLayout, QLabel

class SelectWindow(QMainWindow):
    '''
    This window is for selecting the point cloud file for viusalization
    '''
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(" Window for selecting point cloud")