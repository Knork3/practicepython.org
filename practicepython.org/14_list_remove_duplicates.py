import random
x = []
for i in range(0,99):
    x.append(random.randint(1,10))

def remove_duplicates(a_list):
    a_list = [set(a_list)]
    return a_list

print(x)
print(remove_duplicates(x))
