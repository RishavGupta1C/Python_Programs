def merge_the_tools(string, k):
	t = []
	# u = []
	# n = len(string)
	# if n%k == 0:
	# 	parts = int(n/k)
	# 	for i in range(parts):
	# 		t.append(string[3*i:3*(i+1)])
	# 	print(t)

	# x = iter([1,2,3,4,5,6,7,8,9])
	# print(list(zip(x, x, x)))
	
	# print(1, 2, 3, 4)
	# print(*[1, 2, 3, 4])


# 1st way:
	length_t = 0
	for item in string:
		length_t += 1
		if item not in t:
			t.append(item)
		if length_t == k:
			print(''.join(t))
			t = []
			length_t = 0
	result = zip(*([iter(string)] *k))
	print(result)
	result_list = list(result)
	print(result_list)

# 2nd way:
	for part in zip(*([iter(string)] *k)):
		d = dict()
		ls = [d.setdefault(c, c) for c in part if c not in d]
		print(ls)
		

# Expaination of the 2nd way ->

# setdefault method returns the key value available in the dictionary and if given key is not available then it will take provided default value and adds it to the dictionary.



# what exactly this zip(*iter(S)*N) do?



# ❶iter(s) returns an iterator for S.

# ❷[iter(s)]*n makes a list of n times the same iterator for s.

# Example: [[iter(s)]*3] = ([iter(s), iter(s), iter(s)])

# ADVICE: It's not three copies of the same iterator, it's three times the same iterator object. Really:

# for part in zip(*[iter(S)] * N):
# It is equivalent to:

# it = iter(s)
# for part in zip(it, it, it):
# ❹*[] unpack a list: 
	# i.e. *[] unpacks all the three iterators before zipping.
# Example: print(*[1,2,3,4]) = print(1,2,3,4)

# ❺zip make an iterator that aggregates elements from each of the iterables.

# Example:

# >>> x = [1, 2, 3]
# >>> y = [4, 5, 6]
# >>> zipped = zip(x, y)
# >>> list(zipped)
# [(1, 4), (2, 5), (3, 6)]
# we have:

# zip(*[iter(s)]*3)
# It is equivalent to:

# itr = iter(s)
# zip(itr, itr, itr)
# it extracts an item from all the three iterators from the list in order. Since all the iterators are the same object, it just groups the list in chunks of 3.

# Example:

# for part in zip(*[iter('abcdefghi')]*3):
# 	print(part)
# a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i
# ^                    ^                    ^             
#       ^                    ^                    ^
#             ^                    ^                    ^
# Output:

# (a,b,c)

# (d,e,f)

# (g,h,i)







# 3rd way:
 	# for i in range(0, len(string), k):
  #       uniq = ''
  #       for c in string[i : i+k]:
  #           if (c not in uniq):
  #               uniq+=c
  #       print(uniq)




if __name__ == '__main__':
	string, k = input(), int(input())
	merge_the_tools(string, k)