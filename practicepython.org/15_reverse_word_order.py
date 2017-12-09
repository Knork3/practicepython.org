def ReverseWords():
    a = str(input("Bitte längeren String eingeben: \n"))
    x = a.split(" ")
    x.reverse()

    return " ".join(x)

print(ReverseWords())
