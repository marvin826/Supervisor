import BaseApp as ba
import sys

print "BaseAppTester.starting..."
sys.stdout.flush()

baseApp = ba.BaseApp()
baseApp.init()
sys.stdout.flush()

print "BaseApp.run..."
baseApp.run()
sys.stdout.flush()

print "BaseAppTester....ending"


