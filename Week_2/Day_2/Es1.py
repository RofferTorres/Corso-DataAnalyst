# Esercizio 1
str_input = input('Scrivi una frase: ')
new = ''
i = 0
while i < len(str_input):
    if str_input[i] != 'a' and str_input[i] != 'e' and str_input[i] != 'i'and str_input[i] != 'o' and str_input[i] != 'u':      # se input di indice i diverso da vocale lo trasforma in maiuscolo
        old = str_input[i]
        new = new + old.upper()
    else:                                                                                                                        #altrimenti ricopio il carattere di indice i così com'è
        new = new+str_input[i]
    i = i + 1
print(new)

