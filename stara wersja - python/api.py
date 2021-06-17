
class Radar(object):
	def __init__(self, port):
		# port:
			# macos:  ls /dev/tty.*
			# windows : device manager / ports
		import serial, json
		self.json = json
		self.data = serial.Serial(str(port))
		self.data.flushInput()

	def get_data(self):
		return self.json.loads(self.data.readline().decode('utf-8').rstrip().replace('\\', ''))
