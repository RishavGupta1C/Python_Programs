def toys(w):
    w = sorted(w)
    i = 1
    count = 1
    minimum_w = w[0]
    while i<len(w):
        if w[i]<=minimum_w+4:
            pass
        else:
            count += 1
            minimum_w = w[i]
        i += 1
    return count

w = [1,2,3,21,7,12,14,21]
print(toys(w))