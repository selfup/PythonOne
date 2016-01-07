#!/usr/bin/python

import os

o = os.system

o('pwd')
o('echo Starting Brew Stuff')
o('brew update --verbose')
o('brew upgrade --verbose')
o('brew cleanup --verbose')
o('brew doctor --verbose')
o('echo Brew Stuff Is Over')
