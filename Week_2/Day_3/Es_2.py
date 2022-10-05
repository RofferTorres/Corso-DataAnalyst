# Esercizio 2
matrix = [ [], []]  # matrice [ [nomi_clienti], [valore_acquisti] ]
flag = 1            # valore usato come sentinella. Fine input se 0
i=0
while flag == 1:
    matrix[0].append(input("\nCustomer's name: "))
    matrix[1].append(float(input("Purchase value: € ")))
    if matrix[1][i] == 0:                           # conludo l'iserimento dei dati quando il prezzo inserito è 0
        del matrix[0][-1]                           # rimuovo i dati dell'ultimo cliente che non ha acquistato nulla
        del matrix[1][-1]
        print('\nStop write now. Wait...\n')
        flag = 0
    i += 1
# miglior cliente
i_max = matrix[1].index(max(matrix[1]))
print('"Best buyer" ==> {}: {}€ \n'.format(matrix[0][i_max].capitalize(), matrix[1][i_max]))
# peggior cliente
i_min = matrix[1].index(min(matrix[1]))
print('"Worst buyer" ==> {}: {}€ \n'.format(matrix[0][i_min].capitalize(), matrix[1][i_min]))
# media
avarage = sum(matrix[1])/len(matrix[1])
print('Customers spent on average: € {}\n'.format(avarage))
# mediana
len = int(len(matrix[1]))
sort_price = matrix[1][0:len]           # lista ordinata dei prezzi
if len %2 == 0 :                        #se dati pari faccio media tra valori di indici len/2 e len/2 - 1
    median = (sort_price[int(len/2)] + sort_price[int(len/2 - 1)])/2
else:
    median = sort_price[int(((len - 1)/2))]     #se dati dispari prendo la metà del valore centrale nella lista ordinata
print('Median is: € {}\n'.format(median))