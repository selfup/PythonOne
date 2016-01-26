import os

o = os.system

o('brew install libtiff libjpeg webp little-cms2')
o('pip install --upgrade pip')
o('brew install Caskroom/cask/xquartz')
o('pip install Pillow')
o('brew install imagemagick --with-fftw --with-librsvg --with-x11')
o('brew install graphviz --with-librsvg --with-x11')
o('brew install cairo')
o('brew install py2cairo') # this will ask you to download xquartz and install it
o('brew install qt pyqt')
