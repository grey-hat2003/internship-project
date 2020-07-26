def mainMenu():
  print("1.Kilometers to Miles.")
  print("2.Celsius to Fahrenheit.")
  print("3.Feet to Meter.")
  print("4.Pounds to kilograms.")
  print("5.USD to INR.")
  print("6.Quit")
  selection=int(input("Enter Choice: "))
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
      print("Invalid input")
      mainMenu()
def metric():
    km=float(input("Enter units In kilometers: "))
    miles=km/1.609
    print(km,"km converted to",\
        format(miles,".3f"),"miles")

def temp():
    cel=float(input("Enter temperature in Celsius: "))
    fah= (cel*(9/5)+32)
    print(cel,"Celsius converted to",\
        format(fah,".1f"),"Fahrenheit")

def meter():
    feet=float(input("Enter unit in foot:"))
    meter=feet/3.281
    print(feet,"feet converted to",format(meter, ".3f"),"meter")

def kg():
    pound=float(input("Enter units in Pounds: "))
    kg=pound/2.205
    print(pound,"pound converted to",format(kg,".3f"),"kilograms")

def currency():
    USD=float(input("Enter units in USD($): "))
    INR=USD*74.77
    print(USD,"$ converted to", format(INR,"0.2f"),"INR(₹)")

mainMenu()
