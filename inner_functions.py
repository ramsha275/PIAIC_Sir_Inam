def calculator(num1, num2, op):
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    if op == '+':
        return add(num1, num2)
    elif op == '-':
        return subtract(num1, num2)


print(calculator(2, 3, '+'))
print(calculator(2, 3, '-'))

