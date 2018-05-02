#Math operands of calculator

def calculate(num1, operand, num2):
    if operand == '+':
        return num1 + num2
    elif operand == '-':
        return num1-num2
    elif operand == '/':
        return num1/num2
    else: #for * or x
        return num1 * num2
