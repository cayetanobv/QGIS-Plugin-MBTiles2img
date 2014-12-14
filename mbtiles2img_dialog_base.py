# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mbtiles2img_dialog_base.ui'
#
# Created: Sun Dec 14 22:00:04 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MBTiles2imgDialogBase(object):
    def setupUi(self, MBTiles2imgDialogBase):
        MBTiles2imgDialogBase.setObjectName(_fromUtf8("MBTiles2imgDialogBase"))
        MBTiles2imgDialogBase.resize(264, 222)
        self.button_box = QtGui.QDialogButtonBox(MBTiles2imgDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 170, 221, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.widget = QtGui.QWidget(MBTiles2imgDialogBase)
        self.widget.setGeometry(QtCore.QRect(10, 20, 241, 141))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.loadFileButton = QtGui.QPushButton(self.widget)
        self.loadFileButton.setObjectName(_fromUtf8("loadFileButton"))
        self.verticalLayout.addWidget(self.loadFileButton)
        self.labelPathMBTiles = QtGui.QLabel(self.widget)
        self.labelPathMBTiles.setFrameShape(QtGui.QFrame.StyledPanel)
        self.labelPathMBTiles.setFrameShadow(QtGui.QFrame.Plain)
        self.labelPathMBTiles.setScaledContents(True)
        self.labelPathMBTiles.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathMBTiles.setObjectName(_fromUtf8("labelPathMBTiles"))
        self.verticalLayout.addWidget(self.labelPathMBTiles)
        self.selectDestFolderButton = QtGui.QPushButton(self.widget)
        self.selectDestFolderButton.setObjectName(_fromUtf8("selectDestFolderButton"))
        self.verticalLayout.addWidget(self.selectDestFolderButton)
        self.labelPathDestFolder = QtGui.QLabel(self.widget)
        self.labelPathDestFolder.setFrameShape(QtGui.QFrame.StyledPanel)
        self.labelPathDestFolder.setFrameShadow(QtGui.QFrame.Plain)
        self.labelPathDestFolder.setScaledContents(True)
        self.labelPathDestFolder.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathDestFolder.setObjectName(_fromUtf8("labelPathDestFolder"))
        self.verticalLayout.addWidget(self.labelPathDestFolder)

        self.retranslateUi(MBTiles2imgDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), MBTiles2imgDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), MBTiles2imgDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MBTiles2imgDialogBase)

    def retranslateUi(self, MBTiles2imgDialogBase):
        MBTiles2imgDialogBase.setWindowTitle(_translate("MBTiles2imgDialogBase", "MBTiles images export", None))
        self.loadFileButton.setText(_translate("MBTiles2imgDialogBase", "Load MBTiles file", None))
        self.labelPathMBTiles.setText(_translate("MBTiles2imgDialogBase", "MBTiles to extract...", None))
        self.selectDestFolderButton.setText(_translate("MBTiles2imgDialogBase", "Select folder to save images", None))
        self.labelPathDestFolder.setText(_translate("MBTiles2imgDialogBase", "Destination folder...", None))

