list = []
n = 0
n = int(input("Enter the number of elements : "))
print("Enter the elements")
for i in range(0,n):
    list.append(input())

print(list)
print("Largest Element :")
print(max(list))