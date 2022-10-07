# Insieme di funzioni
import csv
import math

def dev_stand(db_list, index):
    """
    Calcola la deviazione standard di una lista di liste
    :param db_list: arg lista
    :param index: indice colonna
    :return: st_dev deviazione standard in 'float'
    """
    l_new = []
    for i in range(len(db_list)):
        if i != 0 and db_list[i][index] != '':  # non vogliamo l'header
            l_new.append(int(db_list[i][index]))
    mean = sum(l_new) / len(l_new)
    var = sum((l - mean) ** 2 for l in l_new) / len(l_new)
    st_dev = math.sqrt(var)
    #print("Standard deviation of {}: {}".format(db_list[0][index],round(st_dev,2)))
    return st_dev

def my_min(db_list, index):
    """
    Calcola il min di una lista di liste. Non considera i valori nulli
    :param db_list: arg lista
    :param index: indice colonna
    :return: m minimo della colonna
    """
    l_new = []
    for i in range(len(db_list)):
        if i != 0 and db_list[i][index] != '':                              # non vogliamo l'header né valori nulli
            l_new.append(float(db_list[i][index]))
    m = min(l_new)
    #print('Il valore minimo di {} è {}'.format(db_list[0][index],round(m,2)))
    return m


def my_max(db_list, index):
    """
    Calcola il max di una lista di liste. Non considera i valori nulli
    :param db_list: arg lista
    :param index: indice colonna
    :return: m minimo della colonna
    """
    l_new = []
    for i in range(len(db_list)):
        if i != 0 and db_list[i][index] != '':                              # non vogliamo l'header né valori nulli
            l_new.append(float(db_list[i][index]))
    m = max(l_new)
    #print('Il valore massimo di {} è {}'.format(db_list[0][index],round(m,2)))
    return m


def my_tot(db_list, index):
    """
    Calcola la somma totale di una lista di liste. Non considera i valori nulli
    :param db_list: arg lista
    :param index: indice colonna
    :return: m somma totale dei valori nella colonna
    """
    l_new = []
    for i in range(len(db_list)):
        if i != 0 and db_list[i][index] != '':                              # non vogliamo l'header né valori nulli
            l_new.append(float(db_list[i][index]))
    m = sum(l_new)
    #print('Il valore massimo di {} è {}'.format(db_list[0][index],round(m,2)))
    return m


def my_avg(db_list, index):
    """
    Calcola la media di una lista di liste. Non considera i valori nulli
    :param db_list: arg lista
    :param index: indice colonna
    :return: m media aritmetica
    """
    l_new = []
    for i in range(len(db_list)):
        if i != 0 and db_list[i][index] != '':                              # non vogliamo l'header né valori nulli
            l_new.append(float(db_list[i][index]))
    m = sum(l_new)/len(l_new)
    #print('La Media di {} è {}'.format(db_list[0][index],round(m,2)))
    return m


def mediana(db_list, index):
    """
    Calcola la mediana di una lista di liste. Non considera i valori nulli
    :param db_list: arg list
    :param index: indice colonna
    :return: median mediana dei valori nella colonna
    """
    l_new = []
    for i in range(len(db_list)):
        if i != 0 and db_list[i][index] != '':
           l_new.append(float(db_list[i][index]))

    lun = len(l_new)
    lundisp1 = int(lun/2)
    lundisp2 = int(lun/2 - 1)
    sort_price = l_new                              # lista ordinata dei prezzi

    if lun %2 == 0 :                                #se dati pari faccio media tra valori di indici len/2 e len/2 - 1
        median = (sort_price[lundisp1] + sort_price[lundisp2])/2
    else:
        median = sort_price[int(((lun - 1)/2))]     #se dati dispari prendo la metà del valore centrale nella lista ordinata

    #print('La Mediana di {} è {}'.format(db_list[0][index],round(median,2)))
    return median


def csv_to_list(file_path, delimiter=","):
    """
    Converte il mio dataset da formato .csv in lista
    :param file_path:
    :param delimiter:
    :return: db
    """
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        db = []
        for row in reader:
            db.append(row)
        #print("reader è di tipo ", type(reader))
    return db


def small_by_year(db_list, index, i_data, year):
    """
    Estrae una lista relativa ad un anno. Inoltre decido già quali colonne ricopiare
    :param db_list: arg list
    :param index: lista di indici relative alle colonne di mio interesse
    :param i_data: indice della colonna dove trovo la data in formato 'YYYY-MM-DD'
    :param year: anno che voglio considerare, scritto come stringa
    :return: nuovo dataset
    """
    nuova = []
    for i in range(0, (len(db_list))):
        var = db_list[i][i_data].split('-')           # split in ['year', 'month', 'day']
        if var[0] == year or i == 0 :
            riga = []
            for j in index:                             # itera solo per gli indici delle colonne che desidero
                riga.append(db_list[i][j])
            nuova.append(riga)                          # aggiungo la lista riga creata nel ciclo for più interno
            #print(riga)
    return nuova

def small_by_country(db_list, index, i_paese, paese):
    """
    Estrae una lista relativa a due paesi. Inoltre decido già quali colonne ricopiare
    :param db_list: arg list
    :param index: lista di indici relative alle colonne di mio interesse
    :param i_paese: indice della colonna dove trovo i paesi di mio interesse
    :param paese: lista di paesi che considero
    :return: nuovo dataset
    """
    nuova = []
    for i in range(0, (len(db_list))):
        var = db_list[i][i_paese]          # ['year', 'month', 'day']
        if var == paese[0] or var == paese[1] or i == 0 :
            riga = []
            for j in index:
                riga.append(db_list[i][j])
            nuova.append(riga)
            #print(riga)
    return nuova


def small_by_valor(db_list, i_valor, valor):
    """
    Estrae una lista relativa ad uno specifico valore stringa.
    :param db_list: arg list
    :param i_valor: indice della colonna dove trovo il valore di mio interesse
    :param valor: Valore da estrarre
    :return: nuovo dataset
    """
    nuova = []
    for i in range(0, (len(db_list))):
        var = db_list[i][i_valor]
        if var == valor or i == 0 :
            riga = []
            for j in range(0, (len(db_list[0]))):                   # itera solo per gli indici delle colonne che desidero
                riga.append(db_list[i][j])
            nuova.append(riga)                                      # aggiungo la lista riga creata nel ciclo for più interno
            #print(riga)
    return nuova