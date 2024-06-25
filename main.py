import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from main_Window import Ui_MainWindow as Ui_MainWindow_1
from connecting_Dialog import Ui_Dialog as UiDialog_1

import client


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)

        self.ui.pb_ChangeStatus.clicked.connect(self.openConnectingWindow)

    def openConnectingWindow(self):
        # connectingWindow.show()
        connectingDialog.show()

    def disconnect(self):
        connectionClient.disconnect()
        self.changeStatus()

    def changeStatus(self):
        if connectionClient.connected:
            self.ui.le_Status1.setText("ONLINE")
            self.ui.pb_ChangeStatus.setText("DISCONNECT")
            self.ui.pb_ChangeStatus.clicked.disconnect(self.openConnectingWindow)
            self.ui.pb_ChangeStatus.clicked.connect(self.disconnect)
        else:
            self.ui.le_Status1.setText("OFFLINE")
            self.ui.pb_ChangeStatus.setText("CONNECT")
            self.ui.pb_ChangeStatus.clicked.disconnect(self.disconnect)
            self.ui.pb_ChangeStatus.clicked.connect(self.openConnectingWindow)


class ConnectingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiDialog_1()
        self.ui.setupUi(self)

        self.ui.pb_CancelButton.clicked.connect(lambda: self.close())
        self.ui.pb_ConnectButton.clicked.connect(self.connect)
        self.ui.le_IPLine.setText(connectionClient.ip)
        self.ui.le_PortLine.setText(
            str(connectionClient.port) if connectionClient.port != 0 else ""
        )

    def connect(self):
        ip = self.ui.le_IPLine.text()
        port = self.ui.le_PortLine.text()

        try:
            int(port)
        except ValueError:
            print("Port error")
            return
        else:
            port = int(port)
            if port < 1024 or port > 65535:
                print("Port error")
                return

        ip_list = [i for i in ip.split(".")]
        if ip != "localhost":
            try:
                for i in ip_list:
                    i = int(i)
                    if i < 0 or i > 255:
                        raise ValueError
            except ValueError:
                print("Ip error")
                return
            else:
                if len(ip_list) != 4:
                    print("Ip error")
                    return

        connectionClient.ip = ip
        connectionClient.port = port
        try:
            connectionClient.connect()
        except WindowsError:
            print("Connect error")
        else:
            mainWindow.changeStatus()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    connectionClient = client.ClientSocket()

    mainWindow = MainWindow()
    connectingDialog = ConnectingDialog(mainWindow)
    mainWindow.show()

    sys.exit(app.exec())
