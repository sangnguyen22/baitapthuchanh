print("Nhập vào số N lớn hơn 1: ")
n = int(input())
flag = True
if n==1:
    flag = False
for i in range(2,n):
        if (n % i == 0):
            flag = False
if flag == True:
    print(n, " là số nguyên tố")
else:
    print(n, " không phải là số nguyên tố")