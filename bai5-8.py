def giai(dlist,item):
	pos=0
	found= False
	while True:
		if pos<len(dlist):
			found=True
			print('phan tu khong duoc tim thay!')
		else:
			return found,pos
		if dlist[pos]==item:
			found==True
			print('True',pos)
		else:
			pos=pos+1
a=input('nhap: ')
b=input('nhap phan tu can tim kiem: ')
giai(a,b)