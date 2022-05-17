s=input('nhap 1 chuoi: ').split()
ddln=0


for a in s:
	if len(a) > ddln:
		ddln= len(a)
ptln=a
print('phan tu %s co do dai lon nhat va bang %d' %(ptln,ddln)	)	
