# def alphabet_rangoli(size):
# 	myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
# 	for i in range(size-1, -size, -1):
# 		x = abs(i)
# 		line = myStr[size:x:-1]+myStr[x:size]
# 		print("--"*x+'-'.join(line)+"--"*x)

# if __name__ == "__main__":
# 	n = int(input())
# 	alphabet_rangoli(n)


# 2nd method:

import string
def alphabet_rangoli(size):
	alpha = string.ascii_lowercase
	# print(alpha)
	line = []
	for i in range(n):
		myStr = "-".join(alpha[i:n])
		line.append((myStr[::-1]+myStr[1:]).center(4*n-3, '-'))
		# print(line)
	print('\n'.join(line[:0:-1]+line))

if __name__ == "__main__":
	n = int(input())
	alphabet_rangoli(n)
