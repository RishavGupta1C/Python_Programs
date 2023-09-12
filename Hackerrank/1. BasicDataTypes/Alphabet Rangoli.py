pattern = [1, 2, 3, 4, 5]
n = len(pattern)
for i in range(n-1, -1, -1):            # To traveerse backward using range()
    print(i, ' -> ', pattern[i])



import string
alpha = string.ascii_lowercase
num = int(input())

def srange(N):
    return list(range(N)) + list(range(N-2, -1, -1))
for i in srange(num):
    print('-'.join([alpha[num-j-1] for j in srange(i+1)]).center(4*num-3, '-'))