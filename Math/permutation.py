'''
Permutation Calculation
'''
def nFactorial(n, factorial):
    for i in range(1, n+1):
        factorial = factorial*i
    return factorial
    
def nrFactorial(n, r, factorial):
    for i in range(1, n-r+1):
        factorial = factorial*i
    return factorial
    
n = int(input("enter total number of objects: "))
r = int(input("enter number of objects selected: "))
factorial = 1

nFac = nFactorial(n, factorial)
nrFac = nrFactorial(n, r, factorial)
permutation = nFac/nrFac

print("permutation: ",int(permutation))