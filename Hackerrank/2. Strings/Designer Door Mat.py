n, m = map(int, input().split())
# p = '.|.'
# def upper_part(n, m, p):
#     i = 0
#     while i<n//2:
#         x = 3*(2*i+1)
#         print(('-'*((m-x)//2)) + p*(2*i+1) + ('-'*((m-x)//2)))
#         i += 1

# def middle(m):
#     x = m//2-3
#     print(('-'*x) + 'WELCOME' + ('-'*x))

# def lower_part(n, m, p):
#     i = n//2
#     while i>0:
#         x = 3*(2*i-1)
#         print(('-'*((m-x)//2)) + p*(2*i-1) + ('-'*((m-x)//2)))
#         i -= 1

# upper_part(n, m, p)
# middle(m)
# lower_part(n, m, p)

pattern = [('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m,'-')] + pattern[::-1]))