from itertools import combinations
N = int(input())
ls = list(map(str, input().split()))[:N]
K = int(input())
print(N, ls, K)

pairs = list(combinations(ls, K))
print(pairs)

filteredList = [i for i in pairs if 'a' in i]
print(len(filteredList)/ len(pairs))


# method 2
# N = int(input())
# L = input().split()
# K = int(input())

# C = list(combinations(L, K))
# F = filter(lambda c: 'a' in c, C)
# print("{0:.3}".format(len(list(F))/len(C)))

# Method 3
# M = ''.join(L).count('a')
# print 1.0 - reduce(lambda x,y: x*y,[(1.0-M*1.0/(N-i)) for i in xrange(K)])