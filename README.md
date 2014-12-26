#QGIS Plugin - MBTiles2img

##Description
With this QGIS plugin you can take an MBTiles file and extract all the tiles as images to a local folder.
This plugin can be very useful for debugging processes.

Compliant with MBTiles stable specification (1.1) and previous (1.0):
https://github.com/mapbox/mbtiles-spec

##Requirements
QGIS 2.0 or later.

This project uses MBTilesextractor library to do the work:
https://github.com/cayetanobv/MBTilesextractor_lib

You must add MBTilesextractor library as a Git submodule:

$ git submodule add https://github.com/cayetanobv/MBTilesextractor_lib.git

##About author
Developed by Cayetano Benavent (2014).
GIS Analyst at Geographica.

http://www.geographica.gs/#!/en/geographica/team

##License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
