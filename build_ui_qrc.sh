echo "Building UI with pyuic5..."
pyuic5 -o mbtiles2img_dialog_base.py mbtiles2img_dialog_base.ui

echo "Building resources with pyrcc5  ..."
pyrcc5 -o resources_rc.py resources.qrc
