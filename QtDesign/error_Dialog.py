# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(500, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 130))
        icon = QIcon()
        icon.addFile("./QtDesign/resources/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        font = QFont()
        font.setFamilies(["Roboto"])
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.hl_1 = QHBoxLayout()
        self.hl_1.setSpacing(25)
        self.hl_1.setObjectName("hl_1")
        self.hl_1.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.vl_1 = QVBoxLayout()
        self.vl_1.setObjectName("vl_1")
        self.l_errorImage = QLabel(Dialog)
        self.l_errorImage.setObjectName("l_errorImage")
        sizePolicy.setHeightForWidth(self.l_errorImage.sizePolicy().hasHeightForWidth())
        self.l_errorImage.setSizePolicy(sizePolicy)
        self.l_errorImage.setMinimumSize(QSize(64, 64))
        self.l_errorImage.setMaximumSize(QSize(64, 64))
        self.l_errorImage.setPixmap(QPixmap("./QtDesign/resources/errorImage.png"))

        self.vl_1.addWidget(self.l_errorImage)

        self.vs_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_1.addItem(self.vs_1)

        self.hl_1.addLayout(self.vl_1)

        self.l_errorText = QLabel(Dialog)
        self.l_errorText.setObjectName("l_errorText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_errorText.sizePolicy().hasHeightForWidth())
        self.l_errorText.setSizePolicy(sizePolicy1)
        self.l_errorText.setMinimumSize(QSize(404, 24))
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        font1.setPointSize(15)
        self.l_errorText.setFont(font1)
        self.l_errorText.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.hl_1.addWidget(self.l_errorText)

        self.verticalLayout.addLayout(self.hl_1)

        self.hl_2 = QHBoxLayout()
        self.hl_2.setSpacing(0)
        self.hl_2.setObjectName("hl_2")
        self.hl_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_2.addItem(self.hs_2)

        self.pb_ok = QPushButton(Dialog)
        self.pb_ok.setObjectName("pb_ok")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_ok.sizePolicy().hasHeightForWidth())
        self.pb_ok.setSizePolicy(sizePolicy2)
        self.pb_ok.setMinimumSize(QSize(75, 32))
        self.pb_ok.setMaximumSize(QSize(75, 32))
        self.pb_ok.setFont(font1)

        self.hl_2.addWidget(self.pb_ok)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_2.addItem(self.hs_1)

        self.verticalLayout.addLayout(self.hl_2)

        self.retranslateUi(Dialog)
        self.pb_ok.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Error", None))
        self.l_errorImage.setText("")
        self.l_errorText.setText(
            QCoreApplication.translate(
                "Dialog",
                "UNKNOWN ERROR!",
                None,
            )
        )
        self.pb_ok.setText(QCoreApplication.translate("Dialog", "OK", None))

    # retranslateUi
