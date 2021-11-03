#!/bin/bash
cd ./Package
debuild -b -kC3FBBEC27B2A17AE
rm ./Package/debian/busylight.debhelper.log ./Package/debian/busylight.substvars ./Package/debian/files
rm -r ./Package/debian/busylight ./Package/debian/.debhelper