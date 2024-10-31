# Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. 
# En caso que sea letra, determine si es mayúscula o minúscula.

type = input('Type a single character please: ')

if 'a' <= type <= 'z' or 'A' <= type <= 'Z':
    print("The character is a letter")
    if 'A' <= type <= 'Z':
        print('The charaacter is an upper case')
    else:
        print('The character is a lower case')
elif '0' <= type <= '9':
    print('The character is a number')
else:
    print('The character is not one of the options')