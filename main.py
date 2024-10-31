# Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
# El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.

day = int(input('Type your birth day number: '))
month = int(input('Type your birth month number: '))
year = int(input('Type your birth year number: '))

currentDay = int(input('Type the current day number: '))
currentMonth = int(input('Type the current month number: '))
currentYear = int(input('Type the current year number: '))

old = currentYear - year
print(f'You are {old} years old')