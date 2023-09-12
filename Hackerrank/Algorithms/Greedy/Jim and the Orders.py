def jimOrders(orders):
    # i = 0
    # ls = []
    # while i<len(orders):
    #     ls.append([i+1,sum(orders[i])])
    #     # ls.append(orders[i][0]+orders[i][1])
    #     i += 1
    # print(ls)
    # ls = sorted(ls, key = lambda x: x[1])
    ls = sorted(enumerate(orders, 1), key = lambda x: sum(x[1]))
    print(ls)
    return [i[0] for i in ls]



n = int(input())
orders = []
for _ in range(n):
    orders.append(list(map(int, input().rstrip().split())))
print(orders)
print(jimOrders(orders))


# One-line Solution
# print(*(q[0]+1 for q in sorted([(i, sum(map(int, input().split()))) for i in range(int(input()))], key=lambda x: (x[1], x[0]))))