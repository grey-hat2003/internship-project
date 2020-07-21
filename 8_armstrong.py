number = input("\nenter a number: ")
digits = [int(x) for x in str(number)]
sum = 0
for digit in digits:
    sum += digit**3
if number == sum:
    print(str(number) + " is an armstrong number ")
else:
    print(str(number) + " is not an armstrong number ")



