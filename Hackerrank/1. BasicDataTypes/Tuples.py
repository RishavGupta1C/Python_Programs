n = int(input())
integer_list = map(int, input().split()[:n])    # to work with only first n inputs
print(n)
for i in integer_list:
    print(i)
print(type(integer_list))   # class map
my_tuple = tuple(integer_list)
print(hash(my_tuple))
