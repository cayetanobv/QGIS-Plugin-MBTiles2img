"""
/***************************************************************************
 MBTiles2img

 A QGIS plugin

This plugin takes an mbtiles file and split it apart into a folder hierarchy
 of individual image tile files.
                              -------------------
        begin                : 2014-12-09
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
import os.path

from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from qgis.core import Qgis
from MBTiles2img import resources_rc
from MBTiles2img.mbtilesextractor import MBTilesExtractor
from MBTiles2img.mbtiles2img_dialog import MBTiles2imgDialog


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
        self.dlg = MBTiles2imgDialog(parent=self.iface.mainWindow())

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

        self.dlg.loadFileButton.clicked.connect(self.loadMBTilesFile)
        self.dlg.selectDestFolderButton.clicked.connect(self.setDestFolder)
        self.dlg.runExtractionButton.clicked.connect(self.runTileExtraction)
        self.dlg.helpButton.clicked.connect(self.getHelp)


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&MBTiles images extract'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        #show the dialog
        self.dlg.show()

    def runTileExtraction(self):
        """
        Run tiles extraction from MBTiles file
        """

        input_file = self.dlg.getPathMBTiles()
        dest_folder = self.dlg.getPathDestFolder()
        res = self.tileExtractor(input_file, dest_folder)

        if res == 1:
            self.dlg.clearLabelPathMBTiles()
            self.dlg.clearLabelPathDestFolder()
            self.dlg.setLabelPathDestFolder("Destination folder...")
            self.dlg.setLabelPathMBTiles("MBTiles to extract...")

    def loadMBTilesFile(self):
        """
        Load MBTiles file
        """

        self.dlg.progressBar.setValue(0)

        # open file dialog to load MBTiles file
        start_dir = '/home'
        fl_types = "MBTiles files (*.mbtiles)"
        file_path, _ = QFileDialog.getOpenFileName(self.iface.mainWindow(),
                                                'Open MBTiles file',
                                                start_dir, fl_types)

        if file_path:
            self.dlg.setLabelPathMBTiles(file_path)
        else:
            self.dlg.setLabelPathMBTiles("MBTiles to extract...")

    def setDestFolder(self):
        """
        Set Destination folder to save exported images
        """

        self.dlg.progressBar.setValue(0)

        # open file dialog to select folder
        start_dir = '/home'
        folder_path = QFileDialog.getExistingDirectory(self.iface.mainWindow(),
                                                     'Select destination folder to save exported images',
                                                     start_dir)

        if folder_path:
            self.dlg.setLabelPathDestFolder(folder_path)
        else:
            self.dlg.setLabelPathDestFolder("Destination folder...")

    def tileExtractor(self, input_file, dest_folder):
        """
        MBTiles images extraction method

        This method uses MBTilesextractor library to do the work

        """

        try:
            ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=True)
            self.dlg.progressBar.setValue(10)
            ex_mbt.extractTiles()
            msg_type= "Info"
            level = Qgis.Info
            progress_value  = 100

            outfolder = os.path.join(dest_folder,os.path.basename(input_file).split('.')[0])
            result = 'Tile extraction done! Output folder: {}'.format(outfolder)

            self.iface.messageBar().pushMessage(msg_type, result, level=level, duration=10)
            self.dlg.progressBar.setValue(progress_value)

            return 1

        except Exception as err:
            result = 'Error: {0}'.format(err)
            self.iface.messageBar().pushMessage("Error", result, level=Qgis.Critical, duration=10)
            self.dlg.progressBar.setValue(0)

    def getHelp(self):
        """
        Show help to users
        """

        QMessageBox.information(self.iface.mainWindow(),"Help",
            """
            1) Select MBTiles to extract.

            2) Select destination folder to
            save exported images.

            3) Push button "Run tile extraction".

            Developed by Cayetano Benavent 2014-2018.

            """)
