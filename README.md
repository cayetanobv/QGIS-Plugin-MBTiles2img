#QGIS Plugin - MBTiles2img

##Description
With this QGIS plugin you can take an MBTiles file and extract all the tiles as images to a local folder.
This plugin can be very useful for debugging processes.

You can find the plugin in QGIS Plugin Repository:

https://plugins.qgis.org/plugins/MBTiles2img/

To install it you can use the QGIS plugin manager from the Plugins menu.

Compliant with MBTiles stable specification (1.1) and previous (1.0):

https://github.com/mapbox/mbtiles-spec

##Requirements
QGIS 2.0 or later.

This project uses MBTilesextractor library to do the work:

https://github.com/cayetanobv/MBTilesextractor_lib

You must add MBTilesextractor library as a Git submodule:

```
$ git submodule add https://github.com/cayetanobv/MBTilesextractor_lib.git
```

To use the Plugin from this repository you must run ```preparesubmoduleforplugin.sh``` script.

##About author
Developed by Cayetano Benavent (2014-2017).
GIS Analyst at Geographica.

http://www.geographica.gs

##License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
