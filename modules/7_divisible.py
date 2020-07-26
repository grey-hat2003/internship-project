number = input("\nenter a number: ")
divisor = input("\nenter a divisor: ")
if number % divisor == 0:
    print(str(number) + " is divisible by " + str(divisor))
else:
    print(str(number) + " is not divisible by " + str(divisor))
    