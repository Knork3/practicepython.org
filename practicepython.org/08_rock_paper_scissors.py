from random import randint

options = ["stein", "schere", "papier"]
name = str(input("Bitte namen eingeben: "))

while True:
    p1 = str(input(name + ". Stein, Schere oder Papier: "))
    p2 = options[randint(0,2)]
    print("Computer wählt " + p2.capitalize())
    p1 = p1.lower()
    p2 = p2.lower()

    if p1 == "quit":
        break

    while True:
        if p1 not in options:
            print ("Ungültige Eingabe.")
            break
        elif p1 == p2:
            print ("Unentschieden!")
            break
        elif p1 == options[0] and p2 ==  options[1]:
            print (name + " hat gewonnen!")
            break
        elif p1 == options[1] and p2 == options[2]:
            print (name + " hat gewonnen!")
            break
        elif p1 == options[2] and p2 == options[0]:
            print (name + " hat gewonnen!")
            break
        else:
            print ("Computer hat gewonnen.")
            break
