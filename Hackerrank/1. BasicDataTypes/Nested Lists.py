# Method 1: Using only list
# ls = []
# ls = [[input(), float(input())] for _ in range(int(input()))]
# print(ls)
# We use set() to remove duplicates
# second_lowest = sorted(list(set([marks for name, marks in ls])))[1]
# print(second_lowest)
# print('\n'.join([name for name, marks in sorted(ls) if marks == second_lowest]))
# print(ls)



# ls = []
# for _ in range(int(input())):
    # name = input()
    # score = float(input())
    # One way to add element to a list
    # ls += [[name, score]]

# ls = sorted(ls, key = lambda x: x[1])
# print(ls)


# Method 2: Using dictionary
d = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    d[name] = score

scores = d.values()
print(d.values())
second_lowest = sorted(list(set(scores)))[1]
# One-liner
# print('\n'.join([key for key, value in sorted(d.items()) if value == second_lowest]))

new_list = []
print(d.items())
for key, value in d.items():
    if value == second_lowest:
        new_list.append(key)

# print(new_list.sort())        # new_list.sort() returns None
print('\n'.join([item for item in sorted(new_list)]))





