s = input()
# This solution is not right as we can't include multiple spaces in between as present in the original string.
# new_str = ''
# for x in string.split():
#     new_str += x.capitalize() + ' '
# new_str.strip()



# Method 1 : Not Efficient
for string in s.split():
    s = s.replace(string, string.capitalize())
# new_str.strip()
print(s)


# Method 2 : Best Method
print(' '.join(word.capitalize() for word in s.split(' ')))
# If sep is given, consecutive delimiters are not grouped together and 
# are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2'])
# In case of (' '.join()) :-
# If there are 5 spaces then we will have 4 empty strings and 
# between all 4 empty strings we will have spaces i.e, 5 spaces.




# Method 3 : importing string
import string
print(string.capwords(s, ' '))
