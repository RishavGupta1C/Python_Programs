S = input()
print(any(c.isalnum() for c in S))
print(c.isalnum() for c in S)
print([c.isalnum() for c in S])
print(any(c.isalpha() for c in S))
print(any(c.isdigit() for c in S))
print(any(c.islower() for c in S))
print(any(c.isupper() for c in S))


# method 2
S = input()
t = type(S)     # Here it gives str or String Object
for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    print(any(method(c) for c in S))