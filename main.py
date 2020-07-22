# 1) UNIT CONVERTER FUNCTION
def unit_convert():
  def metric():
    km=float(input("Enter units in Kilometers: "))
    miles=km/1.609
    print(km,"km converted to",\
    format(miles,".3f"),"Miles")
      
    main()

  def temp():
    cel=float(input("Enter temperature in Celsius: "))
    fah= (cel*(9/5)+32)
    print(cel,"Celsius converted to",\
    format(fah,".1f"),"Fahrenheit")
      
    main()

  def meter():
    feet=float(input("Enter unit in Feets:"))
    meter=feet/3.281
    print(feet,"Feet converted to",format(meter, ".3f"),"Metre")
      
    main()

  def kg():
    pound=float(input("Enter units in Pounds: "))
    kg=pound/2.205
    print(pound,"Pound converted to",format(kg,".3f"),"Kilograms")
      
    main()

  def currency():
    USD=float(input("Enter units in USD($): "))
    INR=USD*74.77
    print(USD,"USD converted to", format(INR,"0.2f"),"INR")

    main()
  
  print("1) Kilometers to Miles")
  print()
  print("2) Celsius to Fahrenheit")
  print()
  print("3) Feet to Meter")
  print()
  print("4) Pounds to Kilograms")
  print()
  print("5) USD to INR")
  print()
  print("6) Quit")
  selection=int(input("Enter Choice number: "))
  if selection==1:
    metric()
  elif selection==2:
    temp()
  elif selection==3:
    meter()
  elif selection==4:
    kg()
  elif selection==5:
    currency()
  elif selection==6:
    exit()
  else:
    print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
    unit_convert()
      
    main()





# 2) QUADRATIC FUNCTION
import math
def quadratic():
    #input
  a,b,c = map(int,input("Enter a,b,c :").split())
    
    #discriminant
  D = ((b**2)-(4*a*c))
    
    #for real and distinct roots
  if (D > 0) :
    print ("Roots are real and distinct:")
    print()
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Root 1 = {:.3f} and Root 2 = {:.3f} ".format(root1,root2))
    main()
    
    #for real and identical roots
  elif D == 0 :
    print("Roots are real and identical :")
    print()
    root1 = -b / (2*a)
    print("Common Root = {:.3f}".format(root1))
    main()
    
    #for complex roots
  elif D < 0 :
    print("Roots are imaginary:")
    print()
    rootreal = -b/(2*a)
    rootimg = math.sqrt(-D)/(2*a)
    print("Root 1 = {:.3f} + {:.3f}i and Root 2 = {:.3f} - {:.3f}i".format(rootreal,rootimg,rootreal,rootimg))
    main()





# 3) LARGEST NUMBER FUNCTION
def largest():
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
  main()





# 4) MULTIPICATION TABLE FUNCTION
def mult_tab():
  num = int (input("\nmultiplication table of: "))
  integer = int (input("\nexpected till: "))
  for x in range (1, integer+1):
    print(("{} X {} = {}").format(num, x, num*x))

  main()




# 5) NUMBER SYSTEM CONVERTER FUNCTION
def num_convert():
  print("Convert from : 1) Decimal to Octal, Binary, Hexadecimal")
  print("               2) Octal Binary, Hexadecimal to Decimal")
  print("               3) Main Menu")
  print()
  inpu = int(input("Enter your choice number: "))

  def decimal():
    print("Convert Decimal to : \n")
    print("1) Binary\n2) Octal\n3) Hexadecimal")
    print()
    n = int(input("Enter your choice number: "))
    print()
    number = int(input("Enter the Decimal number to be converted : " ))
    if n == 1 :
        print("Converstion to Binary is ", bin(number))
        num_convert()
    elif n == 2 :
        print("Converstion to Octal is ",oct(number))
        num_convert()
    elif n == 3 :
        print("Converstion to Hexadecimal is ",hex(number))
        num_convert()
    else :
        print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
        num_convert()

  def binary():
    print("Convert to Decimal from :\n")
    print("1) Binary\n2) Octal\n3) Hexadecimal")
    print()
    n = int(input("Enter yout choice number: "))
    number = input("Enter the non-decimal number: ")
    if n == 1 :
        print("Converstion from Binary to Decimal is ",int(number,2))
        num_convert()
    elif n == 2 :
        print("Conerstion from Octal to Decimal is ",int(number,8))
        num_convert()
    elif n == 3 :
        print("Converstion from Hexadecimal to Decimal is ",int(number,16))
        num_convert()
    else :
        print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
        num_convert()

  if inpu == 1:
    decimal()
  elif inpu == 2:
    binary()
  elif inpu == 3:
    main()
  else :
    print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
    num_convert()

    





# 6) BASIC MATH FUNCTION
def basic_math():
  list = []
  n = int(input("Enter number of elements: "))
  for i in range(n):
    num = int(input("Enter numbers: "))
    list.append(num)
  print("What you want to perform?")
  print("1) Addition")
  print("2) Subtraction")
  print("3) Multiplication")
  print("4) Main menu")
  opt = int(input("Enter option number:"))
  
  if opt == 1:
    print("Sum of numbers is: ",sum(list))
    basic_math()
  
  elif opt == 2:
    diff = 0
    for x in list:
      diff -= x
    print("Subtraction is {}".format(diff))
    basic_math()
  
  elif opt == 3:
    tot = 1
    for x in list:
      tot = tot*x
    print("Multiplication is {}".format(tot)) 
    basic_math()
  
  elif opt == 4:
    main()
  
  else:
    print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")

 

# 7) DIVISIBILITY TEST FUNCTION
def divisible():
  number = int(input("\nenter a number: "))
  divisor = int(input("\nenter a divisor: "))
  if number % divisor == 0:
    print(str(number) + " is divisible by " + str(divisor))
    main()
  else:
    print(str(number) + " is not divisible by " + str(divisor))
    main()



# 8) ARMSTRONG FUNCTION
def armstrong():
  number = int(input("\nenter a number: "))
  digits = [int(x) for x in str(number)]
  sum = 0
  for digit in digits:
    sum += digit**3
  if number == sum:
    print(str(number) + " is an armstrong number ")
  else:
    print(str(number) + " is not an armstrong number ")

  main()




def main():
  #main menu display
  print()
  print("_________________________________________________________________________________________________________________________________")
  print()
  print("---------------------------------------------------SOLVING MATH USING PYTHON-----------------------------------------------------")
  print()
  print("_________________________________________________________________________________________________________________________________")
  print()
  print("         1) Unit converter")
  print()
  print("         2) Quadratic equation solver")
  print()
  print("         3) Finding the largest number from your input") 
  print()
  print("         4) Multiplication table calculator")
  print()
  print("         5) Number system converter") 
  print()
  print("         6) Basic math operations")
  print()
  print("         7) Divisibility test")
  print()
  print("         8) Armstrong's number")
  print()
  print("         9) Exit")
  print()
  
  #main menu selection if else ladder
  choice = int(input("    CHOOSE YOUR DESIRED OPTION NUMBER AND ENTER IT: "))
  print()
  print("_________________________________________________________________________________________________________________________________")
  print()
  if choice == 1:
    unit_convert()
  elif choice == 2:
    quadratic()
  elif choice == 3:
    largest()
  elif choice == 4:
    mult_tab()
  elif choice == 5:
    num_convert()
  elif choice == 6:
    basic_math()
  elif choice == 7:
    divisible()
  elif choice == 8:
    armstrong()
  elif choice == 9:
    exit()
  else:
    print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
    
    main()

#EXECUTION
main()