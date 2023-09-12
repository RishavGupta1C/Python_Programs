def boardCutting(cost_y, cost_x):
    cost_y = list(reversed(sorted(cost_y)))
    cost_x = list(reversed(sorted(cost_x)))
    # print(cost_x)
    # print(cost_y)
    segment_x = 1
    segment_y = 1
    total_cost = 0
    k = 0
    j = 0
    i=0
    while i < len(cost_y) + len(cost_x):
        if k > len(cost_x)-1 or (j != len(cost_y) and cost_y[j] >= cost_x[k]):
            total_cost += cost_y[j] * segment_x
            segment_y += 1
            # if j < len(cost_y)-1:
            j += 1
        else:
            total_cost += cost_x[k] * segment_y
            segment_x += 1
            k += 1
        print(total_cost)
        i += 1
    return total_cost%(pow(10,9)+7)


cy = [2, 1, 3, 1, 4]
cx = [4, 2, 2]
boardCutting(cy, cx)