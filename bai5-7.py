import numpy as np
kdl_type=[('ten','S15'),('lop',int),('cannang',float)]
dl_details=[("tuan",5,40.5),("tu",6,50.7),("huyen",7,47.5),('tung',3,24.5)]
hs=np.array(dl_details, dtype=kdl_type)
print('dsa: ')

print(dl_details)
print('sap xep theo can nang: ')
print(np.sort(dl_details, order='cannang'))
