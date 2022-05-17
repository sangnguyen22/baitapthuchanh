ds= input('nhap chuoi: ').split()
ds.append('abc')
ds.remove('123')
for ch in ds:
	print(ch)
print("vi tri cua chuoi abc la: ", ds.index('abc'))
ds.sort()
for ch in ds:
	print(ch)