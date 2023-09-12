# import email.utils

# n = int(input())
# for i in range(n):
# 	username = input()
# 	print(email.utils.formataddr(username))
	# if(email.parseaddr(username).equals(username))
		# print(username)

number_list = [1,2,3]
string_list = ['one', 'two']
number_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip()

print(result)

result = zip(number_list, number_tuple)
result_set = set(result)
print(result_set)

result = zip(number_list, string_list)
result_set = set(result)
print(result_set)