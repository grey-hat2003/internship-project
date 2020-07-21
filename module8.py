decimal= int(input("Enter Decimal Value: "))
convert =int(input("Convert to: [1]Binary, [2]Octal, [3]Hexadecimal"))
if convert==1:
    print("Converted to binary: ",bin(decimal))
elif convert==2:
    print("Converted to octal: ",oct(decimal))
elif convert==3:
    print("Converted to hexadecimal: ",hex(decimal))
else:
    print("Invalid Input")
