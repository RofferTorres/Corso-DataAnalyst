#Esercizio 2
import random
X = 0
Y = 0
i = 0
while i < 100:
    S = random.randint(1, 10)   # Distanza casuale che compie ad ogni iterazione
    dir = random.randint(1, 4)   # 1 è Nord , 2 sud, 3 Est, 4 Ovest
    if dir == 1:
        Y = Y + S
    elif dir == 2:
        Y = Y - S
    elif dir == 3:
        X = X + S
    elif dir == 4:
        X = X - S
    i = i+1
print('La posizione finale è:',X,Y)

