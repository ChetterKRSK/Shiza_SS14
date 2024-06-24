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
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 311)
        MainWindow.setStyleSheet(
            "QLineEdit#le_Status0 {\n"
            "    padding-right: 10%;\n"
            "    padding-left: 10%;\n"
            "    border: 2px solid #eaeaea;\n"
            "    border-right: 1px solid #eaeaea;\n"
            "    border-top-left-radius: 10%;\n"
            "    border-bottom-left-radius: 10%;\n"
            "}\n"
            "\n"
            "QLineEdit#le_Status1 {\n"
            "    padding-right: 10%;\n"
            "    padding-left: 10%;\n"
            "    border: 2px solid #eaeaea;\n"
            "    border-left: 1px solid #eaeaea;\n"
            "    border-top-right-radius: 10%;\n"
            "    border-bottom-right-radius: 10%;\n"
            "}"
        )
        self.markup = QWidget(MainWindow)
        self.markup.setObjectName("markup")
        self.verticalLayout = QVBoxLayout(self.markup)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.upperLayout = QHBoxLayout()
        self.upperLayout.setSpacing(0)
        self.upperLayout.setObjectName("upperLayout")
        self.upperLayout.setContentsMargins(10, 10, 10, 10)
        self.le_Status0 = QLineEdit(self.markup)
        self.le_Status0.setObjectName("le_Status0")
        self.le_Status0.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Status0.sizePolicy().hasHeightForWidth())
        self.le_Status0.setSizePolicy(sizePolicy)
        self.le_Status0.setMinimumSize(QSize(100, 30))
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

        self.upperLayout.addWidget(self.le_Status0)

        self.le_Status1 = QLineEdit(self.markup)
        self.le_Status1.setObjectName("le_Status1")
        sizePolicy.setHeightForWidth(self.le_Status1.sizePolicy().hasHeightForWidth())
        self.le_Status1.setSizePolicy(sizePolicy)
        self.le_Status1.setMinimumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setWeight(QFont.DemiBold)
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

        self.upperLayout.addWidget(self.le_Status1)

        self.hs_1 = QSpacerItem(
            25, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.upperLayout.addItem(self.hs_1)

        self.pb_ChangeStatus = QPushButton(self.markup)
        self.pb_ChangeStatus.setObjectName("pb_ChangeStatus")
        sizePolicy.setHeightForWidth(
            self.pb_ChangeStatus.sizePolicy().hasHeightForWidth()
        )
        self.pb_ChangeStatus.setSizePolicy(sizePolicy)
        self.pb_ChangeStatus.setMinimumSize(QSize(200, 30))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setItalic(False)
        self.pb_ChangeStatus.setFont(font2)
        self.pb_ChangeStatus.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_ChangeStatus.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.upperLayout.addWidget(self.pb_ChangeStatus)

        self.verticalLayout.addLayout(self.upperLayout)

        self.line = QFrame(self.markup)
        self.line.setObjectName("line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.centerLayout = QHBoxLayout()
        self.centerLayout.setSpacing(0)
        self.centerLayout.setObjectName("centerLayout")
        self.centerLayout.setContentsMargins(10, 10, 10, 10)
        self.le_Message = QLineEdit(self.markup)
        self.le_Message.setObjectName("le_Message")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_Message.sizePolicy().hasHeightForWidth())
        self.le_Message.setSizePolicy(sizePolicy1)
        self.le_Message.setMinimumSize(QSize(0, 150))
        font3 = QFont()
        font3.setPointSize(15)
        self.le_Message.setFont(font3)
        self.le_Message.setMaxLength(250)
        self.le_Message.setCursorPosition(0)
        self.le_Message.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.le_Message.setClearButtonEnabled(True)

        self.centerLayout.addWidget(self.le_Message)

        self.verticalLayout.addLayout(self.centerLayout)

        self.line2 = QFrame(self.markup)
        self.line2.setObjectName("line2")
        self.line2.setFrameShadow(QFrame.Shadow.Raised)
        self.line2.setLineWidth(1)
        self.line2.setMidLineWidth(2)
        self.line2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line2)

        self.downLayout = QHBoxLayout()
        self.downLayout.setSpacing(0)
        self.downLayout.setObjectName("downLayout")
        self.downLayout.setContentsMargins(10, 10, 10, 10)
        self.cb_Messages = QComboBox(self.markup)
        self.cb_Messages.setObjectName("cb_Messages")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_Messages.sizePolicy().hasHeightForWidth())
        self.cb_Messages.setSizePolicy(sizePolicy2)
        self.cb_Messages.setMinimumSize(QSize(300, 30))
        self.cb_Messages.setFont(font3)
        self.cb_Messages.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.downLayout.addWidget(self.cb_Messages)

        self.pb_AddMessages = QPushButton(self.markup)
        self.pb_AddMessages.setObjectName("pb_AddMessages")
        self.pb_AddMessages.setFont(font3)

        self.downLayout.addWidget(self.pb_AddMessages)

        self.hs_2 = QSpacerItem(
            25, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.downLayout.addItem(self.hs_2)

        self.le_NameKey = QLineEdit(self.markup)
        self.le_NameKey.setObjectName("le_NameKey")
        sizePolicy.setHeightForWidth(self.le_NameKey.sizePolicy().hasHeightForWidth())
        self.le_NameKey.setSizePolicy(sizePolicy)
        self.le_NameKey.setMinimumSize(QSize(125, 30))
        self.le_NameKey.setMaximumSize(QSize(125, 16777215))
        self.le_NameKey.setFont(font3)
        self.le_NameKey.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_NameKey.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.le_NameKey.setReadOnly(True)

        self.downLayout.addWidget(self.le_NameKey)

        self.kse_Key = QKeySequenceEdit(self.markup)
        self.kse_Key.setObjectName("kse_Key")
        sizePolicy2.setHeightForWidth(self.kse_Key.sizePolicy().hasHeightForWidth())
        self.kse_Key.setSizePolicy(sizePolicy2)
        self.kse_Key.setMinimumSize(QSize(200, 30))
        font4 = QFont()
        font4.setPointSize(10)
        self.kse_Key.setFont(font4)
        self.kse_Key.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.kse_Key.setClearButtonEnabled(True)
        self.kse_Key.setMaximumSequenceLength(1)

        self.downLayout.addWidget(self.kse_Key)

        self.hs_3 = QSpacerItem(
            25, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.downLayout.addItem(self.hs_3)

        self.pb_SendMessages = QPushButton(self.markup)
        self.pb_SendMessages.setObjectName("pb_SendMessages")
        sizePolicy.setHeightForWidth(
            self.pb_SendMessages.sizePolicy().hasHeightForWidth()
        )
        self.pb_SendMessages.setSizePolicy(sizePolicy)
        self.pb_SendMessages.setMinimumSize(QSize(100, 30))
        self.pb_SendMessages.setFont(font3)
        self.pb_SendMessages.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.downLayout.addWidget(self.pb_SendMessages)

        self.verticalLayout.addLayout(self.downLayout)

        MainWindow.setCentralWidget(self.markup)

        self.retranslateUi(MainWindow)

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
        self.pb_AddMessages.setText(
            QCoreApplication.translate("MainWindow", "ADD", None)
        )
        self.le_NameKey.setText(
            QCoreApplication.translate("MainWindow", "CHAT KEY:", None)
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
# retranslateUi
