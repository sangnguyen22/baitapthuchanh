a=input('nhap danh sach: ').split()
for i in range(0,len(a)):
	a[i]=int(a[i])
f=max(a)
k=min(a)
print('so lon nhat la: ',f)
print('so be nhat la: ',k)
print('vi tri cau so lon nhat la: 'a.index(f))
print('vi tri cua so be nhat la: 'a.index(k))