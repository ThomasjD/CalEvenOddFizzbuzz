#Calculator main module

#Get user input
first_num = float(input("Enter 1st number"))
operand = input("Enter operand!")
second_num = float(input("Enter 2nd number."))

#Calculation
import Calmodule.py
result = Calmodule.calculate(first_num, operand, second_num)
print(f"The result is {result}")
