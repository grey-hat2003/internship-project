num = int (input("\nmultiplication table of: "))
integer = int (input("\nexpected till: "))
for x in range (1, integer+1):
  print(("{} X {} = {}").format(num, x, num*x))


