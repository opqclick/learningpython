user_name = str(input("What is your name? "))
user_age = int(input("How old are you? "))

yearsto50 = 50 - user_age

if yearsto50 > 0:
    print("Hello" + user_name + ", you will be 50 in " + str(yearsto50) + " years")
else:
    print("Hello" + user_name + ", you were 50 " + str(yearsto50) + " years ago")
    
print("bye")




