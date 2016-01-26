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
o('pip install virtualenv && pip install nose && pip install numpy && pip install scipy && brew install numpy && brew install scipy')
o("python -c 'import numpy ; numpy.test();'")
o("python -c 'import scipy ; scipy.test();'")
# brew install matplotlib --with-cairo --with-tex
# pip install pandas
# pip install nltk
# pip install sympy
# pip install q
# pip install snakeviz
# brew install zmq
# pip install ipython[all]
# pip install html5lib cssselect pyquery lxml BeautifulSoup
# pip install Flask Django tornado
# pip install rdflib SPARQLWrapper
# pip install networkx
