# n = 10
# for _ in range(0,n):
# 	n-=1
# 	print(n)
# # working with placeholders{} and format().
# text = "Order {item:} for {price:.2f} dollars only!"
# print(text.format(item = "Extra large pizza", price = 49))
# testVar = "Hello World!"
# print(testVar)


# favoriteShows = ['Panchayat', 'Mirzapur', 'Family Man']
# print("My favorite shows are : ")
# for i in favoriteShows:
# 	print("%s" %i)


# bookList = []
# running = True	
# while running == True:
# 	userInput = input("Book List \nType \"add\" to add a book \"list\" to list the book \"exit\" to exit the program:")

# 	if userInput.lower() == "add":
# 		userInput = input("Enter the name of the book: ")
# 		bookList.append(userInput)
# 	elif userInput.lower() == "list":
# 		if not bookList:
# 			print("Empty List\n")
# 		else:
# 			for i in bookList:
# 				print("%s\n" %i)
		
# 	elif userInput.lower() == "exit":
# 		running = False
# 	else:
# 		print("Invalid Input Command")

# print(bookList)

x = int(input())
y = int(input())
z = int(input())
n = int(input())
# list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
# print(list)


list = []
for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if (i+j+k) != n:
				list.append([i,j,k])

print(list)