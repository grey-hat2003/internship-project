list1=[]
tot=1
n=int(input("Enter number of elements: "))
for i in range(n):
    num=int(input("Enter numbers: "))
    list1.append(num)
    tot=tot*num
print("Multipliaction of numbers is: ",tot)
