# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 200))
        Dialog.setMaximumSize(QSize(500, 500))
        font = QFont()
        font.setFamilies(["Roboto"])
        font.setPointSize(15)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(":/icon/resources/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 500, 352))
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_1 = QFrame(self.scrollAreaWidgetContents)
        self.frame_1.setObjectName("frame_1")
        self.frame_1.setMaximumSize(QSize(16777215, 100))
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 25, 0)
        self.l_clearMessageName = QLabel(self.frame_1)
        self.l_clearMessageName.setObjectName("l_clearMessageName")
        self.l_clearMessageName.setMinimumSize(QSize(0, 40))
        self.l_clearMessageName.setFont(font)

        self.horizontalLayout.addWidget(self.l_clearMessageName)

        self.chB_clearMessage = QCheckBox(self.frame_1)
        self.chB_clearMessage.setObjectName("chB_clearMessage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chB_clearMessage.sizePolicy().hasHeightForWidth())
        self.chB_clearMessage.setSizePolicy(sizePolicy2)
        self.chB_clearMessage.setMinimumSize(QSize(0, 40))
        self.chB_clearMessage.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.chB_clearMessage.setStyleSheet("QCheckBox::indicator {width: 20px;height: 20px;}")
        self.chB_clearMessage.setChecked(False)
        self.chB_clearMessage.setTristate(False)

        self.horizontalLayout.addWidget(self.chB_clearMessage)

        self.verticalLayout_2.addWidget(self.frame_1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 25, 0)
        self.l_clearMessage = QLabel(self.frame_2)
        self.l_clearMessage.setObjectName("l_clearMessage")
        self.l_clearMessage.setMinimumSize(QSize(0, 40))
        self.l_clearMessage.setFont(font)

        self.horizontalLayout_5.addWidget(self.l_clearMessage)

        self.chB_clearPrefix = QCheckBox(self.frame_2)
        self.chB_clearPrefix.setObjectName("chB_clearPrefix")
        sizePolicy2.setHeightForWidth(self.chB_clearPrefix.sizePolicy().hasHeightForWidth())
        self.chB_clearPrefix.setSizePolicy(sizePolicy2)
        self.chB_clearPrefix.setMinimumSize(QSize(0, 40))
        self.chB_clearPrefix.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.chB_clearPrefix.setStyleSheet("QCheckBox::indicator {width: 20px;height: 20px;}")
        self.chB_clearPrefix.setChecked(False)
        self.chB_clearPrefix.setTristate(False)

        self.horizontalLayout_5.addWidget(self.chB_clearPrefix)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 25, 0)
        self.l_languageName = QLabel(self.frame_3)
        self.l_languageName.setObjectName("l_languageName")
        self.l_languageName.setMinimumSize(QSize(0, 40))
        self.l_languageName.setFont(font)

        self.horizontalLayout_2.addWidget(self.l_languageName)

        self.cb_language = QComboBox(self.frame_3)
        self.cb_language.setObjectName("cb_language")
        sizePolicy2.setHeightForWidth(self.cb_language.sizePolicy().hasHeightForWidth())
        self.cb_language.setSizePolicy(sizePolicy2)
        self.cb_language.setMinimumSize(QSize(0, 40))
        self.cb_language.setFont(font)
        self.cb_language.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_2.addWidget(self.cb_language)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 25, 0)
        self.l_themeName = QLabel(self.frame_4)
        self.l_themeName.setObjectName("l_themeName")
        self.l_themeName.setMinimumSize(QSize(0, 40))
        self.l_themeName.setFont(font)

        self.horizontalLayout_3.addWidget(self.l_themeName)

        self.cb_theme = QComboBox(self.frame_4)
        self.cb_theme.setObjectName("cb_theme")
        sizePolicy2.setHeightForWidth(self.cb_theme.sizePolicy().hasHeightForWidth())
        self.cb_theme.setSizePolicy(sizePolicy2)
        self.cb_theme.setMinimumSize(QSize(0, 40))
        self.cb_theme.setFont(font)
        self.cb_theme.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_3.addWidget(self.cb_theme)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.hl_downButtons = QHBoxLayout()
        self.hl_downButtons.setSpacing(10)
        self.hl_downButtons.setObjectName("hl_downButtons")
        self.hl_downButtons.setContentsMargins(0, -1, 10, -1)
        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_downButtons.addItem(self.hs_1)

        self.pb_ok = QPushButton(Dialog)
        self.pb_ok.setObjectName("pb_ok")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_ok.sizePolicy().hasHeightForWidth())
        self.pb_ok.setSizePolicy(sizePolicy3)
        self.pb_ok.setMinimumSize(QSize(120, 40))
        self.pb_ok.setMaximumSize(QSize(16777215, 16777215))
        self.pb_ok.setFont(font)
        self.pb_ok.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.hl_downButtons.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(Dialog)
        self.pb_cancel.setObjectName("pb_cancel")
        sizePolicy3.setHeightForWidth(self.pb_cancel.sizePolicy().hasHeightForWidth())
        self.pb_cancel.setSizePolicy(sizePolicy3)
        self.pb_cancel.setMinimumSize(QSize(120, 40))
        self.pb_cancel.setMaximumSize(QSize(16777215, 16777215))
        self.pb_cancel.setFont(font)
        self.pb_cancel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.hl_downButtons.addWidget(self.pb_cancel)

        self.pb_accept = QPushButton(Dialog)
        self.pb_accept.setObjectName("pb_accept")
        sizePolicy3.setHeightForWidth(self.pb_accept.sizePolicy().hasHeightForWidth())
        self.pb_accept.setSizePolicy(sizePolicy3)
        self.pb_accept.setMinimumSize(QSize(120, 40))
        self.pb_accept.setMaximumSize(QSize(16777215, 16777215))
        self.pb_accept.setFont(font)
        self.pb_accept.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.hl_downButtons.addWidget(self.pb_accept)

        self.verticalLayout.addLayout(self.hl_downButtons)

        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)
        QWidget.setTabOrder(self.pb_cancel, self.pb_accept)
        QWidget.setTabOrder(self.pb_accept, self.scrollArea)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Settings", None))
        self.l_clearMessageName.setText(
            QCoreApplication.translate("Dialog", "Clear message after send", None)
        )
        self.l_clearMessage.setText(
            QCoreApplication.translate("Dialog", "Clear prefix after send", None)
        )
        self.l_languageName.setText(QCoreApplication.translate("Dialog", "Language", None))
        self.l_themeName.setText(QCoreApplication.translate("Dialog", "Theme", None))
        self.pb_ok.setText(QCoreApplication.translate("Dialog", "\u041e\u043a", None))
        self.pb_cancel.setText(
            QCoreApplication.translate("Dialog", "\u041e\u0442\u043c\u0435\u043d\u0430", None)
        )
        self.pb_accept.setText(
            QCoreApplication.translate(
                "Dialog", "\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None
            )
        )

    # retranslateUi
