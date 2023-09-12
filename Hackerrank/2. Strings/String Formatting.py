number = 17

# Method 1
w = len(bin(number)[2:])
for i in range(1, number+1):
    print(str(i).rjust(w, ' '), str(oct(i)[2:].rjust(w, ' ')), str(hex(i)[2:].rjust(w, ' ').upper()), str(bin(i)[2:].rjust(w, ' ')))


# Method 2
n = int(input())
width = len('{:b}'.format(n))
for i in range(1, n+1):
    print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i, w = width))   # positional argument, keyword argument


