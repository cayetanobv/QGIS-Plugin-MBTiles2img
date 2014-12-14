# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MBTiles2img
                                 A QGIS plugin
 This plugin takes an mbtiles file and split it apart into a folder hierarchy 
 of individual image tile files.
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from mbtiles2img_dialog import MBTiles2imgDialog
import os.path
from MBTilesextractor_lib.lib.mbtilesextractor import MBTilesExtractor


class MBTiles2img:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MBTiles2img_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = MBTiles2imgDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&MBTiles images extract')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'MBTiles2img')
        self.toolbar.setObjectName(u'MBTiles2img')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('MBTiles2img', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/MBTiles2img/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'MBTiles images extract'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # Connecting actions and functions (signals and slots)
        QObject.connect(self.dlg.loadFileButton, SIGNAL("clicked()"), self.loadMBTilesFile)
        QObject.connect(self.dlg.selectDestFolderButton, SIGNAL("clicked()"), self.setDestFolder)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&MBTiles images extract'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # run MBTiles image extraction process
            input_file = self.dlg.getPathMBTiles()
            dest_folder = self.dlg.getPathDestFolder()
            self.runExtraction(input_file, dest_folder)
            
            
    
    def loadMBTilesFile(self):
        #Load MBTiles file
        
        # open file dialog to load MBTiles file
        start_dir = '/home'
        fl_types = "MBTiles files (*.mbtiles)"
        file_path = QFileDialog.getOpenFileName(self.iface.mainWindow(), 
                                                'Open MBTiles file', start_dir, fl_types)
        
        if file_path:
            self.dlg.setLabelPathMBTiles(file_path)
        else:
            self.dlg.setLabelPathDestFolder("MBTiles to extract...")
    
    def setDestFolder(self):
        #Set Destination folder to save exported images
        
        # open file dialog to select folder
        start_dir = '/home'
        folder_path = QFileDialog.getExistingDirectory(self.iface.mainWindow(), 
                                                     'Select destination folder to save exported images', 
                                                     start_dir)
        
        if folder_path:
            self.dlg.setLabelPathDestFolder(folder_path)
        else:
            self.dlg.setLabelPathDestFolder("Destination folder...")
    
    def runExtraction(self, input_file, dest_folder):
        # Run MBTiles images extraction
        
        try:
            ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=True)
            result = ex_mbt.extractTiles()
            msg_type= "Info"
            level = QgsMessageBar.INFO
            if 'Done!' not in result:
                msg_type= "Warning"
                level = QgsMessageBar.WARNING
            self.iface.messageBar().pushMessage(msg_type, result, level=level)
    
        except Exception as e:
            result = 'Error: %s - %s' % (e.message, e.args)
            self.iface.messageBar().pushMessage("Error", result, level=QgsMessageBar.CRITICAL)
    
