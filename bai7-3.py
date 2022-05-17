f1 = open('myfile.txt', 'r', encoding='UTF-8')

# Đọc toàn bộ file lần 1
data1 = f1.read()
print(data1)
#>> Hello world
f1.close() # Đóng file
    
# Đọc toàn bộ file lần 2
f2 = open('myfile.txt', 'r', encoding='UTF-8')
data2 = f2.read(1)# Đóng file
print(data2)
#>> H
f2.close()