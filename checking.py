# n = int(input())
# integer_list = map(int, input().split()[:n]) #to work with only first n inputs
# print(n)
# for i in integer_list:
# 	print(i)
# print(type(integer_list))	# class map
# my_tuple = tuple(integer_list)
# print(hash(my_tuple))


# n = range(-5,5)
# l = list(filter(lambda x: x<0, n))
# print(l)


# from functools import reduce
# m = set(range(1,5))
# print(m)
# product = reduce((lambda x, y: x * y), m)
# print(product)



# name=list("GuviGeek")

# i=0;

# temp=''

# name1=''

# m=(len(name)//2)-1

# for j in range(len(name)-1,m,-1):

# 	if i<j:

# 		temp=name[i]

# 		name[i]=name[j]

# 			name[j]=temp

# 	i+=1

# 	name1="".join(name)

# print(name1[::-1])


# a = int(input())
# sum = 0
# while(a>0):
#     rem = a%10
#     sum = sum*10 + rem
#     a = a // 10

# print(sum)





# Python program to find length of the longest valid 
# substring   
def findMaxLen(string): 
    n = len(string) 
  
    # Create a stack and push -1 
    # as initial index to it. 
    stk = [] 
    stk.append(-1) 
  
    # Initialize result 
    result = 0
  
    # Traverse all characters of given string 
    for i in range(n): 
  
        # If opening bracket, push index of it 
        if string[i] == '(': 
            stk.append(i) 
          
        # If closing bracket, i.e., str[i] = ')' 
        else:    
  
            # Pop the previous opening bracket's index 
            if len(stk) != 0: 
               stk.pop() 
  
            # Check if this length formed with base of 
            # current valid substring is more than max 
            # so far 
            if len(stk) != 0: 
                result = max(result,  
                             i - stk[len(stk)-1]) 
  
            # If stack is empty. push current index as 
            # base for next valid substring (if any) 
            else: 
                stk.append(i) 
  
    return result 
  
  
# Driver code 
string = "))(())"
  
# Function call 
print(findMaxLen(string))
  
# string = "()(()))))"
  
# # Function call 
# print findMaxLen(string) 
  

