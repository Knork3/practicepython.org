def get_number(prompt):
    return int(input(prompt))

def is_prime(number):
    if number > 1:
        if len(a) == 0:
            print(str(number) + " ist eine Primzahl!")
        else:
            print (str(number) + " ist keine Primzahl.")

number = get_number("Nummer eingeben: ")

a = [x for x in range(2,number) if number % x == 0]

is_prime(number)
