# Basic Makefile

deb: 
	cd ./Package; \
	  debuild -b -kC3FBBEC27B2A17AE
	rm -r ./Package/debian/.debhelper/ ./Package/debian/busylight/
	rm ./Package/debian/busylight.substvars ./Package/debian/debhelper-build-stamp ./Package/debian/files

package: 
	cd ./Package; \
	  debuild -S -sa -kC3FBBEC27B2A17AE
	rm ./Package/debian/files
