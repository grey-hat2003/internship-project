print("Convert from : 1.Decimal to octal,binary,hexadecimal\n               2.Octal,binary,Hexadecimal to Decimal\n")
inpu = int(input("Enter your choice : "))
def decimal():
    print("Convert to : \n")
    print("1.Binary\n2.Octal\n3.Hexadecimal")
    n = int(input("Enter your choice : "))
    number = int(input("Enter the Decimal number to be converted : " ))
    if n == 1 :
        list = []
        while number >= 1:
            remainder = number % 2
            number = number // 2
            list.append(remainder)
        prefix ='0b'
        list.append(prefix)
        list.reverse()
        binary = ''
        for element in list:
            binary += str(element)
        print("Converstion to binary is ",binary)
    elif n == 2 :
        list = []
        while number >= 1:
            remainder = number % 8
            number = number // 8
            list.append(remainder)
        prefix = '0o'
        list.append(prefix)
        list.reverse()
        octal = ''
        for element in list:
            octal += str(element)
        print("Converstion to octal is ", octal)
    elif n == 3 :
        list = []
        while number >= 1:
            remainder = number % 16
            number = number // 16
            if remainder == 10:
                remainder = 'A'
                list.append(remainder)
            elif remainder == 11 :
                remainder = 'B'
                list.append(remainder)
            elif remainder == 12 :
                remainder = 'C'
                list.append(remainder)
            elif remainder == 13 :
                remainder = 'D'
                list.append(remainder)
            elif remainder == 14 :
                remainder = 'E'
                list.append(remainder)
            elif remainder == 15 :
                remainder = 'F'
                list.append(remainder)
            else:
                list.append(remainder)
        prefix = '0x'
        list.append(prefix)
        list.reverse()
        hexadecimal = ''
        for element in list:
            hexadecimal += str(element)
        print("Converstion to Hexadecimal is ", hexadecimal)
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