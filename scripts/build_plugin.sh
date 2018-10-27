echo "Building plugin..."
./build_ui_qrc.sh

echo "Preparing submodule..."
./preparesubmoduleforplugin.sh

if [ "$DEBUG" == "1" ]; then
  echo "Copying plugin to QGIS3 folder for debugging..."
  SOURCE=../../MBTiles2img
  DESTINATION=~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
  cp -rf $SOURCE $DESTINATION
fi
