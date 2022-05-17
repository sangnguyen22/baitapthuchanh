a=input('nhap danh sach: ').split()
for i in range(0,len(a)):
	a[i]=int(a[i])
print('so lon nhat la: ',max(a))
print('so be nhat la: ',min(a))	
