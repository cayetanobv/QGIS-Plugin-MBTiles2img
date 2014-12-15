# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mbtiles2img_dialog_base.ui'
#
# Created: Mon Dec 15 01:21:13 2014
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
        MBTiles2imgDialogBase.resize(322, 210)
        MBTiles2imgDialogBase.setMinimumSize(QtCore.QSize(300, 210))
        MBTiles2imgDialogBase.setMaximumSize(QtCore.QSize(800, 211))
        self.verticalLayout = QtGui.QVBoxLayout(MBTiles2imgDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.selectDestFolderButton = QtGui.QPushButton(MBTiles2imgDialogBase)
        self.selectDestFolderButton.setObjectName(_fromUtf8("selectDestFolderButton"))
        self.gridLayout.addWidget(self.selectDestFolderButton, 2, 0, 1, 1)
        self.loadFileButton = QtGui.QPushButton(MBTiles2imgDialogBase)
        self.loadFileButton.setObjectName(_fromUtf8("loadFileButton"))
        self.gridLayout.addWidget(self.loadFileButton, 0, 0, 1, 1)
        self.labelPathMBTiles = QtGui.QLabel(MBTiles2imgDialogBase)
        self.labelPathMBTiles.setFrameShape(QtGui.QFrame.StyledPanel)
        self.labelPathMBTiles.setFrameShadow(QtGui.QFrame.Raised)
        self.labelPathMBTiles.setScaledContents(True)
        self.labelPathMBTiles.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathMBTiles.setObjectName(_fromUtf8("labelPathMBTiles"))
        self.gridLayout.addWidget(self.labelPathMBTiles, 1, 0, 1, 1)
        self.labelPathDestFolder = QtGui.QLabel(MBTiles2imgDialogBase)
        self.labelPathDestFolder.setFrameShape(QtGui.QFrame.StyledPanel)
        self.labelPathDestFolder.setFrameShadow(QtGui.QFrame.Raised)
        self.labelPathDestFolder.setScaledContents(True)
        self.labelPathDestFolder.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathDestFolder.setObjectName(_fromUtf8("labelPathDestFolder"))
        self.gridLayout.addWidget(self.labelPathDestFolder, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.button_box = QtGui.QDialogButtonBox(MBTiles2imgDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(MBTiles2imgDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), MBTiles2imgDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), MBTiles2imgDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MBTiles2imgDialogBase)

    def retranslateUi(self, MBTiles2imgDialogBase):
        MBTiles2imgDialogBase.setWindowTitle(_translate("MBTiles2imgDialogBase", "MBTiles images extract", None))
        self.selectDestFolderButton.setText(_translate("MBTiles2imgDialogBase", "Select folder to save images", None))
        self.loadFileButton.setText(_translate("MBTiles2imgDialogBase", "Load MBTiles file", None))
        self.labelPathMBTiles.setText(_translate("MBTiles2imgDialogBase", "MBTiles to extract...", None))
        self.labelPathDestFolder.setText(_translate("MBTiles2imgDialogBase", "Destination folder...", None))

