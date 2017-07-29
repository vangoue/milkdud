mylist=[]

print(mylist)
usr= int(input("how many number do you want"))
for x in range(0,usr):
    print("what is the next number please")
    numbers= int (input("enter a number"))
    mylist.append(numbers)
print(mylist)
mylist.sort()
print(mylist)
print(mylist[0])
mylist.reverse()
print (mylist)
print(mylist[0])