# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MBTiles2imgDialog
                                 A QGIS plugin
 This plugin takes an mbtiles file and split it apart into a folder hierarchy of individual image tile files.
                             -------------------
        begin                : 2014-12-09
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Cayetano Benavent
        email                : cayetanobv@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'mbtiles2img_dialog_base.ui'))


class MBTiles2imgDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MBTiles2imgDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
    
    def setLabelPathMBTiles(self, output):
        self.labelPathMBTiles.setText(output)
    
    def setLabelPathDestFolder(self, output):
        self.labelPathDestFolder.setText(output)
