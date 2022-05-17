def file_read(fname):
	from itertools import isline
	with open (fname, 'w') as myfile:
			myfile.write('Python exercies\\n')
			myfile.write('Java exercies')
	txt= open(fname)
	print(txt.read())

file_read('abc.txt')