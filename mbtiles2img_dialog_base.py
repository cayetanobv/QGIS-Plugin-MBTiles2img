# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mbtiles2img_dialog_base.ui'
#
# Created: Sat Feb 20 00:35:46 2016
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
        MBTiles2imgDialogBase.resize(310, 330)
        MBTiles2imgDialogBase.setMinimumSize(QtCore.QSize(310, 330))
        MBTiles2imgDialogBase.setMaximumSize(QtCore.QSize(310, 330))
        self.layoutWidget = QtGui.QWidget(MBTiles2imgDialogBase)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 200, 291, 121))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.runExtractionButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runExtractionButton.sizePolicy().hasHeightForWidth())
        self.runExtractionButton.setSizePolicy(sizePolicy)
        self.runExtractionButton.setMinimumSize(QtCore.QSize(0, 50))
        self.runExtractionButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.runExtractionButton.setObjectName(_fromUtf8("runExtractionButton"))
        self.verticalLayout_2.addWidget(self.runExtractionButton)
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.helpButton = QtGui.QPushButton(self.layoutWidget)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.verticalLayout_2.addWidget(self.helpButton)
        self.layoutWidget1 = QtGui.QWidget(MBTiles2imgDialogBase)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 291, 161))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.layoutWidget1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.loadFileButton = QtGui.QPushButton(self.splitter)
        self.loadFileButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loadFileButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.loadFileButton.setObjectName(_fromUtf8("loadFileButton"))
        self.labelPathMBTiles = QtGui.QLabel(self.splitter)
        self.labelPathMBTiles.setMinimumSize(QtCore.QSize(0, 30))
        self.labelPathMBTiles.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelPathMBTiles.setFrameShape(QtGui.QFrame.Box)
        self.labelPathMBTiles.setFrameShadow(QtGui.QFrame.Raised)
        self.labelPathMBTiles.setScaledContents(True)
        self.labelPathMBTiles.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathMBTiles.setObjectName(_fromUtf8("labelPathMBTiles"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(self.layoutWidget1)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.selectDestFolderButton = QtGui.QPushButton(self.splitter_2)
        self.selectDestFolderButton.setMinimumSize(QtCore.QSize(0, 40))
        self.selectDestFolderButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.selectDestFolderButton.setObjectName(_fromUtf8("selectDestFolderButton"))
        self.labelPathDestFolder = QtGui.QLabel(self.splitter_2)
        self.labelPathDestFolder.setMinimumSize(QtCore.QSize(0, 30))
        self.labelPathDestFolder.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelPathDestFolder.setFrameShape(QtGui.QFrame.Box)
        self.labelPathDestFolder.setFrameShadow(QtGui.QFrame.Raised)
        self.labelPathDestFolder.setScaledContents(True)
        self.labelPathDestFolder.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathDestFolder.setObjectName(_fromUtf8("labelPathDestFolder"))
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.retranslateUi(MBTiles2imgDialogBase)
        QtCore.QMetaObject.connectSlotsByName(MBTiles2imgDialogBase)

    def retranslateUi(self, MBTiles2imgDialogBase):
        MBTiles2imgDialogBase.setWindowTitle(_translate("MBTiles2imgDialogBase", "MBTiles images extract", None))
        self.runExtractionButton.setText(_translate("MBTiles2imgDialogBase", "Run tile extraction", None))
        self.helpButton.setText(_translate("MBTiles2imgDialogBase", "Help", None))
        self.loadFileButton.setText(_translate("MBTiles2imgDialogBase", "Load MBTiles file", None))
        self.labelPathMBTiles.setText(_translate("MBTiles2imgDialogBase", "MBTiles to extract...", None))
        self.selectDestFolderButton.setText(_translate("MBTiles2imgDialogBase", "Select folder to save images", None))
        self.labelPathDestFolder.setText(_translate("MBTiles2imgDialogBase", "Set destination folder...", None))

