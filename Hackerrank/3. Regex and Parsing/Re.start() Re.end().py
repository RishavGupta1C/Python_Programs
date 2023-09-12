import re

# S = input()
# k = input()
# anymatch = "No"
# # (...) -> Matches whatever regular expression is inside the parentheses, 
# # and indicates the start and end of a group
# for match in re.finditer(r'(?=('+k+'))', S, re.I):
#     print(match)
#     anymatch ="Yes"
#     print((match.start(1), match.end(1)-1))       # match.end([group]) and 1 is representing 1st paranthesized subgroup
# if anymatch == "No":
#     print((-1, -1))





# S = input()
# k = input()
# index = 0
# r = re.search(k, S, re.I)
# if not r:
#     print((-1, -1))
# while r:
#     ls = []
#     ls.append(index+r.start())
#     ls.append(index+r.end()-1)
#     print(tuple(ls))
#     index += r.start() + 1
#     # S = S[r.start()+1:]
#     # r = re.search(k, S, re.I)
#     r = re.search(k, S[index:], re.I)
#     print(S)




# index = 0
# if re.search(k, s):
#     while index+len(k) < len(s):
#         m = re.search(k, s[index:]) #begins search with new index
        
#         print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        
#         index += m.start() + 1 #assign new index by +1 
# else:
#     print((-1, -1))






# Using while-else
# index = 0
# m = re.search(k, S)
# while m:
#     m = re.search(k, S[index:]) #begins search with new index
#     print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
#     index += m.start() + 1 #assign new index by +1 
# else:
#     print((-1, -1))






S, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), S))     # positive lookahead asssertion. It starts with 0.
# matches = list(re.finditer(r'(?<={})'.format(k), S))  # positive lookbehind assertion. It starts with 1.
print(matches)
if matches:
    print('\n'.join(str((match.start(0),
          match.end(0) + len(k) - 1)) for match in matches))    # In theis match doesn't have paranthesized subgroup
else:
    print('(-1, -1)')











# if k in s:
# # * is a way to print list just like join()
#     print(*[(i.start(), (i.start()+len(k)-1)) for i in re.finditer(r'(?={})'.format(k), s)], sep='\n')
# else:
#     print('(-1, -1)')











# for i,x in enumerate(s):
#     if re.match(v,s[i:]):
#         print((i,i+len(v)-1))
# if re.search(v, s)==None:
#     print((-1,-1)) 
# i like this code, its simpler but can you explain why you wrote for i,x in enumerate(s) why x? there is no use of x here but if i remove it the code does not work
# The built-in function "Enumerate" allows you to keep a counter of the iterations, so in this case I only use that function to make life easier for me to solve the problem. Here the "i" is the counter and "x" is the value, even though you are not gonna use the value per se for any other operation, you can not iterate to the "s" without explicitly declaring the counter and value on the "for" loop as enumerate(s) will give you 2 values in each iteration, which, again, are the counter and the value.







# results = list(map(lambda x: (x.start(1), x.end(1)-1), re.finditer(r"(?=(%s))" % subs, s))) or [(-1, -1)]













# string = input()
# pattern = input()
# index = 0
# m = re.search(pattern, string)
# if m:
#     while index+len(pattern) < len(string):
#         m = re.search(pattern, string[index:])
#         print("({0}, {1})".format(index+m.start(), index+m.end()-1))
#         index += m.start()+1
# else:
#     print('(-1, -1)')


# import re
# S = input()
# k = input()
# pattern = re.compile(k)
# r = pattern.search(S)
# if not r:
#     print("(-1, -1)")
# while r:
#     print("({0}, {1})".format(r.start(), r.end() - 1))
#     r = pattern.search(S, r.start() + 1)
