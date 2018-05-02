#Fizz Buzz
#Take input from user
number = int(input("Enter a number from 1-100."))
#if input is divisible by 3 & 5 then print Fizzbuzz
if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")

elif number%3 == 0 or number%5 == 0:
    if number%3 == 0:
        print("Fizz") #if input is %3 then print Fizz
    else:
        print("Buzz") #if input is %5 then print Fizz
else: #not divisible neither by 3 or 5
    print("No Fizz, Buzz, Fizzbuz for you!")
