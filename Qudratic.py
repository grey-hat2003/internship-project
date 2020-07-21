import math
def quadratic():
    #input
    a,b,c = map(int,input("Enter a,b,c :").split())
    #discriminant
    D = ((b**2)-(4*a*c))
    #for real and distinct roots
    if (D > 0) :
        print ("Roots are real and distinct:")
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print("Root 1 = {:.3f} and root 2 = {:.3f} ".format(root1,root2))
    #for real and identical roots
    elif D == 0 :
        print("Roots are real and identical :")
        root1 = -b / (2*a)
        print("Root = {:.3f}".format(root1))
    #for complex roots
    elif D < 0 :
        print("Roots are imaginary:")
        rootreal = -b/(2*a)
        rootimg = math.sqrt(-D)/(2*a)
        print("Root 1 = {:.3f} + {:.3f}i and root 2 = {:.3f} - {:.3f}i".format(rootreal,rootimg,rootreal,rootimg))

quadratic()