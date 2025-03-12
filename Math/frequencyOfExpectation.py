'''
Frequency Of Expectations
'''
nA = int(input("enter the number of expected events: "))
nS = int(input("enter the multitude of possibilities: "))
noT = int(input("enter number of try: "))

probability = nA/nS
frequencyOfExpectation = probability * noT

print("Frequency Of Expectation: ",int(frequencyOfExpectation))