# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QKeySequenceEdit,
    QLineEdit,
    QMainWindow,
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
        MainWindow.resize(745, 316)
        icon = QIcon()
        icon.addFile(":/icon/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        MainWindow.setIconSize(QSize(32, 32))
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.markup = QWidget(MainWindow)
        self.markup.setObjectName("markup")
        self.verticalLayout = QVBoxLayout(self.markup)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setSpacing(0)
        self.hLayout_1.setObjectName("hLayout_1")
        self.hLayout_1.setContentsMargins(10, 10, 10, 10)
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
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.le_Status0.setFont(font)
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
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.le_Status1.setFont(font1)
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
        sizePolicy1.setHeightForWidth(
            self.pb_ChangeStatus.sizePolicy().hasHeightForWidth()
        )
        self.pb_ChangeStatus.setSizePolicy(sizePolicy1)
        self.pb_ChangeStatus.setMinimumSize(QSize(300, 40))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setItalic(False)
        self.pb_ChangeStatus.setFont(font2)
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
        self.hLayout_2.setContentsMargins(10, 10, 10, 10)
        self.le_Message = QLineEdit(self.markup)
        self.le_Message.setObjectName("le_Message")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_Message.sizePolicy().hasHeightForWidth())
        self.le_Message.setSizePolicy(sizePolicy2)
        self.le_Message.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.le_Message.setFont(font3)
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
        self.hLayout_3.setContentsMargins(10, 10, 10, 10)
        self.cb_Messages = QComboBox(self.markup)
        self.cb_Messages.setObjectName("cb_Messages")
        sizePolicy.setHeightForWidth(self.cb_Messages.sizePolicy().hasHeightForWidth())
        self.cb_Messages.setSizePolicy(sizePolicy)
        self.cb_Messages.setMinimumSize(QSize(300, 40))
        self.cb_Messages.setMaximumSize(QSize(300, 16777215))
        font4 = QFont()
        font4.setPointSize(15)
        self.cb_Messages.setFont(font4)
        self.cb_Messages.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.cb_Messages.setAutoFillBackground(False)
        self.cb_Messages.setEditable(False)
        self.cb_Messages.setMaxVisibleItems(3)
        self.cb_Messages.setMaxCount(32)
        self.cb_Messages.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.cb_Messages.setSizeAdjustPolicy(
            QComboBox.SizeAdjustPolicy.AdjustToContents
        )
        self.cb_Messages.setMinimumContentsLength(32)
        self.cb_Messages.setFrame(False)

        self.hLayout_3.addWidget(self.cb_Messages)

        self.hs_2 = QSpacerItem(
            25, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.hLayout_3.addItem(self.hs_2)

        self.kse_Key = QKeySequenceEdit(self.markup)
        self.kse_Key.setObjectName("kse_Key")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.kse_Key.sizePolicy().hasHeightForWidth())
        self.kse_Key.setSizePolicy(sizePolicy3)
        self.kse_Key.setMinimumSize(QSize(125, 40))
        self.kse_Key.setMaximumSize(QSize(310, 16777215))
        self.kse_Key.setFont(font4)
        self.kse_Key.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.kse_Key.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.kse_Key.setAutoFillBackground(False)
        self.kse_Key.setClearButtonEnabled(False)
        self.kse_Key.setMaximumSequenceLength(1)

        self.hLayout_3.addWidget(self.kse_Key)

        self.hs_3 = QSpacerItem(
            25, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.hLayout_3.addItem(self.hs_3)

        self.pb_SendMessages = QPushButton(self.markup)
        self.pb_SendMessages.setObjectName("pb_SendMessages")
        sizePolicy1.setHeightForWidth(
            self.pb_SendMessages.sizePolicy().hasHeightForWidth()
        )
        self.pb_SendMessages.setSizePolicy(sizePolicy1)
        self.pb_SendMessages.setMinimumSize(QSize(100, 40))
        self.pb_SendMessages.setFont(font4)
        self.pb_SendMessages.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_SendMessages.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.hLayout_3.addWidget(self.pb_SendMessages)

        self.verticalLayout.addLayout(self.hLayout_3)

        self.hLayout_4 = QHBoxLayout()
        self.hLayout_4.setSpacing(0)
        self.hLayout_4.setObjectName("hLayout_4")
        self.hLayout_4.setContentsMargins(10, 10, 10, 10)
        self.pb_RemoveMessage = QPushButton(self.markup)
        self.pb_RemoveMessage.setObjectName("pb_RemoveMessage")
        sizePolicy.setHeightForWidth(
            self.pb_RemoveMessage.sizePolicy().hasHeightForWidth()
        )
        self.pb_RemoveMessage.setSizePolicy(sizePolicy)
        self.pb_RemoveMessage.setMinimumSize(QSize(150, 40))
        self.pb_RemoveMessage.setFont(font4)
        self.pb_RemoveMessage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_RemoveMessage.setMouseTracking(True)
        self.pb_RemoveMessage.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.hLayout_4.addWidget(self.pb_RemoveMessage)

        self.pb_AddMessage = QPushButton(self.markup)
        self.pb_AddMessage.setObjectName("pb_AddMessage")
        sizePolicy.setHeightForWidth(
            self.pb_AddMessage.sizePolicy().hasHeightForWidth()
        )
        self.pb_AddMessage.setSizePolicy(sizePolicy)
        self.pb_AddMessage.setMinimumSize(QSize(150, 40))
        self.pb_AddMessage.setFont(font4)
        self.pb_AddMessage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_AddMessage.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.hLayout_4.addWidget(self.pb_AddMessage)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.hLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.hLayout_4)

        self.verticalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.markup)
        QWidget.setTabOrder(self.pb_ChangeStatus, self.le_Message)
        QWidget.setTabOrder(self.le_Message, self.pb_SendMessages)

        self.retranslateUi(MainWindow)
        self.pb_SendMessages.clicked.connect(self.le_Message.clear)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "SpaceStation SHIZA", None)
        )
        self.le_Status0.setText(
            QCoreApplication.translate("MainWindow", "STATUS:", None)
        )
        self.le_Status1.setText(
            QCoreApplication.translate("MainWindow", "OFFLINE", None)
        )
        self.pb_ChangeStatus.setText(
            QCoreApplication.translate("MainWindow", "CONNECT", None)
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
        self.pb_SendMessages.setText(
            QCoreApplication.translate("MainWindow", "SEND", None)
        )
        # if QT_CONFIG(shortcut)
        self.pb_SendMessages.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.pb_RemoveMessage.setText(
            QCoreApplication.translate("MainWindow", "REMOVE", None)
        )
        self.pb_AddMessage.setText(
            QCoreApplication.translate("MainWindow", "ADD", None)
        )

    # retranslateUi
