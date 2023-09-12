# s = 'This is a sunstring in python'
# print(s[2:10:2])

# myset = {"abcd", 11, 1.1, "11", (1,2)}
# print(myset)

# l = [0, 1,1,2,3,5,8,13,21,34,55]
# res = list(filter(lambda x: x%2 -1, l))
# print(res)


# mylist = [lambda m:m**2,lambda m,n:m*n,lambda m:m**4]
# print(mylist[0](10), mylist[1](2,20), mylist[2](3))


# a = [1,2,3,4,5,6,7,8,9]
# print(a[::2])

# import re
# m = re.finditer('[abc]','dtg$b@uagd')
# for i in m:
#     print(i.start(), i.group())


# Comparing time of printing a list of space-separated elements in Python3
import time as t

a, b = 10, 210000
l = list(range(a, b))
tic = t.time()
for i in l:
    print(i, end=" ")
print()
tac = t.time()
t1 = (tac - tic) * 1000
print(*l)
toe = t.time()
t2 = (toe - tac) * 1000
print(" ".join([str(i) for i in l]))
joe = t.time()
t3 = (joe - toe) * 1000
print(" ".join(list(map(str, l))))
toy = t.time()
t4 = (toy - joe) * 1000
print("Time",t1,t2,t3,t4)

# Time 34097.96595573425 33599.29275512695 128.01218032836914 112.00642585754395
