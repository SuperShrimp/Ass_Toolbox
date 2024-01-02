# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingWindow-demo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QPlainTextEdit, QSizePolicy, QMainWindow,
    QWidget)
from pcdWindow import VisWindow

class SelectWindow(QMainWindow):
    def __init__(self, file_path = 'None'):
        super(SelectWindow, self).__init__()
        self.Background_Color = 'White'
        self.Point_Color = 'Black'
        self.file_path = file_path
        self.setupUi()

    def setupUi(self):
        self.setGeometry(400, 400, 400, 300)
        self.setWindowTitle('Select Features')

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(400, 40, 81, 241)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.recieve_ms_and_switch)
        self.buttonBox.rejected.connect(self.close)

        self.Back_bt = QComboBox(self)
        self.Back_bt.addItem("Black")
        self.Back_bt.addItem("White")
        self.Back_bt.addItem("Yellow")
        self.Back_bt.addItem("Red")
        self.Back_bt.setObjectName(u"comboBox")
        self.Back_bt.setGeometry(120, 140, 81, 21)

        self.Background = QLabel(self)
        self.Background.setObjectName(u"Background")
        self.Background.setText('Background: ')
        self.Background.setGeometry(40, 140, 71, 20)

        self.PointColor = QLabel(self)
        self.PointColor.setObjectName(u"PointColor")
        self.PointColor.setText('Point Color: ')
        self.PointColor.setGeometry(40, 190, 81, 16)

        self.PointColor_bt = QComboBox(self)
        self.PointColor_bt.addItem("Black")
        self.PointColor_bt.addItem("Blue")
        self.PointColor_bt.addItem("Yellow")
        self.PointColor_bt.addItem("Red")
        self.PointColor_bt.addItem("White")
        self.PointColor_bt.addItem("intensity")
        self.PointColor_bt.setObjectName(u"comboBox_2")
        self.PointColor_bt.setGeometry(120, 190, 81, 22)

        self.File_Path = QLabel(self)
        self.File_Path.setObjectName(u"File_Path")
        self.File_Path.setText('File Path: ')
        self.File_Path.setGeometry(40, 60, 154, 16)


        self.op_file_path = QLabel(self)
        self.op_file_path.setObjectName(u"op_file_path")
        self.op_file_path.setText(self.file_path)
        self.op_file_path.setGeometry(110, 60, 271, 16)
        # self.op_file_path.setToolTip(self.file_path)

        # self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        # self.buttonBox.rejected.connect(Dialog.reject)

        # QMetaObject.connectSlotsByName()
    # setupUi

    # def retranslateUi(self, Dialog):
    #     Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    #     self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Black", None))
    #     self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"White", None))
    #     self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Yellow", None))
    #     self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Red", None))
    #
    #     self.Background.setText(QCoreApplication.translate("Dialog", u"Background", None))
    #     self.PointColor.setText(QCoreApplication.translate("Dialog", u"Point Color", None))
    #     self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Blue", None))
    #     self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Black", None))
    #     self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"White", None))
    #     self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"Red", None))
    #     self.comboBox_2.setItemText(4, QCoreApplication.translate("Dialog", u"Intensity", None))
    #
    #     self.File_Path.setText(QCoreApplication.translate("Dialog", u"File Path: ", None))
    # # retranslateUi
    def recieve_ms_and_switch(self):
        background_color = self.Back_bt.currentText()
        point_color = self.PointColor_bt.currentText()
        self.sub_window = VisWindow(file_path=self.file_path, bg_color= background_color, pt_color=point_color)
        self.sub_window.setGeometry(100, 100, 600, 500)
        self.sub_window.show()  # 使用 exec_() 方法以模态方式显示窗口


if __name__ == '__main__':
    app = QApplication([])
    window = SelectWindow()
    window.show()
    app.exec_()


