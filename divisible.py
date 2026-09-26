print("Enter the value(numerator)")
numN= int(input())
print("Enter the value(denominator)")
numD= int(input())

if numN % numD== 0:
    print("\n" +str(numN)+"is divisible by" +str (numD))
else:
    print("\n"+str(numN)+"is not divisible by"+str (numD)) 
