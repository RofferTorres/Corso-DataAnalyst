-- Esercitazione D2W3
-- L'esercizio è mirato a prendere confidenza con le interrogazioni avanzate SQL che fanno uso di join, funzioni di aggregazione e ordinamenti. Dato il seguente schema scrivere le interrogazioni di seguito:
--	DISCO (NroSerie, TitoloAlbum,Anno, Prezzo) 
--	CONTIENE (NroSerieDisco, CodiceReg, NroProg) 
--	ESECUZIONE (CodiceReg, TitoloCanz, Anno) 
--	AUTORE (Nome, TitoloCanzone) 
--	CANTANTE (NomeCantante, CodiceReg) 


--	1. 	I cantautori(persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D';
select distinct AUTORE.Nome Cantautore
from ESECUZIONE, AUTORE, CANTANTE 
where (ESECUZIONE.TitoloCanz like ‘D%’) AND 
(ESECUZIONE.TitoloCanz = AUTORE.TitoloCanzone) AND 
(CANTANTE.CodiceReg = ESECUZIONE.CodiceReg) AND 
(AUTORE.Cantautore = CANTANTE.NomeCantante);

--	2. 	I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione; 
select DISCO.TitoloAlbum Album
from DISCO, ESECUZIONE
where ESECUZIONE.Anno IS NULL;

--	3. 	I cantanti che non hanno mai registrato una canzone come solisti; 
select distinct CANTANTE.NomeCantante Cantante_non_solista
from ESECUZIONE, CANTANTE
where ESECUZIONE.CodiceReg = CANTANTE.CodiceReg
group by CANTANTE.CodiceReg having count(CANTANTE.CodiceReg) > 1;

 
--	4.	I cantanti che hanno sempre registrato canzoni come solisti.
select distinct CANTANTE.NomeCantante Cantante_solista
from ESECUZIONE, CANTANTE
where ESECUZIONE.CodiceReg = CANTANTE.CodiceReg
group by CANTANTE.CodiceReg having count(CANTANTE.CodiceReg) = 1;
