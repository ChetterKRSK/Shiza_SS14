# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QCursor, QFont, QIcon
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QHBoxLayout,
    QKeySequenceEdit,
    QLineEdit,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 300)
        MainWindow.setMinimumSize(QSize(1000, 300))
        MainWindow.setWindowTitle("SpaceStation SHIZA")
        icon = QIcon()
        icon.addFile(":/icon/resources/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "QLineEdit {\n"
            "    padding-right: 10%;\n"
            "    padding-left: 10%;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    padding-left: 10%;\n"
            "    padding-right: 10%;\n"
            "}"
        )
        MainWindow.setIconSize(QSize(64, 64))
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        font = QFont()
        font.setFamilies(["Roboto"])
        self.actionSettings.setFont(font)
        self.actionSettings.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAbout_as = QAction(MainWindow)
        self.actionAbout_as.setObjectName("actionAbout_as")
        self.actionAbout_as.setFont(font)
        self.actionAbout_as.setMenuRole(QAction.MenuRole.NoRole)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setFont(font)
        self.actionExit.setMenuRole(QAction.MenuRole.NoRole)
        self.markup = QWidget(MainWindow)
        self.markup.setObjectName("markup")
        self.verticalLayout = QVBoxLayout(self.markup)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setSpacing(0)
        self.hLayout_1.setObjectName("hLayout_1")
        self.hLayout_1.setContentsMargins(10, 10, 10, 5)
        self.le_Status0 = QLineEdit(self.markup)
        self.le_Status0.setObjectName("le_Status0")
        self.le_Status0.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Status0.sizePolicy().hasHeightForWidth())
        self.le_Status0.setSizePolicy(sizePolicy)
        self.le_Status0.setMinimumSize(QSize(200, 40))
        self.le_Status0.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        font1.setPointSize(15)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.le_Status0.setFont(font1)
        self.le_Status0.setMouseTracking(False)
        self.le_Status0.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_Status0.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.le_Status0.setMaxLength(50)
        self.le_Status0.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.le_Status0.setReadOnly(True)

        self.hLayout_1.addWidget(self.le_Status0)

        self.le_Status1 = QLineEdit(self.markup)
        self.le_Status1.setObjectName("le_Status1")
        sizePolicy.setHeightForWidth(self.le_Status1.sizePolicy().hasHeightForWidth())
        self.le_Status1.setSizePolicy(sizePolicy)
        self.le_Status1.setMinimumSize(QSize(200, 40))
        self.le_Status1.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setFamilies(["Roboto"])
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.le_Status1.setFont(font2)
        self.le_Status1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_Status1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.le_Status1.setMaxLength(50)
        self.le_Status1.setFrame(True)
        self.le_Status1.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.le_Status1.setReadOnly(True)

        self.hLayout_1.addWidget(self.le_Status1)

        self.hs_1 = QSpacerItem(
            25, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.hLayout_1.addItem(self.hs_1)

        self.pb_ChangeStatus = QPushButton(self.markup)
        self.pb_ChangeStatus.setObjectName("pb_ChangeStatus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_ChangeStatus.sizePolicy().hasHeightForWidth())
        self.pb_ChangeStatus.setSizePolicy(sizePolicy1)
        self.pb_ChangeStatus.setMinimumSize(QSize(300, 40))
        font3 = QFont()
        font3.setFamilies(["Roboto"])
        font3.setPointSize(15)
        font3.setItalic(False)
        self.pb_ChangeStatus.setFont(font3)
        self.pb_ChangeStatus.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_ChangeStatus.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.hLayout_1.addWidget(self.pb_ChangeStatus)

        self.verticalLayout.addLayout(self.hLayout_1)

        self.line = QFrame(self.markup)
        self.line.setObjectName("line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.hLayout_2 = QHBoxLayout()
        self.hLayout_2.setSpacing(0)
        self.hLayout_2.setObjectName("hLayout_2")
        self.hLayout_2.setContentsMargins(10, 5, 10, 5)
        self.le_MessagePrefix = QLineEdit(self.markup)
        self.le_MessagePrefix.setObjectName("le_MessagePrefix")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_MessagePrefix.sizePolicy().hasHeightForWidth())
        self.le_MessagePrefix.setSizePolicy(sizePolicy2)
        self.le_MessagePrefix.setMinimumSize(QSize(110, 50))
        self.le_MessagePrefix.setMaximumSize(QSize(110, 16777215))
        font4 = QFont()
        font4.setFamilies(["Roboto"])
        font4.setPointSize(15)
        self.le_MessagePrefix.setFont(font4)
        self.le_MessagePrefix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hLayout_2.addWidget(self.le_MessagePrefix)

        self.le_Message = QLineEdit(self.markup)
        self.le_Message.setObjectName("le_Message")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.le_Message.sizePolicy().hasHeightForWidth())
        self.le_Message.setSizePolicy(sizePolicy3)
        self.le_Message.setMinimumSize(QSize(0, 50))
        font5 = QFont()
        font5.setFamilies(["Roboto"])
        font5.setPointSize(15)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.le_Message.setFont(font5)
        self.le_Message.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.le_Message.setMaxLength(250)
        self.le_Message.setCursorPosition(0)
        self.le_Message.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.le_Message.setClearButtonEnabled(True)

        self.hLayout_2.addWidget(self.le_Message)

        self.verticalLayout.addLayout(self.hLayout_2)

        self.line2 = QFrame(self.markup)
        self.line2.setObjectName("line2")
        self.line2.setFrameShadow(QFrame.Shadow.Raised)
        self.line2.setLineWidth(1)
        self.line2.setMidLineWidth(2)
        self.line2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line2)

        self.hLayout_3 = QHBoxLayout()
        self.hLayout_3.setSpacing(0)
        self.hLayout_3.setObjectName("hLayout_3")
        self.hLayout_3.setContentsMargins(10, 5, 10, 5)
        self.cb_Messages = QComboBox(self.markup)
        self.cb_Messages.setObjectName("cb_Messages")
        sizePolicy.setHeightForWidth(self.cb_Messages.sizePolicy().hasHeightForWidth())
        self.cb_Messages.setSizePolicy(sizePolicy)
        self.cb_Messages.setMinimumSize(QSize(600, 40))
        self.cb_Messages.setMaximumSize(QSize(600, 16777215))
        self.cb_Messages.setFont(font4)
        self.cb_Messages.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.cb_Messages.setAutoFillBackground(False)
        self.cb_Messages.setEditable(False)
        self.cb_Messages.setMaxVisibleItems(3)
        self.cb_Messages.setMaxCount(32)
        self.cb_Messages.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.cb_Messages.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.cb_Messages.setMinimumContentsLength(32)
        self.cb_Messages.setFrame(False)

        self.hLayout_3.addWidget(self.cb_Messages)

        self.hs_2 = QSpacerItem(25, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_3.addItem(self.hs_2)

        self.kse_Key = QKeySequenceEdit(self.markup)
        self.kse_Key.setObjectName("kse_Key")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.kse_Key.sizePolicy().hasHeightForWidth())
        self.kse_Key.setSizePolicy(sizePolicy4)
        self.kse_Key.setMinimumSize(QSize(125, 40))
        self.kse_Key.setMaximumSize(QSize(310, 16777215))
        self.kse_Key.setFont(font4)
        self.kse_Key.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.kse_Key.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.kse_Key.setAutoFillBackground(False)
        self.kse_Key.setClearButtonEnabled(False)
        self.kse_Key.setMaximumSequenceLength(1)

        self.hLayout_3.addWidget(self.kse_Key)

        self.hs_3 = QSpacerItem(25, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_3.addItem(self.hs_3)

        self.pb_SendMessages = QPushButton(self.markup)
        self.pb_SendMessages.setObjectName("pb_SendMessages")
        sizePolicy1.setHeightForWidth(self.pb_SendMessages.sizePolicy().hasHeightForWidth())
        self.pb_SendMessages.setSizePolicy(sizePolicy1)
        self.pb_SendMessages.setMinimumSize(QSize(100, 40))
        self.pb_SendMessages.setFont(font4)
        self.pb_SendMessages.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_SendMessages.setMouseTracking(False)
        self.pb_SendMessages.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.hLayout_3.addWidget(self.pb_SendMessages)

        self.verticalLayout.addLayout(self.hLayout_3)

        self.hLayout_4 = QHBoxLayout()
        self.hLayout_4.setSpacing(0)
        self.hLayout_4.setObjectName("hLayout_4")
        self.hLayout_4.setContentsMargins(10, 5, 10, 10)
        self.pb_RemoveMessage = QPushButton(self.markup)
        self.pb_RemoveMessage.setObjectName("pb_RemoveMessage")
        sizePolicy.setHeightForWidth(self.pb_RemoveMessage.sizePolicy().hasHeightForWidth())
        self.pb_RemoveMessage.setSizePolicy(sizePolicy)
        self.pb_RemoveMessage.setMinimumSize(QSize(200, 40))
        self.pb_RemoveMessage.setMaximumSize(QSize(250, 16777215))
        self.pb_RemoveMessage.setFont(font4)
        self.pb_RemoveMessage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_RemoveMessage.setMouseTracking(False)
        self.pb_RemoveMessage.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.hLayout_4.addWidget(self.pb_RemoveMessage)

        self.horizontalSpacer_2 = QSpacerItem(
            200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.hLayout_4.addItem(self.horizontalSpacer_2)

        self.pb_AddMessage = QPushButton(self.markup)
        self.pb_AddMessage.setObjectName("pb_AddMessage")
        sizePolicy.setHeightForWidth(self.pb_AddMessage.sizePolicy().hasHeightForWidth())
        self.pb_AddMessage.setSizePolicy(sizePolicy)
        self.pb_AddMessage.setMinimumSize(QSize(200, 40))
        self.pb_AddMessage.setMaximumSize(QSize(250, 16777215))
        self.pb_AddMessage.setFont(font4)
        self.pb_AddMessage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_AddMessage.setMouseTracking(False)
        self.pb_AddMessage.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.hLayout_4.addWidget(self.pb_AddMessage)

        self.horizontalSpacer = QSpacerItem(
            200, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.hLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.hLayout_4)

        self.verticalSpacer = QSpacerItem(
            20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.markup)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1000, 24))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setWeight(QFont.DemiBold)
        self.menuBar.setFont(font6)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setEnabled(True)
        self.menuFile.setMinimumSize(QSize(150, 0))
        self.menuFile.setMaximumSize(QSize(150, 16777215))
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setSeparatorsCollapsible(False)
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.pb_ChangeStatus, self.le_Message)
        QWidget.setTabOrder(self.le_Message, self.pb_SendMessages)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionAbout_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.le_Message.returnPressed.connect(self.pb_SendMessages.click)
        self.le_MessagePrefix.returnPressed.connect(self.le_Message.setFocus)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", "Settings", None))
        self.actionAbout_as.setText(QCoreApplication.translate("MainWindow", "About as", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.le_Status0.setText(QCoreApplication.translate("MainWindow", "STATUS:", None))
        self.le_Status1.setText(QCoreApplication.translate("MainWindow", "OFFLINE", None))
        self.pb_ChangeStatus.setText(QCoreApplication.translate("MainWindow", "CONNECT", None))
        self.le_MessagePrefix.setText("")
        self.le_MessagePrefix.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u0440\u0435\u0444\u0438\u043a\u0441", None
            )
        )
        self.le_Message.setText("")
        self.le_Message.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u0435\u0434\u0430\u0432\u0430\u0435\u043c\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435.",
                None,
            )
        )
        self.kse_Key.setKeySequence("")
        self.pb_SendMessages.setText(QCoreApplication.translate("MainWindow", "SEND", None))
        self.pb_RemoveMessage.setText(QCoreApplication.translate("MainWindow", "REMOVE", None))
        self.pb_AddMessage.setText(QCoreApplication.translate("MainWindow", "ADD", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "     File     ", None))
        pass

    # retranslateUi
