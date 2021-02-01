from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class QMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LoginWindow")
        MainWindow.resize(800, 600)

    def keyPressEvent(self, buttonUpDown):

        if buttonUpDown.key() == Qt.Key_PageDown:
            self.______()

        if buttonUpDown.key() == Qt.Key_PageUp:
            self.______()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WMainWindow = QtWidgets.QMainWindow()
    ui = QMainWindow()
    ui.setupUi(WMainWindow)
    # Запуск
    WMainWindow.show()
    sys.exit(app.exec_())