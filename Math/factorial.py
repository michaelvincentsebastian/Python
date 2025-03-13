def nFactorial(n, factorial):
    for i in range(1, n+1):
        factorial = factorial*i
    return factorial

n = int(input("enter an number: "))
factorial = 1
fac = nFactorial(n, factorial)
print(fac)