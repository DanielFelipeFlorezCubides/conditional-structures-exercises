# Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
n = int(input('Give a number of numbers you wanna put: '))

numbersList = []

for i in range(n):
    number = int(input(f'Type the number {i+1}: '))
    numbersList.append(number)

numbersList.sort() # This function is to ordering the numbers in the list

print('The number list in order is: ')
for number in numbersList:
    print(number)