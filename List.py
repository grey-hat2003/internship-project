list = []
n = 0
n = int(input("Enter the number of elements : "))
print("Enter the elements")
for i in range(0,n):
    while True :
        try:
            list.append(int(input()))
            break
        except:
            print("only numbers are allowed please enter a number :")

print(list)
print("Largest Element :")
print(max(list))