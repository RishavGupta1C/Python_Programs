from itertools import permutations
string, k = map(str, input().split())
k = int(k)
ls = sorted(list(permutations(string, k)))

for i in ls:
    print(''.join(i))

[print(''.join(i)) for i in ls]