def rev_sen(sen):
	words = sen.split(' ')
	reversed_sen = ' '.join(reversed(words))
	return reversed_sen

if __name__ == "__main__": 
    input1 = 'geeks quiz practice code'
    print (rev_sen(input1))


