import sys
import signal
import time
import thread


class BaseApp(object):

	def __init__(self):
		super(BaseApp, self).__init__()
		self.stop_signal = False
		self.stop_child_signal = False

	def init(self):
		self.prnt("BaseApp.init")

		def handleSignal(signum, frame) :
			self.handleSignal(signum, frame)
		signal.signal(signal.SIGTERM, handleSignal)

	def run(self):
		self.prnt("BaseApp.run")

		t_id = thread.start_new_thread(self.runThread, (0,))

		while True:
			time.sleep(5)
			if(self.stop_signal and self.stop_child_signal):
				self.prnt("Shutting down...")
				self.shutdown()
				break

	def runThread(self, threadID):
		self.prnt("BaseApp.runThread")

		while True:
			time.sleep(10)
			if(self.stop_signal):
				self.prnt("BaseApp.runThread : stop received")
				self.stop_child_signal = True
				break

	def signalThread(self):
		self.prnt("BaseApp.signalThread : " + str(threadID))

	def handleSignal(self, signum, frame) :

		self.prnt("BaseApp.handleSignal : " + str(signum))
		self.stop_signal = True

	def shutdown(self):
		self.prnt ("BaseApp.shutdown")

	def prnt(self, message):
		print(message)
		sys.stdout.flush()
