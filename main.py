# TIME N DATE FUNCTION

def time():
    import datetime
    now=datetime.datetime.now()
    print(now.strftime("%d-%m-%y %H:%M:%S"))



# 1) UNIT CONVERTER FUNCTION
def unit_convert():
  time()
  print()
  
  def metric():
    km=float(input("Enter units in Kilometers: "))
    miles=km/1.609
    print(km,"km converted to",\
    format(miles,".3f"),"Miles")
    
    print()
    main()

  def temp():
    cel=float(input("Enter temperature in Celsius: "))
    fah= (cel*(9/5)+32)
    print(cel,"Celsius converted to",\
    format(fah,".1f"),"Fahrenheit")
    
    print() 
    main()

  def meter():
    feet=float(input("Enter unit in Feets: "))
    meter=feet/3.281
    print(feet,"Feet converted to",format(meter, ".3f"),"Metre")
    
    print() 
    main()

  def kg():
    pound=float(input("Enter units in Pounds: "))
    kg=pound/2.205
    print(pound,"Pound converted to",format(kg,".3f"),"Kilograms")
    
    print()
    main()

  def currency():
    USD=float(input("Enter units in USD($): "))
    INR=USD*74.77
    print(USD,"USD converted to", format(INR,"0.2f"),"INR")
    
    print()
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
  print()
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
    
    print()
    unit_convert()






# 2) QUADRATIC FUNCTION
import math
def quadratic():
  time()
  print()
    
 #input
  a,b,c = map(int,input("Enter a,b,c : ").split())

 #discriminant
  D = ((b**2)-(4*a*c))
  
  #for real and distinct roots
  if a == 0 :
    print("These are not quadratic coeeficients, try again")
    print()
    quadratic()
    
  else:
    if (D > 0) :
      print ("Roots are real and distinct")
      root1 = (-b + math.sqrt(D)) / (2*a)
      root2 = (-b - math.sqrt(D)) / (2*a)
      print("Root 1 = {:.3f} and root 2 = {:.3f} ".format(root1,root2))
      
      print()
      main()
        
    #for real and identical roots
    elif D == 0 :
      print("Roots are real and identical")
      root1 = -b / (2*a)
      print("Root = {:.3f}".format(root1))
      
      print()
      main()
  
    #for complex roots
    elif D < 0 :
      print("Roots are imaginary")
      rootreal = -b/(2*a)
      rootimg = math.sqrt(-D)/(2*a)
      print("Root 1 = {:.3f} + {:.3f}i and root 2 = {:.3f} - {:.3f}i".format(rootreal,rootimg,rootreal,rootimg))
      
      print()
      main()





# 3) LARGEST NUMBER FUNCTION
def largest():
  time()
  print()
  
  list = []
  n = 0
  n = int(input("Enter the number of elements: "))
  print("Enter the elements: ")
  
  for i in range(0,n):
    while True :
      try:
        list.append(int(input()))
        break
      except:
        print("only numbers are allowed please enter a number: ")
  
  print()
  print(list)
  print()
  print("Largest Element: ")
  print(max(list))
  
  print()
  main()





# 4) MULTIPICATION TABLE FUNCTION
def mult_tab():
  time()
  print()
  
  num = int (input("\nmultiplication table of: "))
  integer = int (input("\nexpected till: "))
  print()
  
  for x in range (1, integer+1):
    print(("{} X {} = {}").format(num, x, num*x))
  
  print()
  main()




# 5) NUMBER SYSTEM CONVERTER FUNCTION
def num_convert():
  time()
  print()
  
  print("Convert from : 1) Decimal to Octal, Binary, Hexadecimal")
  print("               2) Octal Binary, Hexadecimal to Decimal")
  print("               3) Main Menu")
  print()
  
  inpu = int(input("Enter your choice number: "))

  def decimal():
    print("Convert to : \n")
    print("1.Binary\n2.Octal\n3.Hexadecimal")
    print()
    
    n = int(input("Enter your choice : "))
    print()
    number = int(input("Enter the decimal number to be converted : " ))
    
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
      
      print()
      num_convert()
    
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

      print()
      num_convert()
    
    elif n == 3 :
      list = []
      
      while number >= 1:
        remainder = number % 16
        number = number // 16
        if remainder == 10:
          remainder = 'A'
          list.append(remainder)
        elif remainder == 11 :
          emainder = 'B'
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

      print()
      num_convert()
    
    else :
      print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")

      print()
      num_convert()

  def binary():
    print("Convert to Decimal from :\n")
    print("1) Binary\n2) Octal\n3) Hexadecimal")
    print()
    
    n = int(input("Enter yout choice number: "))
    print()
    number = input("Enter the non-decimal number to be converted: ")
    
    if n == 1 :
        print("Converstion from Binary to Decimal is ",int(number,2))
        print()
        num_convert()
    
    elif n == 2 :
        print("Conerstion from Octal to Decimal is ",int(number,8))
        print()
        num_convert()
    
    elif n == 3 :
        print("Converstion from Hexadecimal to Decimal is ",int(number,16))
        print()
        num_convert()
    
    else :
        print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
        print()
        num_convert()

  if inpu == 1:
    print()
    decimal()
  elif inpu == 2:
    print()
    binary()
  elif inpu == 3:
    print()
    main()
  else :
    print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
    print()
    num_convert()

    





# 6) BASIC MATH FUNCTION
def basic_math():
  time()
  print()
  
  list1 = []
  n = int(input("Enter number of elements: "))
  print()
  for i in range(n):
    while True:
      try:
        num = int(input("Enter number: "))
        list1.append(num)
        break
      except:
        print("That input was not numerical, please try again with a number")
  print()
  print("What you want to perform?")
  print("1) Addition")
  print("2) Subtraction")
  print("3) Multiplication")
  print("4) Subtraction with 2 lists")
  print("5) Main menu")
  print()
  
  opt = int(input("Enter option number: "))
  print()
  
  if opt == 1:
    print("Sum of numbers is: ",sum(list1))
    print()
    basic_math()
  
  elif opt == 2:
    diff = 0
    for x in list1:
      diff -= x
    print(("Subtraction is {}").format(diff))
    print()
    basic_math()
  
  elif opt == 3:
    tot = 1
    for x in list1:
      tot = tot*x
    print(("Multiplication is {}").format(tot)) 
    print()
    basic_math()
  
  elif opt == 4:
    list2 = []
    result = []
    print(("Enter {} elements").format(n))
    for x in range(n):
      while True:
        try:
          num = int(input("Enter number: "))
          list2.append(num)
          break
        except:
          print("That input was not numerical, please try again with a number")
    result = [list1[i] - list2[i] for i in range(n)]
    print(("The subtraction of the lists is {}").format(result))
    print()
    basic_math()
  
  elif opt == 5:
    print()
    main()
  
  else:
    print("!!!  INVALID INPUT, PLEASE TRY AGAIN  !!!")
    print()
    basic_math()

 

# 7) DIVISIBILITY TEST FUNCTION
def divisible():
  time()
  print()
  number = int(input("\nenter a number: "))
  divisor = int(input("\nenter a divisor: "))
  print()
  if number % divisor == 0:
    print(str(number) + " is divisible by " + str(divisor))
    print()
    main()
  else:
    print(str(number) + " is not divisible by " + str(divisor))
    print()
    main()



# 8) ARMSTRONG FUNCTION
def armstrong():
  time()
  print()
  number = int(input("\nenter a number: "))
  print()
  if number<0:
    print("That's a negative number, try again")
    print()
    armstrong()
  digits = [int(x) for x in str(number)]
  sum = 0
  for digit in digits:
    sum += digit**3
  if number == sum:
    print(str(number) + " is an armstrong number ")
    print()
  else:
    print(str(number) + " is not an armstrong number ")
    print()

  main()




def main():
  #main menu display
  print()
  print("_________________________________________________________________________________________________________________________________")
  print()
  print("---------------------------------------------------SOLVING MATH USING PYTHON-----------------------------------------------------")
  print()
  print("_________________________________________________________________________________________________________________________________")
  time()
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
