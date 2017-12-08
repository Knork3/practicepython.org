num = int(input("Enter a number: "))
div = int(input("Enter a divisor (Enter 0 to skip): "))
if div > 0:
    if num % div == 0:
        print (str(num) + " is dividable by " + str(div))
    else:
        print (str(num) + " is not dividable by " + str(div))
else:
    if num % 2 == 0 and num % 4 == 0:
        print ("Quadruple Kill!")
    elif num % 2 == 0:
        print ("The number is even.")
    else:
        print ("The number is odd.")
