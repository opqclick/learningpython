counter = 0

for number in range(1, 10):
    #print(number)
    if(number % 2 == 0):
      print(number, "This number is Even")
      counter += 1
    else:
      print(number, "This number is Odd")
     
print("Total Even number count is", counter)