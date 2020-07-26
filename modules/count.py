list= []
while True:
    el=input("Enter elements: ")
    if el== "exit":
        break
    else:
        list.append(el)
print("There are",len(list),"elements")
