import math
i=int(input('nhap n dòng: '))
m=0
a=2

def tinh(m):
	for j in range(0,m+1):
		print(int(ct(m,j)))
		
		


def ct(n,k):
	
	p= math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
	return p 
print("1\n1 1")
while a<i:
	tinh((a))
	a+=1
	