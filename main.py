import sys
import os

import client
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QFontMetrics

from QtDesign.main_Window import Ui_MainWindow as Ui_MainWindow_1
from QtDesign.connecting_Dialog import Ui_Dialog as Ui_ConnectingDialog
from QtDesign.aboutUs_Dialog import Ui_Dialog as Ui_AboutUsDialog
from QtDesign.settings_Dialog import Ui_Dialog as Ui_SettingsDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)

        for message in savedData["messages"]:
            self.ui.cb_Messages.addItem(f"{message[0]} {message[1]}")
        self.ui.kse_Key.setKeySequence(savedData["key"])

        self.ui.pb_ChangeStatus.clicked.connect(self.openConnectingDialog)
        self.ui.pb_AddMessage.clicked.connect(self.addMessage)
        self.ui.pb_RemoveMessage.clicked.connect(self.removeMessage)

        self.ui.cb_Messages.textActivated.connect(self.pasteMessageFromComboBox)

        self.ui.pb_SendMessages.clicked.connect(self.sendMessage)
        self.ui.kse_Key.keySequenceChanged.connect(self.changeKey)
        self.ui.le_MessagePrefix.textChanged.connect(self.prefixMessageChangeSize)
        self.ui.le_MessagePrefix.setStatusTip(
            f"{self.ui.le_MessagePrefix.width()},{self.ui.le_MessagePrefix.height()}"
        )

        self.ui.actionSettings.triggered.connect(self.openSettingsDialog)
        self.ui.actionAbout_as.triggered.connect(self.openAboutUsDialog)
        self.ui.actionExit.triggered.connect(self.close)

    def prefixMessageChangeSize(self) -> None:
        if self.ui.le_MessagePrefix.text() != "":
            fm = QFontMetrics(self.ui.le_MessagePrefix.font())
            textSize = fm.size(0, self.ui.le_MessagePrefix.text())
            self.ui.le_MessagePrefix.setFixedSize(
                textSize.width() + 40, self.ui.le_MessagePrefix.height()
            )
        else:
            size = self.ui.le_MessagePrefix.statusTip().split(",")
            self.ui.le_MessagePrefix.setFixedSize(int(size[0]), int(size[1]))

    def openConnectingDialog(self) -> None:
        connectingDialog.show()

    def openAboutUsDialog(self) -> None:
        aboutUsDialog.show()

    def openSettingsDialog(self) -> None:
        settingsDialog.show()

    def disconnect(self) -> None:
        connectionClient.disconnect()
        self.changeStatus()

    def addMessage(self) -> None:
        prefix = self.ui.le_MessagePrefix.text()
        text = self.ui.le_Message.text()
        if text != "" and [prefix, text] not in savedData["messages"]:
            savedData["messages"].append([prefix, text])
            self.ui.cb_Messages.addItem(f"{prefix} {text}")
            save("saved_data.json", savedData)

    def removeMessage(self) -> None:
        prefix = self.ui.le_MessagePrefix.text()
        text = self.ui.le_Message.text()
        if [prefix, text] in savedData["messages"]:
            self.ui.cb_Messages.removeItem(savedData["messages"].index([prefix, text]))
            savedData["messages"].remove([prefix, text])
            save("saved_data.json", savedData)

    def pasteMessageFromComboBox(self) -> None:
        prefix = savedData["messages"][self.ui.cb_Messages.currentIndex()][0]
        text = savedData["messages"][self.ui.cb_Messages.currentIndex()][1]
        self.ui.le_Message.setText(text)
        self.ui.le_MessagePrefix.setText(prefix)

    def changeKey(self) -> None:
        if self.ui.kse_Key.keySequence().toString() == "Return":
            self.ui.kse_Key.setKeySequence("")
            return
        savedData["key"] = self.ui.kse_Key.keySequence().toString()
        save("saved_data.json", savedData)

    def sendMessage(self) -> None:
        if not connectionClient.connected:
            return
        text = f"{self.ui.le_MessagePrefix.text()}{self.ui.le_Message.text()}"
        key = self.ui.kse_Key.keySequence().toString()
        if not (len(key) == 1 and (97 < ord(key) < 122 or 65 < ord(key) < 90)):
            return
        if text == "" or key == "":
            return
        try:
            connectionClient.send_message_in_thread(message_text=text, key_to_print=key)
        except ConnectionResetError:
            self.changeStatus()
        else:
            if settings["clearMessage"]:
                self.ui.le_Message.clear()
            if settings["clearPrefix"]:
                self.ui.le_MessagePrefix.clear()

    def changeStatus(self) -> None:
        if connectionClient.connected:
            self.ui.le_Status1.setText("ONLINE")
            self.ui.pb_ChangeStatus.setText("DISCONNECT")
            self.ui.pb_ChangeStatus.clicked.disconnect(self.openConnectingDialog)
            self.ui.pb_ChangeStatus.clicked.connect(self.disconnect)
        else:
            self.ui.le_Status1.setText("OFFLINE")
            self.ui.pb_ChangeStatus.setText("CONNECT")
            self.ui.pb_ChangeStatus.clicked.disconnect(self.disconnect)
            self.ui.pb_ChangeStatus.clicked.connect(self.openConnectingDialog)


class ConnectingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ConnectingDialog()
        self.ui.setupUi(self)

        self.ui.pb_CancelButton.clicked.connect(lambda: self.close())
        self.ui.pb_ConnectButton.clicked.connect(self.connect)
        if "ip" in savedData.keys() and "port" in savedData.keys():
            self.ui.le_IPLine.setText(savedData["ip"])
            self.ui.le_PortLine.setText(str(savedData["port"]) if savedData["port"] != 0 else "")

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


class AboutUsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutUsDialog()
        self.ui.setupUi(self)


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.ui.chB_clearMessage.setChecked(settings["clearMessage"])
        self.ui.chB_clearPrefix.setChecked(settings["clearPrefix"])

        self.ui.chB_clearMessage.clicked.connect(self.changeSettingClearMessage)
        self.ui.chB_clearPrefix.clicked.connect(self.changeSettingClearPrefix)
        self.ui.pb_accept.clicked.connect(self.acceptSettingsChanges)
        self.ui.pb_ok.clicked.connect(self.close)
        self.ui.pb_cancel.clicked.connect(self.close)

        self.ui.pb_accept.setEnabled(False)

        global newSettings
        newSettings = dict()

    def changeSettingClearMessage(self) -> None:
        newSettings["clearMessage"] = self.ui.chB_clearMessage.isChecked()
        self.changesCheck()

    def changeSettingClearPrefix(self) -> None:
        newSettings["clearPrefix"] = self.ui.chB_clearPrefix.isChecked()
        self.changesCheck()

    def changesCheck(self) -> None:
        for key in settings.keys():
            if key not in newSettings.keys():
                continue
            if settings[key] != newSettings[key]:
                self.ui.pb_accept.setEnabled(True)
                break
        else:
            self.ui.pb_accept.setEnabled(False)

    def acceptSettingsChanges(self) -> None:
        settings.update(newSettings)
        save("settings.json", settings)
        newSettings.clear()
        self.changesCheck()


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
        for i in range(0, len(savedData["messages"])):
            if isinstance(savedData["messages"][i], str):
                savedData["messages"][i] = ["", savedData["messages"][i]]
    save("saved_data.json", savedData)

    settings = {"clearMessage": True, "clearPrefix": True, "language": "ru", "theme": "system"}
    if os.path.isfile("settings.json"):
        settings.update(load("settings.json"))
    save("settings.json", settings)

    mainWindow = MainWindow()
    connectingDialog = ConnectingDialog(mainWindow)
    aboutUsDialog = AboutUsDialog(mainWindow)
    settingsDialog = SettingsDialog(mainWindow)

    mainWindow.show()

    sys.exit(app.exec())
