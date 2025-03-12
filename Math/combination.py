''' 
Combination Calculation Program
'''
def nFactorial(n, factorial):
    for i in range(1, n+1):
        factorial = factorial*i
    return factorial
    
def rFactorial(r, factorial):
    for i in range(1, r+1):
        factorial = factorial*i
    return factorial
        
def nrFactorial(n, r, factorial):
    for i in range(1, n-r+1):
        factorial = factorial*i
    return factorial
    
n = int(input("enter total num of object: "))
r = int(input("enter total num of choosing: "))
factorial = 1

nFac = nFactorial(n, factorial)
rFac = rFactorial(r, factorial)
nminrFac = nrFactorial(n, r, factorial)
calculate = nFac/(rFac*nminrFac)

print("total combination: ",int(calculate))