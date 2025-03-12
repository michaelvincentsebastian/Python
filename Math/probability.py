'''
Probability Calculation
'''
nA = int(input("enter the number of expected events: "))
nS = int(input("enter the multitude of possibilities: "))

probability = nA/nS
inPercent = probability * 100

print("Probability: ",int(inPercent),"%")