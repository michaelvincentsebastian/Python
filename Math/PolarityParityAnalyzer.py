def EvenOddNegativePositive(num):
    if (num%2 == 0):
        if (num>0):
            print ("Even Number is Positive")
        elif (num<0):
            print ("Even Number is Negative")
        else:
            print ("Zero")
    elif (num%2 != 0):
        if (num>0):
            print ("Even Number is Positive")
        elif (num<0):
            print ("Odd Number is Negative")
        else:
            print ("Zero")
            
num = int(input("Enter a Number in Integer: "))
EvenOddNegativePositive(num)