def fibonaci(length, first):
    second = first+1

    fibo = []
    
    for i in range (1, length+1):
        fibo.append(first)
        nextValue = first+second
        first = second
        second = nextValue 
    
    print(fibo)

length = int(input(" Row Length: ")) 
first = int(input(" first value: "))
fibonaci(length, first)