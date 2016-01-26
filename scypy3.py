import os

o = os.system

o('pip install virtualenv && pip install nose && pip install numpy && pip install scipy && brew install numpy && brew install scipy')
o("python -c 'import numpy ; numpy.test();'")
o("python -c 'import scipy ; scipy.test();'")
