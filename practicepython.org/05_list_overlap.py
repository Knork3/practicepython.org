a = [1, 1, 2, 3, 5, 8, 13, 21, 34]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55]
result = []

if len(a) > len(b):
    longer = a
    shorter = b
else:
    longer = b
    shorter = a

for element in longer:
    if element in shorter and element not in result:
        result.append(element)

print(str(result))
