import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b]

a.sort()
b.sort()
result.sort()

print(a)
print(b)

print(result)
