# El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. 
# En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

# Un partido de tenis se divide en sets. 
# Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. 
# Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, 
# el set se define en un último juego, en cuyo caso el resultado final es 7-6.

# Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

# si A ganó el set, o
# si B ganó el set, o
# si el set todavía no termina, o
# si el resultado es inválido (por ejemplo, 8-6 o 7-3).
# Desarrolle un programa que solucione el problema de Solarrabietas:

# Definimos el número de juegos ganados por los jugadores A y B
juegos_a = int(input('Type the wins number for A: '))
juegos_b = int(input('Type the wins number for B: '))

# Comprobamos si los resultados son válidos
if juegos_a < 0 or juegos_b < 0 or juegos_a > 7 or juegos_b > 7:
    resultado = "Invalid result"
elif juegos_a >= 8 or juegos_b >= 8:
    resultado = "Invalid result"
    
# Comprobamos si A ganó el set
elif juegos_a >= 6 and (juegos_a - juegos_b) >= 2 or juegos_a == 7:
    resultado = "A wins the game"

# Comprobamos si B ganó el set
elif juegos_b >= 6 and (juegos_b - juegos_a) >= 2 or juegos_b == 7:
    resultado = "B wins the game"

# Comprobamos si hay empate a 6
elif juegos_a == 6 and juegos_b == 6:
    resultado = "The set is tie to 6"
    
# Comprobamos si hay empate a 5
elif juegos_a == 5 and juegos_b == 5:
    resultado = "The set is tie to 5"
    
# Si no se ha ganado el set
else:
    resultado = "The game doesn't finish yet"

# Imprimimos el resultado
print(resultado)