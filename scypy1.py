import os

o = os.system

o('echo Starting Python Science')
o('brew update --verbose')
o('brew doctor --verbose')
o('echo Python Science Is Over')
o('brew tap homebrew/science') # a lot of cool formulae for scientific tools
o('brew tap homebrew/python') # numpy, scipy, matplotlib, ...
o('brew update && brew upgrade')
o('brew install python')
o('brew doctor')
