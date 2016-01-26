import os

o = os.system

o('pip install virtualenv && pip install nose && pip install numpy && pip install scipy && brew install numpy && brew install scipy')
o('brew link numpy')
o('brew link --overwrite numpy')
o("python -c 'import numpy ; numpy.test();'")
o("python -c 'import scipy ; scipy.test();'")
o('# brew install matplotlib --with-cairo --with-tex && pip install pandas && pip install nltk && pip install sympy && pip install q && pip install snakeviz')
o('brew install zmq')
o('pip install ipython[all]')
o('pip install html5lib cssselect pyquery lxml BeautifulSoup')
o('pip install Flask Django tornado')
o('pip install rdflib SPARQLWrapper')
o('pip install networkx')
