list1=[2,4,6,8,10]

list2=[1,3,5,7,9]

list3=[]

j,k=0,0

for i in range(len(list1)*2):

    if(i%2==0):

        list3.append(list1[j])

        j=j+1

    else :

       list3.append(list2[k])

       k=k+1

print(list3)









print([i.lower() for i in "HELLO"])










list1=[1,0,1,0,0,1]

list2=[23,45,78,99,88,32]

j=0

for i in range(len(list1)):

  if(list1[i]==1):

    num=list2[j]

    sum=0

    rem=0

    while(num>0):

      rem=num%10

      sum=sum*10+rem

      num=num//10

    list2[i]=sum

  j=j+1

print(list2)






def instr(str,start,end):

  return "".join(str[start:end])

name=list("GuviGeek")

print(instr(name,0,4))






list=[21,22,23,24,25]

for i in range(1,3):

  print(i)

  for j in range(1,6):

    print(j,end="")

  print()








# Type Error
# a=input("Enter a number:")
# to correct it 
a = int(input("Enter a number:"))
b=a*a

print("The square of number is:",b)




def dosomething(str):

  if len(str)==0:

    return str

  else:

    return dosomething(str[1:])+str[0]

name="GuviGeek"

print(dosomething(name))
