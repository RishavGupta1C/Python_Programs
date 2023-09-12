def getMinimumCost(k, c):
    c = sorted(c)
    i=1
    x=1
    count = 0
    minimum_cost = 0
    while i<=len(c):
        z = c.pop()
        minimum_cost += x * z
        print(z)
        count += 1
        if count%k == 0:
            x += 1
    return minimum_cost

ls = [1,3,5,7,9]
k=3
print(getMinimumCost(k,ls))