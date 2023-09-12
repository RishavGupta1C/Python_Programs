# The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
# Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

english_students = int(input())
english_rolls = set(input().split(' ', english_students)) # input set of strings
print(english_rolls)
french_students = int(input())
french_rolls = input().split(' ', french_students)	# input list of strings
print(french_rolls)
print(len(english_rolls.symmetric_difference(french_rolls)))


# students subscribed to english and french newspaper
# E intersection F = E U F - E.symmetric_difference(F)
union_newspapers = english_rolls.union(french_rolls)
s_difference_newspaper = english_rolls.symmetric_difference(french_rolls)
print(len(union_newspapers.difference(s_difference_newspaper))) # intersection
print(len(english_rolls.intersection(french_rolls))) # intersection using intersection