
def reverse_word(self, s):
	self.s=s
	return ''.join(reverse(s.split()))
print(reverse_word('hello_python'))