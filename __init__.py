# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MBTiles2img
                                 A QGIS plugin
 This plugin takes an mbtiles file and split it apart into a folder hierarchy of individual image tile files.
                             -------------------
        begin                : 2014-12-09
        copyright            : (C) 2014 by Cayetano Benavent
        email                : cayetanobv@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MBTiles2img class from file MBTiles2img.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .mbtiles2img import MBTiles2img
    return MBTiles2img(iface)
