#Esercizio 3
Benz = float(input('Scrivi litri benzina serbatoio: '))
Eff = float(input('Scrivi efficienza carburante (km/l): '))
Prezzo = float(input('Scrivi prezzo benzina (€/l): '))
dis = 100               # km
costo = (dis/Eff)*Prezzo    #costo è dato dalla distanza percora su efficienza, moltiplicato poi per il prezzo
Km = Benz * Eff              #Km percorrebili con la bezina in serbatoio
print('Per 100 Km percorsi la spesa è di euro',costo)
print('La distanza percorrible con il carburante disponibile è:', Km,'Km')

print ("Il costo per 100 Km è {}, la distanza che può percorrere è {}".format(costo,Km))
