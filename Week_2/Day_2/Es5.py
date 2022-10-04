#Esercizio 5
var = input('Scrivi qualcosa: ')
if len(var) < 3:
    print('WARNING! Stringa inserita troppo corta.')
else:
    print(var[:3]+'...'+var[-3:])  #stampa primi 3 caratteri + '...'+ultimi 3 caratteri