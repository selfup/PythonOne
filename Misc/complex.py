# coding: interpy

import sys, os, subprocess

o = os.system

output = subprocess.check_output('ruby ruby_store.rb', shell=True)

o('rm -rf ruby_store.rb')
o('echo class RubyStore >> ruby_store.rb')
o('echo def data >> ruby_store.rb')
o('echo 100.to_s >> ruby_store.rb')
o('echo end >> ruby_store.rb')
o('echo end >> ruby_store.rb')
o('echo puts RubyStore.new.data >> ruby_store.rb')
o("python fib.py  #{output}" )
