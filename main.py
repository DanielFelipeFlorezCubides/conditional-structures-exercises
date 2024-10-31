# Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división. 
# El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /. 
# La salida del programa debe ser el resultado de la operación.

firstNumber = float(input('Type a number: '))
secondNumber = float(input('Type another one: '))
operation = input('Which operation do you wish to do? (+ , - , * , /): ')

if operation == '+':
    result  = firstNumber + secondNumber
    print(f'The result is: {result}')
elif operation == '-':
    result = firstNumber - secondNumber
    print(f'The result is: {result}')
elif operation == '*':
    result = firstNumber * secondNumber
    print(f'The result is: {result}')
else:
    result = firstNumber / secondNumber
    print(f'The result is: {result}')