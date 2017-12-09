from random import randint
guess = 0
number = randint(1, 9)
count = 0


while guess != number and guess != "exit":
    guess = input("Rate die Zahl (1-9): ")
    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print ("Zu niedrig.")
    elif guess > number:
        print ("Zu hoch.")
    else:
        print ("Korrekt! Sie haben " + str(count) + " Versuche benötigt.")
