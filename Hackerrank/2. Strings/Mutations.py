# Stirngs are immutable

# >>> string[5] = 'k' 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment



# Two ways to change string

# ONE: convert the string to a list and then change the value.
# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra


# TWO: slice the string and join it back.
# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra



def mutate_string(string, position, character):
    ls = list(string)
    ls[position] = character
    return ''.join(ls)
    # return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)