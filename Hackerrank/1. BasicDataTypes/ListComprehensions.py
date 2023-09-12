# 0<=i<=x; 0<=j<=y; 0<=k<=z
# i+j+k != n

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Without List Comprehension

lists = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != n:
                lists.append([i, j, k])

print(lists)

print()
# With List Comprehension

lists = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]

print(lists)
