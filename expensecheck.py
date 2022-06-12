
exp = -1
total = 0
maxexp = 0
minexp = 0
while exp != 0:
    exp = int(input("What is the expense? (Type 0 to stop) "))
    total += exp
    if exp > maxexp:
        maxexp = exp
        print(maxexp)
    if exp > 0: 
        minexp = exp

print("Total expenditure is: "+ str(total))

print("Maximum you spend is: " + str(maxexp))
print("Minimum you spend is: " + str(minexp))