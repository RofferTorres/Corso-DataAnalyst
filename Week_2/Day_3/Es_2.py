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
# mediana""""
len= int(len(matrix[1]))
if len %2 == 0 :
    median = (matrix[1][int(len/2)] + matrix[1][int(len/2 - 1)])/2
else:
    median = matrix[1][int(((len - 1)/2))]
print('Median is: € {}\n'.format(median))