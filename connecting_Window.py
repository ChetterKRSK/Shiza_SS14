# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connecting_Window.ui'
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
    QFrame,
    QHBoxLayout,
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
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(500, 200)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 200))
        MainWindow.setMaximumSize(QSize(500, 200))
        self.markup = QWidget(MainWindow)
        self.markup.setObjectName("markup")
        self.markup.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalLayout = QVBoxLayout(self.markup)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.hl_First = QHBoxLayout()
        self.hl_First.setSpacing(0)
        self.hl_First.setObjectName("hl_First")
        self.hl_First.setContentsMargins(10, 10, 10, 10)
        self.le_NameIPLine = QLineEdit(self.markup)
        self.le_NameIPLine.setObjectName("le_NameIPLine")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.le_NameIPLine.sizePolicy().hasHeightForWidth()
        )
        self.le_NameIPLine.setSizePolicy(sizePolicy1)
        self.le_NameIPLine.setMinimumSize(QSize(50, 0))
        font = QFont()
        font.setPointSize(15)
        self.le_NameIPLine.setFont(font)
        self.le_NameIPLine.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_NameIPLine.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.le_NameIPLine.setReadOnly(True)

        self.hl_First.addWidget(self.le_NameIPLine)

        self.le_IPLine = QLineEdit(self.markup)
        self.le_IPLine.setObjectName("le_IPLine")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_IPLine.sizePolicy().hasHeightForWidth())
        self.le_IPLine.setSizePolicy(sizePolicy2)
        self.le_IPLine.setMinimumSize(QSize(400, 0))
        self.le_IPLine.setFont(font)
        self.le_IPLine.setClearButtonEnabled(True)

        self.hl_First.addWidget(self.le_IPLine)

        self.verticalLayout.addLayout(self.hl_First)

        self.hl_Second = QHBoxLayout()
        self.hl_Second.setSpacing(0)
        self.hl_Second.setObjectName("hl_Second")
        self.hl_Second.setContentsMargins(10, 10, 10, 10)
        self.le_NamePortLine = QLineEdit(self.markup)
        self.le_NamePortLine.setObjectName("le_NamePortLine")
        sizePolicy1.setHeightForWidth(
            self.le_NamePortLine.sizePolicy().hasHeightForWidth()
        )
        self.le_NamePortLine.setSizePolicy(sizePolicy1)
        self.le_NamePortLine.setMinimumSize(QSize(50, 0))
        self.le_NamePortLine.setFont(font)
        self.le_NamePortLine.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_NamePortLine.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.le_NamePortLine.setReadOnly(True)

        self.hl_Second.addWidget(self.le_NamePortLine)

        self.le_PortLine = QLineEdit(self.markup)
        self.le_PortLine.setObjectName("le_PortLine")
        sizePolicy2.setHeightForWidth(self.le_PortLine.sizePolicy().hasHeightForWidth())
        self.le_PortLine.setSizePolicy(sizePolicy2)
        self.le_PortLine.setMinimumSize(QSize(400, 0))
        self.le_PortLine.setFont(font)
        self.le_PortLine.setClearButtonEnabled(True)

        self.hl_Second.addWidget(self.le_PortLine)

        self.verticalLayout.addLayout(self.hl_Second)

        self.line = QFrame(self.markup)
        self.line.setObjectName("line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.hl_Third = QHBoxLayout()
        self.hl_Third.setSpacing(0)
        self.hl_Third.setObjectName("hl_Third")
        self.hl_Third.setContentsMargins(10, 10, 10, 10)
        self.pb_ConnectButton = QPushButton(self.markup)
        self.pb_ConnectButton.setObjectName("pb_ConnectButton")
        sizePolicy1.setHeightForWidth(
            self.pb_ConnectButton.sizePolicy().hasHeightForWidth()
        )
        self.pb_ConnectButton.setSizePolicy(sizePolicy1)
        self.pb_ConnectButton.setMinimumSize(QSize(150, 0))
        self.pb_ConnectButton.setFont(font)
        self.pb_ConnectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hl_Third.addWidget(self.pb_ConnectButton)

        self.hs_1 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.hl_Third.addItem(self.hs_1)

        self.pb_CancelButton = QPushButton(self.markup)
        self.pb_CancelButton.setObjectName("pb_CancelButton")
        sizePolicy1.setHeightForWidth(
            self.pb_CancelButton.sizePolicy().hasHeightForWidth()
        )
        self.pb_CancelButton.setSizePolicy(sizePolicy1)
        self.pb_CancelButton.setMinimumSize(QSize(150, 0))
        self.pb_CancelButton.setFont(font)
        self.pb_CancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hl_Third.addWidget(self.pb_CancelButton)

        self.verticalLayout.addLayout(self.hl_Third)

        MainWindow.setCentralWidget(self.markup)
        QWidget.setTabOrder(self.le_IPLine, self.le_PortLine)
        QWidget.setTabOrder(self.le_PortLine, self.pb_ConnectButton)
        QWidget.setTabOrder(self.pb_ConnectButton, self.pb_CancelButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Connecting", None)
        )
        self.le_NameIPLine.setText(
            QCoreApplication.translate("MainWindow", "ip:", None)
        )
        self.le_NamePortLine.setText(
            QCoreApplication.translate("MainWindow", "port:", None)
        )
        self.pb_ConnectButton.setText(
            QCoreApplication.translate("MainWindow", "CONNECT", None)
        )
        self.pb_CancelButton.setText(
            QCoreApplication.translate("MainWindow", "CANCEL", None)
        )

    # retranslateUi
