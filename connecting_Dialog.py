# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connecting_Dialog.ui'
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
    QDialog,
    QFrame,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        Dialog.resize(500, 200)
        Dialog.setMinimumSize(QSize(500, 200))
        Dialog.setMaximumSize(QSize(500, 208))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.hl_First = QHBoxLayout()
        self.hl_First.setSpacing(0)
        self.hl_First.setObjectName("hl_First")
        self.hl_First.setContentsMargins(10, 10, 10, 10)
        self.le_NameIPLine = QLineEdit(Dialog)
        self.le_NameIPLine.setObjectName("le_NameIPLine")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.le_NameIPLine.sizePolicy().hasHeightForWidth()
        )
        self.le_NameIPLine.setSizePolicy(sizePolicy)
        self.le_NameIPLine.setMinimumSize(QSize(50, 40))
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

        self.le_IPLine = QLineEdit(Dialog)
        self.le_IPLine.setObjectName("le_IPLine")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_IPLine.sizePolicy().hasHeightForWidth())
        self.le_IPLine.setSizePolicy(sizePolicy1)
        self.le_IPLine.setMinimumSize(QSize(400, 40))
        self.le_IPLine.setFont(font)
        self.le_IPLine.setClearButtonEnabled(True)

        self.hl_First.addWidget(self.le_IPLine)

        self.verticalLayout.addLayout(self.hl_First)

        self.hl_Second = QHBoxLayout()
        self.hl_Second.setSpacing(0)
        self.hl_Second.setObjectName("hl_Second")
        self.hl_Second.setContentsMargins(10, 10, 10, 10)
        self.le_NamePortLine = QLineEdit(Dialog)
        self.le_NamePortLine.setObjectName("le_NamePortLine")
        sizePolicy.setHeightForWidth(
            self.le_NamePortLine.sizePolicy().hasHeightForWidth()
        )
        self.le_NamePortLine.setSizePolicy(sizePolicy)
        self.le_NamePortLine.setMinimumSize(QSize(50, 40))
        self.le_NamePortLine.setFont(font)
        self.le_NamePortLine.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.le_NamePortLine.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.le_NamePortLine.setReadOnly(True)

        self.hl_Second.addWidget(self.le_NamePortLine)

        self.le_PortLine = QLineEdit(Dialog)
        self.le_PortLine.setObjectName("le_PortLine")
        sizePolicy1.setHeightForWidth(self.le_PortLine.sizePolicy().hasHeightForWidth())
        self.le_PortLine.setSizePolicy(sizePolicy1)
        self.le_PortLine.setMinimumSize(QSize(400, 40))
        self.le_PortLine.setFont(font)
        self.le_PortLine.setClearButtonEnabled(True)

        self.hl_Second.addWidget(self.le_PortLine)

        self.verticalLayout.addLayout(self.hl_Second)

        self.line = QFrame(Dialog)
        self.line.setObjectName("line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.hl_Third = QHBoxLayout()
        self.hl_Third.setSpacing(0)
        self.hl_Third.setObjectName("hl_Third")
        self.hl_Third.setContentsMargins(10, 10, 10, 10)
        self.pb_ConnectButton = QPushButton(Dialog)
        self.pb_ConnectButton.setObjectName("pb_ConnectButton")
        sizePolicy.setHeightForWidth(
            self.pb_ConnectButton.sizePolicy().hasHeightForWidth()
        )
        self.pb_ConnectButton.setSizePolicy(sizePolicy)
        self.pb_ConnectButton.setMinimumSize(QSize(150, 40))
        self.pb_ConnectButton.setFont(font)
        self.pb_ConnectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hl_Third.addWidget(self.pb_ConnectButton)

        self.hs_1 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.hl_Third.addItem(self.hs_1)

        self.pb_CancelButton = QPushButton(Dialog)
        self.pb_CancelButton.setObjectName("pb_CancelButton")
        sizePolicy.setHeightForWidth(
            self.pb_CancelButton.sizePolicy().hasHeightForWidth()
        )
        self.pb_CancelButton.setSizePolicy(sizePolicy)
        self.pb_CancelButton.setMinimumSize(QSize(150, 40))
        self.pb_CancelButton.setFont(font)
        self.pb_CancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hl_Third.addWidget(self.pb_CancelButton)

        self.verticalLayout.addLayout(self.hl_Third)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Connect", None))
        self.le_NameIPLine.setText(QCoreApplication.translate("Dialog", "ip:", None))
        self.le_NamePortLine.setText(
            QCoreApplication.translate("Dialog", "port:", None)
        )
        self.pb_ConnectButton.setText(
            QCoreApplication.translate("Dialog", "CONNECT", None)
        )
        self.pb_CancelButton.setText(
            QCoreApplication.translate("Dialog", "CANCEL", None)
        )

    # retranslateUi
