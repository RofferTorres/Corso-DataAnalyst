-- Esercitazione D2W3
-- L'esercizio è mirato a prendere confidenza con le interrogazioni avanzate SQL che fanno uso di join, 
-- funzioni di aggregazione e ordinamenti. Dato il seguente schema scrivere le interrogazioni di seguito:
--	DISCO (NroSerie, TitoloAlbum,Anno, Prezzo) 
--	CONTIENE (NroSerieDisco, CodiceReg, NroProg) 
--	ESECUZIONE (CodiceReg, TitoloCanz, Anno) 
--	AUTORE (Nome, TitoloCanzone) 
--	CANTANTE (NomeCantante, CodiceReg) 


--	1. 	I cantautori(persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D';
select distinct AUTORE.Nome Cantautore
from ESECUZIONE, AUTORE, CANTANTE 
where (ESECUZIONE.TitoloCanz = AUTORE.TitoloCanzone) AND 
(CANTANTE.CodiceReg = ESECUZIONE.CodiceReg) AND 
(AUTORE.Cantautore = CANTANTE.NomeCantante) AND
(ESECUZIONE.TitoloCanz like ‘D%’);

--	2. 	I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione; 
select DISCO.TitoloAlbum Album
from DISCO,CONTIENE, ESECUZIONE
where DISCO.NroSerie = CONTIENE.NroSerieDisco AND 
CONTIENE.CodiceReg = ESECUZIONE.CodiceReg AND
ESECUZIONE.Anno IS NULL;


--	3. 	I cantanti che non hanno mai registrato una canzone come solisti; 
select distinct NomeCantante
from CANTANTE
where NomeCantante not in
	(select S1.NomeCantante
	from CANTANTE as S1
	where CodiceReg not in
		(select CodiceReg
		from CANTANTE S2
		where S2.NomeCantante <> S1.NomeCantante));

 
--	4.	I cantanti che hanno sempre registrato canzoni come solisti. (solo solisti)
select S1.NomeCantante
from CANTANTE as S1
where CodiceReg not in
	(select CodiceReg
	from CANTANTE S2
	where S2.NomeCantante <> S1.NomeCantante)
group by S1.NomeCantante having count(S1.NomeCantante) = 1;

