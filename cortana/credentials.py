class Credentials:
	def __init__(self):
		f = open("credentials.txt")
		lines = f.readlines()
		self.email = lines[0].replace("\n","")
		self.password = lines[1].replace("\n","")
		f.close()