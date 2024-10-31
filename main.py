# Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

number = int(input('Hello please type an integer number: '))

if number % 2 == 0:
    print('Is a pair number')
else:
    print('is an odd number')