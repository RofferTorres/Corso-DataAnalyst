# Esercizio 1
str_input = input('Scrivi una frase a piacere: ')
#conversione consonanti in maiuscolo
str_2 = str_input.upper()
str_2 = str_2.replace('A', 'a').replace('E', 'e').replace('I', 'i').replace('O', 'o').replace('U', 'u')
print(str_2)
split = str_input.split(' ')  # lista di parole date in input
d = {}
t = tuple()
for word in split:                          # iterazione sulle parole nella lista 'split'
    for char in word:                       # iterazione sulle lettere per ogni parola
        if char.islower() == True:          # attributo islower verifica se la lettera è minuscola
            if char in d.keys():
                t_old = d[char]             # Copio il valore della key su t_old se esiste già
            else:
                t_old = t                   # t_old uguale tuple vuoto se non esiste ancora la key
            t_new =  t_old + (word, )
            d[char] = tuple(set(t_new))     # rimuovo eventuali duplicati e li assegno alla key
print(d)


