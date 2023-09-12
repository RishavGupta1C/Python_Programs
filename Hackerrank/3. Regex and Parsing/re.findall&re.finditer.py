import re

# method 1

# vowels = "aeiou"
# consonants = "qwrtypsdfghjklzxcvbnm"
# match = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), input(), re.I)
# # re.I = re.IGNORECASE and (?<=[expression])[pattern]  -> positive lookbehind
# print('\n'.join(match or ['-1']))






# method 2
consonants = "[qwrtypsdfghjklzxcvbnm]"
# a = re.findall(r'(?<=' + consonants + ')([aeiou]{2,})' + consonants, input(), re.I)
pattern = re.compile(r'(?<=' + consonants + ')([aeiou]{2,})' + consonants, re.I)
b = [match for match in pattern.finditer(input())]
print(b)
# print('\n'.join(a or ['-1']))





# text = "He was carefully disguised but captured quickly by police."

# regEX = r"\w+ly"
# pattern = re.compile(regEX)

# search = pattern.search(text)
# print(search)
# print(type(search))
# print()

# findall = pattern.findall(text)
# print(findall)
# print(type(findall))
# print()

# finditer = pattern.finditer(text)
# print(finditer)
# print(type(finditer))
# print()
# for anObject in finditer:
#     print(anObject)
#     print(type(anObject))
#     print()




# Method 3
# syntax for positive lookahead is demonstrated below: 
# to the right of your pattern you insert the opening parenthesis followed by a question mark and an equals sign.
# [pattern](?=
# S = input()
# v_pattern = 'AEIOU'
# c_pattern = 'QWRTYPSDFGHJKLZXCVBNM'
# substr = re.findall(r'(?<=['+c_pattern+'])(['+v_pattern+']{2,})(?=['+c_pattern+'])', S, re.I)


# match = re.search(r'^b\w+', 'ball')
# print(match.group())
# string = "purple alice-b@google.com monkey dishwasher"
# match = re.search(r'[\w.-]+@[\w.-]+', string)
# if match:
#     print(match.group())

