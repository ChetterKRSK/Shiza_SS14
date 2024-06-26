import sys
import os
import client
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QCoreApplication

from main_Window import Ui_MainWindow as Ui_MainWindow_1
from connecting_Dialog import Ui_Dialog as UiDialog_1


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)

        for message in savedData["messages"]:
            self.ui.cb_Messages.addItem(message)
        self.ui.kse_Key.setKeySequence(savedData["key"])

        self.ui.pb_ChangeStatus.clicked.connect(self.openConnectingWindow)
        self.ui.pb_AddMessage.clicked.connect(self.addMessage)
        self.ui.pb_RemoveMessage.clicked.connect(self.removeMessage)
        self.ui.cb_Messages.currentIndexChanged.connect(self.pasteMessageFromComboBox)
        self.ui.pb_SendMessages.clicked.connect(self.sendMessage)
        self.ui.kse_Key.keySequenceChanged.connect(self.changeKey)

    def openConnectingWindow(self) -> None:
        connectingDialog.show()

    def disconnect(self) -> None:
        connectionClient.disconnect()
        self.changeStatus()

    def addMessage(self) -> None:
        text = self.ui.le_Message.text()
        if text != "" and text not in savedData["messages"]:
            savedData["messages"].append(text)
            self.ui.cb_Messages.addItem(text)
            save("saved_data.json", savedData)

    def removeMessage(self) -> None:
        text = self.ui.le_Message.text()
        if text in savedData["messages"]:
            self.ui.cb_Messages.removeItem(savedData["messages"].index(text))
            savedData["messages"].remove(text)
            save("saved_data.json", savedData)

    def pasteMessageFromComboBox(self) -> None:
        text = savedData["messages"][self.ui.cb_Messages.currentIndex()]
        self.ui.le_Message.setText(text)

    def changeKey(self) -> None:
        if self.ui.kse_Key.keySequence().toString() == "Return":
            self.ui.kse_Key.setKeySequence("")
            return
        savedData["key"] = self.ui.kse_Key.keySequence().toString()
        save("saved_data.json", savedData)

    def sendMessage(self) -> None:
        if not connectionClient.connected:
            return
        text = self.ui.le_Message.text()
        key = self.ui.kse_Key.keySequence().toString()
        if text == "" or key == "":
            return
        try:
            connectionClient.send_message_in_thread(message_text=text, key_to_print=key)
        except ConnectionResetError:
            self.changeStatus()
        else:
            self.ui.le_Message.clear()

    def changeStatus(self) -> None:
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
        if "ip" in savedData.keys() and "port" in savedData.keys():
            self.ui.le_IPLine.setText(savedData["ip"])
            self.ui.le_PortLine.setText(
                str(savedData["port"]) if savedData["port"] != 0 else ""
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
        savedData["ip"] = ip
        savedData["port"] = port
        save("saved_data.json", savedData)
        try:
            connectionClient.connect()
        except WindowsError:
            print("Connect error")
        else:
            with open("saved_data.json", "w") as file:
                json.dump(savedData, file)
            mainWindow.changeStatus()
            self.close()


def load(file_name: str) -> dict:
    with open(file_name, "r") as file:
        return json.load(file)


def save(file_name: str, data: dict) -> None:
    with open(file_name, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    connectionClient = client.ClientSocket()

    savedData = {"ip": "", "port": "", "key": "", "messages": []}
    if os.path.isfile("saved_data.json"):
        savedData = load("saved_data.json")

    mainWindow = MainWindow()
    connectingDialog = ConnectingDialog(mainWindow)
    mainWindow.show()

    sys.exit(app.exec())
