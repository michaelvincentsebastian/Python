'''
Fibonacci
'''
dev Fibonaci(length, firstValue):
    second = first+1

    fibo = []
    
    for i in range (1, length+1):
    nextValue = first+second
    first = second
    second = nextValue
    fibo.append(nextValue)
    
print(fibo)

length = int(input(" Row Length: ")) 
first = int(input(" first value: "))
fibonaci