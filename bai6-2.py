class hinhchunhat:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def chieudai(self):
		return self.a
	def chieurong(self):
		return self.b
	def dientich(self):
		return self.a * self.b
h= hinhchunhat(5,4)
print(h.dientich())