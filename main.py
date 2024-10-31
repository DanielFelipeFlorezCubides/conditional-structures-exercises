# Escriba un programa que pida al usuario dos palabras, 
# y que indique cuál de ellas es la más larga y por cuántas letras lo es.

firstWord = input('Gimme a word: ')
secondWord = input('Gimme another word: ')

lenght_1 = len(firstWord)
lenght_2 = len(secondWord)

if lenght_1 > lenght_2:
    difference = lenght_1 - lenght_2
    print(f'The word {firstWord} has {difference} more letters than {secondWord}')
else:
    difference = lenght_2 - lenght_1
    print(f'The word {secondWord} has {difference} more letters than {firstWord}')