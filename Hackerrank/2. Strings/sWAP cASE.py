# def swap_case(s):
    # Method 1
    # str = ''
    # for element in s:
    #     if element.isupper():
    #         str += element.lower()
    #     elif element.islower():
    #         str += element.upper()
    #     else:
    #         str += element
    # return str


# Method 2
def swap_case(s):
    return s.swapcase()

string = input()
result = swap_case(string)
print(result)


# Method 3
# print(''.join([i.lower() if i.isupper() else i.upper() for i in input()]))


# Method 4
# print(input().swapcase())


# Method 5
# print(''.join(map(str.swapcase, input())))


# Method 6
# s = input()
# x = []
# for i in s:
#     if i.isupper():
#         i = i.lower()
#         x.append(i)
#     else:
#         i = i.upper()
#         x.append(i)
# print(''.join(x))