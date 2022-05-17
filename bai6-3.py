class nguoi(object):
	def getGender(self):
		return 'unknown'
class nam(nguoi):
	def getGender(self):
		return"Nam"
class nu(nguoi):
	def getGender(self):
		return "nu"
aNam= nam()
aNu= nu()
print(aNam.getGender())
print(aNu.getGender())