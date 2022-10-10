-- L’esercizio è mirato a prendere confidenza con le interrogazioni SL nella loro forma basilare. Dato
-- il seguente schema scrivere le interrogazioni di seguito:
--	AEROPORTO (Citta, Nazione, NumPiste)
--	VOLO (ldVolo, GiornoSett, CittaPart, OraPart, CittaArr, OraArr, TipoAereo)
--	AEREO (TipoAereo, NumPasseggeri, QtaMerci)

-- Le Citta con un aeroporto di cui non e noto il numero di piste;
select Citta from AEROPORTO where NumPiste IS NULL;

-- I tipi di aereo usati nei voli che partono da Torino;
select TipoAereo from VOLO where CittaPart = ‘Torino’;

-- Le città da cui partono voli diretti a Bologna
select CittaPart from VOLO where CittaArr = ‘Bologna’;

-- Le città da cui parte e arriva il volo con codice AZ274;
select CittaPart,CittaArr from VOLO where IdVolo = ‘AZ274’;

-- Il tipo di aereo, il giorno della settimana, l'orario di partenza la cui città di partenza inizia
-- per B e contiene O e la cui città di arrivo termina con A e contiene E
select TipoAereo, GiornoSett, OraPart from VOLO where CittaPart like ‘B%O%’ AND CittaArr like ‘%E%A’;
