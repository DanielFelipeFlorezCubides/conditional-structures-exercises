# Escriba un programa que pida dos números enteros y que calcule la división, 
# indicando si la división es exacta o no.

dividend = int(input('Give me the number will be divided: '))
divisor = int(input('Give me the number will divide the other one: '))
remainder = dividend % divisor
quotient = dividend // divisor

if dividend % divisor == 0:
    print('The number is exactly divided')
else:
    print('The number cannot be exactly divided')

print(f'This is the quotient: {quotient}')
print(f'This is the remainder: {remainder}')