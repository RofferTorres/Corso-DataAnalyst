import P_metodi
path={"Covid": "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\covid-data.csv", "Austria" : "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\Austria.csv", "Israel" : "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\Israel.csv", "Pop" : "D:\\vtrg1\Documents\Python\Epicode\Week_2\Day_4\Progetto\population.csv"}

"""
E' stata svolta l'analisi relativa alla diffusione COVID-19 tra il continente Sud America e il continente Europa.
La scelta è stata fatta per pura curiosità personale.
Si valuterà la percentuale di vaccinati in rapporto alla popolazione e la mediana dei casi
totali confermati per milione di abitanti in funzione delle misure anti-covid prese dai rispettivi governi.
"""
# Estrazione dati dei dataset
db_covid = P_metodi.csv_to_list(path["Covid"])
db_covid_y = P_metodi.small_by_year(db_covid, [1,2,3,7,10,20,35,47,48], 3,'2021')   #index db [continent 0, location 1, date 2, total_deaths 3, total_cases_per_million 4, hosp_patients_per_million 5, people_vacinated 6, stringency_index 7, population 8
db_SA = P_metodi.small_by_valor(db_covid_y,0, 'South America')
db_EU = P_metodi.small_by_valor(db_covid_y,0, 'Europe')
print(db_SA)

# Prima analisi: Percentuale vaccinati su popolazione
tot_vac_SA =P_metodi.my_tot(db_SA, 6)
tot_vac_EU =P_metodi.my_tot(db_EU, 6)

pop_SA =P_metodi.my_tot(db_SA, 8)
pop_EU =P_metodi.my_tot(db_EU, 8)

percent_SA = (tot_vac_SA/int(pop_SA))*100
percent_EU = (tot_vac_EU/int(pop_EU))*100

print("\nNel 2021 la percentuale di vaccinati in {} è di {}%, mentre in {} la percentuale di vaccinati è di {}%".format(db_SA[1][0],round(percent_SA, 2),db_EU[1][0],round(percent_EU, 2)))

# Seconda analisi: mediana dei casi totali confermati per milione di abitanti ed indice misure anti-covid, da 0 (poco rigido) a 100 (molto rigido)
medianaSA = P_metodi.mediana(db_SA, 4)
medianaEU = P_metodi.mediana(db_EU, 4)

rules_SA = P_metodi.my_avg(db_SA,7)
rules_EU = P_metodi.my_avg(db_EU,7)
#print(rules_EU, rules_SA)

print("\nLa mediana dei casi totali confermati per milione di abitanti in {} è di {} (casi/1M abitanti), mentre in {} è di {} (casi/1M abitanti)".format(db_SA[1][0],round(medianaSA, 0),db_EU[1][0],round(medianaEU, 0)))
print('{} si dimostra essere il paese che ha adottato misure anti-covid più rigide tra i due paesi, con uno "stringency index" medio pari a {}.\n{} invece ha uno "stringency index" medio di {}, leggermente più basso ma sufficiente a contenere la diffusione del covid.'.format(db_SA[1][0],round(rules_SA, 2),db_EU[1][0],round(rules_EU,2)))