import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from main_Window import Ui_MainWindow as Ui_MainWindow_1
from connecting_Window import Ui_MainWindow as Ui_MainWindow_2


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)

        self.ui.pb_ChangeStatus.clicked.connect(self.openConnectingWindow)

    def openConnectingWindow(self):
        self.connectingWindow = QMainWindow()
        connectingWindow = Ui_MainWindow_2()
        connectingWindow.setupUi(self.connectingWindow)
        self.connectingWindow.show()
        connectingWindow.pb_CancelButton.clicked.connect(
            lambda: self.connectingWindow.close()
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())
