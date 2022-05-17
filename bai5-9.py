def Binary Search(x, a, left_idx, right_idx):
	if left_idx > right_idx:
		return -1
	mid_idx = left_idx + (right_idx - left_idx)//2
	mid = a[mid_idx]
	if x== mid:
		return mid_idx
	elif x< mid:
		return bin_search(x, a, left_idx, mid_idx -1)
	else:
		return bin_search(x, a, mid_idx +1, right_idx)
assert bin_search(0,[0], 0 ,0)==0
assert bin_search(0,[1],0 ,0)==-1
assert bin_search(0,[0,1],0,1)==0
assert bin_search(1,[0,1],0,1)==1
assert bin_search(2,[0,1],0,1)==-1
