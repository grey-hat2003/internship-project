print("Convert from : 1.Decimal to octal,binary,hexadecimal\n               2.Octal,binary,Hexadecimal to Decimal\n")
inpu = int(input("Enter your choice : "))
def decimal():
    print("Convert to : \n")
    print("1.Binary\n2.Octal\n3.Hexadecimal")
    n = int(input("Enter your choice : "))
    number = int(input("Enter the Decimal number to be converted : " ))
    if n == 1 :
        print("Converstion to binary is ", bin(number))
    elif n == 2 :
        print("Converstion to octal is ",oct(number))
    elif n == 3 :
        print("Converstion to hexadecimal is ",hex(number))
    else :
        print("invalid choice ")

def binary():
    print("Convert from :\n")
    print("1.Binary\n2.Octal\n3.Hexadecimal")
    n = int(input("Enter yout choice  : "))
    number = input("Enter the number : ")
    if n == 1 :
        print("Converstion from binary to decimal is ",int(number,2))
    elif n == 2 :
        print("Conerstion from octal to decimal is ",int(number,8))
    elif n == 3 :
        print("Converstion from hexadecimal to decimal is ",int(number,16))
    else :
        print("Invalid choice : ")


if inpu == 1 :
    decimal()
elif inpu == 2 :
    binary()
else :
    print("invalid Choice")