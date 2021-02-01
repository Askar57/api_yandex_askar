import PyQt5
from PyQt5 import QtWidgets


class QMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LoginWindow")
        MainWindow.resize(800, 600)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WMainWindow = QtWidgets.QMainWindow()
    ui = QMainWindow()
    ui.setupUi(WMainWindow)
    # Запуск
    WMainWindow.show()
    sys.exit(app.exec_())