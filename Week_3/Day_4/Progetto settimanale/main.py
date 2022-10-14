# Progetto settimana 3
"""
 Ideazione interrogazioni per base di dati di una web app relativa ad un e-commerce
 di prodotti informatici, sviluppo applicazione in Python con connessione a DBMS MySQL
 con Pandas e con il connettore, implementazione interrogazioni ideate tramite funzioni
 ad-hoc. Vincolo: proporre almeno 10 interrogazioni identiche, sia utilizzando i DataFrame
 di Pandas che utilizzando i cursori. Il database è fornito in input.
"""
import p_metodi
import mappazzone_pandas
import mysql.connector

"""
    La presenza di due foreign keys nella tabella prodotto ha reso impossibile 
    l'inserimento dei dati 'prodotto'. Come soluzione al problema è stata 
    creata una tabella temporanea senza vincoli su uno schema 'testdb', nel 
    quale si sono importati tutti i dati prodotto forniti nella traccia.
    In seguito si sono estratti tutti i valori distinti e non nulli
    dalle colonne 'cid' e 'mid' per poi inserirli nel database 'ecommerce', 
    rispettivamente nelle colonne categoria.mid e marca.mid. 
    
    Completata questa piccola operazione ho imposto flag = 1 così che non ripeta
    la copia di questi dati e vada avanti con il resto del progetto.
"""
DBtest = 'testdb'
DBprog = 'ecommerce'

flag = 1            # flag 0 esegue la copia dei cid e mid; flag 1 copia già eseguita
if flag == 0:
    try:
        conn = p_metodi.connection_database(db=DBtest)
        q_cid = 'select distinct cid from prodotto where cid is not null;'
        q_mid = 'select distinct mid from prodotto where mid is not null;'
        cid = p_metodi.query_wo_parameters(q_cid, conn)         # estrazione dei cid presenti nella tabella testdb.prodotto
        mid = p_metodi.query_wo_parameters(q_mid, conn)
        conn2 = p_metodi.connection_database(db=DBprog)
        # inserisco i dati appena estratti all'interno  di categoria.cid e marca.mid
        print(cid)
        insert_to_category = p_metodi.list_to_column('categoria', 'cid', cid, conn2)
        print(mid)
        insert_to_brand = p_metodi.list_to_column('marca', 'mid', mid, conn2)
        conn2.close()
        conn.close()

    except mysql.connector.errors.DataError as db_error:
        print(db_error.msg)
        sys.exit()

# Elenco di 10 query a scelta. Eseguite e risolte prima tramite l'ausilio di pandas
# ed in seguito tramite l'uso dei cursori
try:
    conn = p_metodi.connection_database(db=DBprog)

    #1 Best sellers
    qpd1 = mappazzone_pandas.queryby_pd(1)
    query = "select p.nome Prodotto, sum(y.quantita) from (select x.nome, x.pid from prodotto x) as p right join " \
            "(select o.pid, o.quantita from orpr01 o) as y on y.pid = p.pid group by p.pid order by sum(y.quantita) desc limit 3;"
    bseller_query = p_metodi.query_wo_parameters(query, conn)  # query inserita manualmente
    print("\n[Cursor]\nBest Sellers:\n{} {}\n{} {}\n{} {}\n".format(bseller_query[0][0], bseller_query[0][1], bseller_query[1][0], bseller_query[1][1], bseller_query[2][0], bseller_query[2][1],))

    #2 Categoria di prodotti più numerosa
    qpd2 = mappazzone_pandas.queryby_pd(2)
    query = "select c.nome Categoria, x.N_prodotti from categoria c right join (select p.cid, count(p.cid) N_prodotti " \
            "from prodotto p group by p.cid order by count(p.cid) desc limit 1) as x on x.cid = c.cid;"
    cat_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nCategoria più numerosa è {} con {} prodotti.\n".format(cat_query[0][0],cat_query[0][1]))

    #3 Utente che ordina più frequentemente
    qpd3 = mappazzone_pandas.queryby_pd(3)
    query = "select i.nome Nome, i.cognome Cognome, x.Hz_ord N_ordini from indirizzo i right join " \
            "(select o.uid, count(o.uid) Hz_ord from ordine o group by o.uid order by count(o.uid) desc limit 1) as x" \
            " on x.uid = i.uid;"
    hz_ordquery = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\n{} {} ha ordinato più di frequente.\n".format(hz_ordquery[0][0],hz_ordquery[0][1]))

    #4 Percentuale utenti che ricevono la newsletter
    qpd4 = mappazzone_pandas.queryby_pd(4)
    query = "select *, n.newsl/sum(n.newsl)*100 perc from (SELECT count(u.newsletter) newsl FROM utente u " \
            "GROUP BY u.newsletter) as n;"
    newsl_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nPercentuale di utenti che ricevono la newsletter è {} %\n".format(round(newsl_query[0][1]), 2))

    #5 Quantità masterizzatori esterni stockati
    qpd5 = mappazzone_pandas.queryby_pd(5)
    query = "select sum(p.quantita) Qnt from prodotto p right join (select c.nome, c.cid from categoria c " \
            "where c.nome = 'MASTERIZZATORI ESTERNI') as x on x.cid = p.cid;"
    qntm_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nQuantità masterizzatori esterni rimasti in magazzino sono {}.\n".format(qntm_query[0][0]))

    #6 Valore medio ordine
    qpd6 = mappazzone_pandas.queryby_pd(6)
    query = "select avg(x.tot) from (select sum(o.prezzo) tot from orpr01 o group by o.oid order by sum(o.prezzo)) as x;"
    avg_ord_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nIl valore medio degli ordini effettuati è {} €\n".format(round(avg_ord_query[0][0],2)))

    #7 Percentuale di rivenditori tra gli utenti
    qpd7 = mappazzone_pandas.queryby_pd(7)
    query = " select (1-riv/sum(riv))*100 perc from(SELECT u.lsid, count(u.lsid) riv FROM utente u GROUP BY u.lsid) as x"
    riv_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nPercentuale di rivenditori tra gli utenti è {} %\n".format(round(riv_query[0][0], 2)))

    #8 Quantità ordini in elaborazione
    qpd8 = mappazzone_pandas.queryby_pd(8)
    query = "select x.nome Stato, count(o.stid) N_ordini from ordine o right join (select s.stid, s.nome from stato s " \
            "where s.nome like '%elab%') as x on x.stid = o.stid;"
    stato_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nNumero ordini attualmente in {} sono {}\n".format(stato_query[0][0],round(stato_query[0][1], 2)))

    #9 Numero utenti con P.IVA
    qpd9 = mappazzone_pandas.queryby_pd(9)
    query = "select count(piva) from utente where piva REGEXP '^[0-9]+$';"
    iva_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nN° utenti con P.IVA: {}\n".format(iva_query[0][0]))

    #10 Quantità di prodotti Kingstone disponibili in magazzino
    qpd10 = mappazzone_pandas.queryby_pd(10)
    query = "select x.marca Nome, sum(quantita) Qnt from prodotto p right join (select m.nome marca, m.mid " \
            "from marca m where m.nome like 'KING%STON') as x on x.mid = p.mid;"
    brand_query = p_metodi.query_wo_parameters(query, conn)
    print("\n[Cursor]\nSono presenti in magazzino {} prodotti {}.\n".format(brand_query[0][1],brand_query[0][0]))


except mysql.connector.errors.DataError as db_error:
    print(db_error.msg)
    sys.exit()


