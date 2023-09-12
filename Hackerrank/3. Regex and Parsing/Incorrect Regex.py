# Program to check whether a regular expression is correct or not.

import re

for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')





# Some regular expression codes

# Syntax - re.sub(pattern, repl, string, max=0)
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
# same as above. just we are not showing the end symbol as $ matches the ending position of the string.
num = re.sub(r'#.*', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print ("Phone Num : ", num)