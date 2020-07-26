def difference2():
  list1 = []
  list2 = []
  result = []
  
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
  
  print(("Enter {} elements for 2nd list").format(n))
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
