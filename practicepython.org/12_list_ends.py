import random
def get_first_4_and_last(a):
    return [a[0], a[len(a)-1]]
x = random.sample(range(100), 20)
print(x)
print(str(get_first_4_and_last(x)))
