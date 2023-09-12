
from itertools import combinations
string, k = input().split()
i = 1
while i<=int(k):
    ls = list(combinations(sorted(string), i))
    [print(''.join(x)) for x in ls]
    i += 1


ls = list(combinations(string, int(k)))
print(ls)
ls1 = list(combinations(sorted(string), int(k)))
[print(''.join(x)) for x in ls1]



