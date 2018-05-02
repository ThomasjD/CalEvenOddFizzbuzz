#Fizz Buzz
#Take input from user
number = int(input("Enter a number from 1-100."))
if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")

elif number%3 == 0 or number%5 == 0:
    if number%3 == 0:
        print("Fizz")
    else:
        print("Buzz")
else:
    print("No Fizz, Buzz, Fizzbuz for you!")
#if input is %3 then print Fizz
