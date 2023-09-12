# Checking leap year

# year = int(input())
year = 1980
# Method 1: Using ternary operator
# leap = True if not year%400 else False if not year%100 else True if not year%4 else False
leap = True if year%400==0 else False if year%100==0 else True if year%4==0 else False
print(leap)


# Method 2:
# if not year%400:
#     leap = True
# elif not year%100:
#     leap = False
# elif not year%4:
#     leap = True
# else:
#     leap = False

# print(leap)

