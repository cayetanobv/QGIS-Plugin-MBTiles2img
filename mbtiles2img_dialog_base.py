# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mbtiles2img_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MBTiles2imgDialogBase(object):
    def setupUi(self, MBTiles2imgDialogBase):
        MBTiles2imgDialogBase.setObjectName("MBTiles2imgDialogBase")
        MBTiles2imgDialogBase.resize(310, 330)
        MBTiles2imgDialogBase.setMinimumSize(QtCore.QSize(310, 330))
        MBTiles2imgDialogBase.setMaximumSize(QtCore.QSize(310, 330))
        self.layoutWidget = QtWidgets.QWidget(MBTiles2imgDialogBase)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 200, 291, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.runExtractionButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runExtractionButton.sizePolicy().hasHeightForWidth())
        self.runExtractionButton.setSizePolicy(sizePolicy)
        self.runExtractionButton.setMinimumSize(QtCore.QSize(0, 50))
        self.runExtractionButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.runExtractionButton.setObjectName("runExtractionButton")
        self.verticalLayout_2.addWidget(self.runExtractionButton)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.helpButton = QtWidgets.QPushButton(self.layoutWidget)
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout_2.addWidget(self.helpButton)
        self.layoutWidget1 = QtWidgets.QWidget(MBTiles2imgDialogBase)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 291, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.loadFileButton = QtWidgets.QPushButton(self.splitter)
        self.loadFileButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loadFileButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.loadFileButton.setObjectName("loadFileButton")
        self.labelPathMBTiles = QtWidgets.QLabel(self.splitter)
        self.labelPathMBTiles.setMinimumSize(QtCore.QSize(0, 30))
        self.labelPathMBTiles.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelPathMBTiles.setFrameShape(QtWidgets.QFrame.Box)
        self.labelPathMBTiles.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelPathMBTiles.setScaledContents(True)
        self.labelPathMBTiles.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathMBTiles.setObjectName("labelPathMBTiles")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.selectDestFolderButton = QtWidgets.QPushButton(self.splitter_2)
        self.selectDestFolderButton.setMinimumSize(QtCore.QSize(0, 40))
        self.selectDestFolderButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.selectDestFolderButton.setObjectName("selectDestFolderButton")
        self.labelPathDestFolder = QtWidgets.QLabel(self.splitter_2)
        self.labelPathDestFolder.setMinimumSize(QtCore.QSize(0, 30))
        self.labelPathDestFolder.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelPathDestFolder.setFrameShape(QtWidgets.QFrame.Box)
        self.labelPathDestFolder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelPathDestFolder.setScaledContents(True)
        self.labelPathDestFolder.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPathDestFolder.setObjectName("labelPathDestFolder")
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.retranslateUi(MBTiles2imgDialogBase)
        QtCore.QMetaObject.connectSlotsByName(MBTiles2imgDialogBase)

    def retranslateUi(self, MBTiles2imgDialogBase):
        _translate = QtCore.QCoreApplication.translate
        MBTiles2imgDialogBase.setWindowTitle(_translate("MBTiles2imgDialogBase", "MBTiles images extract"))
        self.runExtractionButton.setText(_translate("MBTiles2imgDialogBase", "Run tile extraction"))
        self.helpButton.setText(_translate("MBTiles2imgDialogBase", "Help"))
        self.loadFileButton.setText(_translate("MBTiles2imgDialogBase", "Load MBTiles file"))
        self.labelPathMBTiles.setText(_translate("MBTiles2imgDialogBase", "MBTiles to extract..."))
        self.selectDestFolderButton.setText(_translate("MBTiles2imgDialogBase", "Select folder to save images"))
        self.labelPathDestFolder.setText(_translate("MBTiles2imgDialogBase", "Set destination folder..."))

