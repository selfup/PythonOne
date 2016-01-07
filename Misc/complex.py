import sys, os

o = os.system

pwd = o('pwd')

o('rm -rf ruby_store.rb')
o('echo class RubyStore >> ruby_store.rb')
o('echo def data >> ruby_store.rb')
o('echo 100 >> ruby_store.rb')
o('echo end >> ruby_store.rb')
o('echo end >> ruby_store.rb')
o('echo puts RubyStore.new.data >> ruby_store.rb')
o('ruby ruby_store.rb')
