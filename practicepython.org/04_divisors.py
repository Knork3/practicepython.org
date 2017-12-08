num = int(input("Please enter a number: "))
a = []

for element in range(1,num):
    if num % element == 0:
        a.append(element)

print(a)
