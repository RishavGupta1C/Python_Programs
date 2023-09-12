# The tool .difference() returns a set with all the elements from the set that are not in an iterable.
# Your task is to find the total number of students who have subscribed to only English newspapers.

# d = {"Rank":1}
# print(type(d))
# print(d.values())

# >>> s = set("Hacker")
# >>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', 'H', 'k'])
# enumerate() adds a counter to an iterable and returns it.
# So enumerate(['R', 'a', 'n', 'k']) will create an enumerate object 
# with these values (0, 'R'), (1, 'a'), (2, 'n'), (3, 'k') which doesn't match with any s.

# >>> print s.difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'r'])
# {"Rank":1} is a dictionary so it doesn't match with any s.

# >>> s - set("Rank")
# set(['H', 'c', 'r', 'e'])


english_students = int(input())
english_rolls = set(input().split(' ', english_students)) # input set of strings
print(english_rolls)
french_students = int(input())
french_rolls = [i for i in input().split(' ', french_students)]	# input list of strings
print(french_rolls)
print(len(english_rolls.difference(french_rolls)))
