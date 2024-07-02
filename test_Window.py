# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 250)
        MainWindow.setMinimumSize(QSize(500, 250))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.maket = QWidget(MainWindow)
        self.maket.setObjectName("maket")
        self.verticalLayout = QVBoxLayout(self.maket)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.l_translationImage = QLabel(self.maket)
        self.l_translationImage.setObjectName("l_translationImage")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_translationImage.sizePolicy().hasHeightForWidth())
        self.l_translationImage.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.l_translationImage)

        self.hl_1 = QHBoxLayout()
        self.hl_1.setSpacing(0)
        self.hl_1.setObjectName("hl_1")
        self.horizontalSpacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.hl_1.addItem(self.horizontalSpacer)

        self.cb_keyboardFetch = QCheckBox(self.maket)
        self.cb_keyboardFetch.setObjectName("cb_keyboardFetch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_keyboardFetch.sizePolicy().hasHeightForWidth())
        self.cb_keyboardFetch.setSizePolicy(sizePolicy1)
        self.cb_keyboardFetch.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.hl_1.addWidget(self.cb_keyboardFetch)

        self.horizontalSpacer_2 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.hl_1.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.hl_1)

        MainWindow.setCentralWidget(self.maket)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.l_translationImage.setText("")
        self.cb_keyboardFetch.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0422\u041d\u042f\u0422\u042c \u041a\u041b\u0410\u0412\u0418\u0410\u0422\u0423\u0420\u0423",
                None,
            )
        )

    # retranslateUi
