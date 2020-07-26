def addition():
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
  print("Sum of numbers is: ",sum(list1))
  print()
  basic_math()