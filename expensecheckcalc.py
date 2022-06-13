exp = []
stopped = False

while not stopped:
    e = int(input("What is your expense (type 0 to stop) "))
    if e != 0:
        exp.append(e)
    else:
        stopped = True
print(exp)
print("Total expenses: ", sum(exp))
print("Max expense: ", max(exp))
print("Min expense: ", min(exp))
