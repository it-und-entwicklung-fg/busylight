# Basic Makefile

deb: 
	cd ./Package; \
	  debuild -b -kC3FBBEC27B2A17AE

package: 
	cd ./Package; \
	debuild -S -sa -kC3FBBEC27B2A17AE
