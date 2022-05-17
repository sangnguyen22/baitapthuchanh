import math
x1=int(input("nhap gia tri x1--->"))
y1=int(input("nhap gia tri y1--->"))

x2=int(input("nhap gia tri x2--->"))
y2=int(input("nhap gia tri y2--->"))
 
d1= (x2 - x1) * (x2 - x1)
d2 = ( y2 - x1) * ( y2 - y1)
res = math.sqrt(d1+d2)
print ("khoang cach 2 diem la:",res );