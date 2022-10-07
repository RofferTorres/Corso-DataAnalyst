import P_metodi
# dizionario con le path dei file che andrò ad usare
path={"Covid": "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\covid-data.csv", "Austria" : "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\Austria.csv", "Israel" : "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\Israel.csv", "Pop" : "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\population.csv"}

"""
E' stata svolta l'analisi relativa alla diffusione COVID-19 tra Austria e Israele, durante l'anno 2021. 
La scelta è stata ponderata in funzione di una popolazione ed una densità demografica simile tra loro.
Si valuterà in particolare la percentuale di vaccinati in rapporto alla popolazione e la mediana dei casi
totali confermati per milione di abitanti in funzione delle misure anti-covid prese dai rispettivi governi.
"""
# Estrazione dati dei dataset
vacc_Austria = P_metodi.csv_to_list(path["Austria"])      # index db [location 0, date 1, vaccine 2, url 3, total_vacc 4, people_vaccinated 5, people_fully_vaccinated 6, total_boosters 7
vacc_Austria = P_metodi.small_by_year(vacc_Austria, [1,4,5,6,7], 1, '2021')
db_covid = P_metodi.csv_to_list(path["Covid"])
db_covid_y = P_metodi.small_by_year(db_covid, [1,2,3,7,10,20,47], 3,'2021')
db_Aus = P_metodi.small_by_valor(db_covid_y,1, 'Austria')                 #index db [continent 0, location 1, date 2, total_deaths 3, total_cases_per_million 4, hosp_patients_per_million 5, stringency_index 6
db_Isr = P_metodi.small_by_valor(db_covid_y,1, 'Israel')

#print(db_Aus)
#print(db_Isr)

vacc_Israele = P_metodi.csv_to_list(path["Israel"])
vacc_Israele = P_metodi.small_by_year(vacc_Israele, [1,4,5,6,7], 1, '2021')

pop = P_metodi.csv_to_list(path["Pop"])
pop_list = P_metodi.small_by_country(pop,[0,3],0,['Austria','Israel'])   #
# print(pop_list)

# Prima analisi: Percentuale vaccinati su popolazione
max_vac_Aus =P_metodi.my_max(vacc_Austria, 2)
max2_va_Isr =P_metodi.my_max(vacc_Israele, 2)

percent_Aus = (max_vac_Aus/int(pop_list[1][1]))*100
percent_Isr = (max2_va_Isr/int(pop_list[2][1]))*100

print("\nNel 2021 la percentuale di vaccinati in {} è di {}%, mentre in {} la percentuale di vaccinati è di {}%".format(pop_list[1][0],round(percent_Aus, 2),pop_list[2][0],round(percent_Isr, 2)))

# Seconda analisi: mediana dei casi totali confermati per milione di abitanti ed indice misure anti-covid, da 0 (poco rigido) a 100 (molto rigido)
medianaAus = P_metodi.mediana(db_Aus, 4)
medianaIsr = P_metodi.mediana(db_Isr, 4)

rules_Aus = P_metodi.my_avg(db_Aus,6)
rules_Isr = P_metodi.my_avg(db_Isr,6)
#print(rules_Isr, rules_Aus)

print("\nLa mediana dei casi totali confermati per milione di abitanti in {} è di {} (casi/1M abitanti), mentre in {} è di {} (casi/1M abitanti)".format(pop_list[1][0],round(medianaAus, 0),pop_list[2][0],round(medianaIsr, 0)))
print('{} si dimostra essere il paese che ha adottato misure anti-covid più rigide tra i due paesi, con uno "stringency index" medio pari a {}.\n{} invece ha uno "stringency index" medio di {}, leggermente più basso ma sufficiente a contenere la diffusione del covid.'.format(pop_list[1][0],round(rules_Aus, 2),pop_list[2][0],round(rules_Isr,2)))