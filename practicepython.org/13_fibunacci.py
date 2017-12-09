def fibunacci(i):
    fib = [1, 1]

    for element in range(0,i):
        fib.append(fib[element] + fib[element+1])
    return fib

fib = []
while True:
    x = int(input("How many Fibonacci-Numbers to calc? (0 = quit): "))
    if x == 0:
        break
    else:
        for element in fibunacci(x-2):
            if element > 0:
                fib.append(element)
                print (element)
