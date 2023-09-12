from itertools import groupby
string = input()
# i = 0
# while i<len(string):
#     print(string.count(string[i]))
#     i+=1


groups = []
uniquekeys = []
data = list(string)
print(data)

# for k, g in groupby(string, string.count):
    # groups.append(list(g))
    # uniquekeys.append(k)
# This is used to group up characters based on the count and consecutiveness of each character.

# method 1
for k, g in groupby(string):
    groups.append(list(g))
    uniquekeys.append(k)

[print((len(groups[i]), uniquekeys[i]), end = ' ') for i in range(len(groups))]

# print()
# print(groups)
# print(uniquekeys)

# method 2
print()
for k, g in groupby(input()):
    a = list(g)
    # print((len(a), a[0]), end = ' ')
    print("(", len(a), ", ", a[0], ")", end = " ", sep = "")



# method 3
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])