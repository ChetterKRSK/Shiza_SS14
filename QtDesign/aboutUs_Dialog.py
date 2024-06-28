# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        font = QFont()
        font.setFamilies(["Roboto"])
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(":/icon/resources/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(100, 100))
        self.frame.setFrameShape(QFrame.Shape.Panel)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame.setMidLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hl_1 = QHBoxLayout()
        self.hl_1.setSpacing(0)
        self.hl_1.setObjectName("hl_1")
        self.l_author1 = QLabel(self.frame)
        self.l_author1.setObjectName("l_author1")
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        font1.setPointSize(20)
        self.l_author1.setFont(font1)
        self.l_author1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_1.addWidget(self.l_author1)

        self.hs_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_1.addItem(self.hs_3)

        self.l_author2 = QLabel(self.frame)
        self.l_author2.setObjectName("l_author2")
        self.l_author2.setFont(font1)
        self.l_author2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_1.addWidget(self.l_author2)

        self.verticalLayout.addLayout(self.hl_1)

        self.line = QFrame(self.frame)
        self.line.setObjectName("line")
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.l_companyName = QLabel(self.frame)
        self.l_companyName.setObjectName("l_companyName")
        self.l_companyName.setFont(font1)
        self.l_companyName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.l_companyName)

        self.gridLayout.addWidget(self.frame, 1, 1, 1, 2)

        self.vs_2 = QSpacerItem(50, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.vs_2, 2, 1, 1, 1)

        self.hs_2 = QSpacerItem(50, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.hs_2, 1, 3, 1, 1)

        self.hs_1 = QSpacerItem(50, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.hs_1, 1, 0, 1, 1)

        self.vs_1 = QSpacerItem(50, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.vs_1, 0, 2, 1, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "About Us", None))
        self.l_author1.setText(QCoreApplication.translate("Dialog", "  CHETTER", None))
        self.l_author2.setText(QCoreApplication.translate("Dialog", "BAINAL  ", None))
        self.l_companyName.setText(QCoreApplication.translate("Dialog", "NorthUNIT\u00a9", None))

    # retranslateUi
