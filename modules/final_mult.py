def multiplication():
  list1 = []
  tot = 1
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
  for x in list1:
    tot = tot*x
  print(("Multiplication is {}").format(tot)) 
  print()
  basic_math()