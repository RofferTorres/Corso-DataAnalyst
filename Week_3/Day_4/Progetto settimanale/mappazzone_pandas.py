import p_metodi
import pandas as pd

def queryby_pd(n=None):
    """
    Esegue le stesse specifiche query svolte attraverso l'altro metodo (cursori)
    :param n: numero [1-10] corrispondente al #query presente in main

    1 Best sellers,
    2 Categoria di prodotti più numerosa,
    3 Utente che ordina più frequentemente,
    4 Percentuale utenti che ricevono la newsletter,
    5 Quantità masterizzatori esterni stockati,
    6 Valore medio ordine,
    7 Percentuale di rivenditori tra gli utenti,
    8 Quantità ordini in elaborazione,
    9 Numero utenti con P.IVA,
    10 Quantità di prodotti Kingstone disponibili in magazzino

    :return: print del risultato
    """
    DBprog = 'ecommerce'

    if n == 1:
        df_prodotto = p_metodi.conn_by_pandas('prodotto', db=DBprog)
        df_orpr01 = p_metodi.conn_by_pandas('orpr01', db=DBprog)
        dftemp = df_orpr01.groupby('pid')['quantita', 'prezzo'].sum()  # sommo quantità e prezzo in base del product id
        dftemp.sort_values(by='quantita', ascending=False, inplace=True)  # ordine decrescente dei prodotti più venduti
        bseller_temp = dftemp.head(3).reset_index()
        df_merged = pd.merge(bseller_temp, df_prodotto[['pid', 'nome']], on='pid')  # join
        print('1) Best Sellers:\n', df_merged[['nome', 'quantita']].rename(columns={"nome": "Nome Prodotto", "quantita": "Quantità"}))  # by pandas

    elif n == 2:
        df_categoria = p_metodi.conn_by_pandas('categoria', db=DBprog)
        df_prodotto = p_metodi.conn_by_pandas('prodotto', db=DBprog)
        cat_max = df_prodotto['cid'].value_counts()  # conteggia n prodotti in base al category id
        cat_max = cat_max.head(1).reset_index()
        df_merged = pd.merge(cat_max, df_categoria, left_on="index", right_on="cid")  # join con df_categoria per ricavare anche il nome della categoria
        print('2) Categoria più numerosa\n',df_merged[['nome', 'cid_x']].rename(columns={"nome": "Categoria", "cid_x": "N_prodotti"}))

    elif n == 3:
        df_ordini = p_metodi.conn_by_pandas('ordine', db=DBprog)
        df_indirizzi = p_metodi.conn_by_pandas('indirizzo', db=DBprog)
        hz_ord = df_ordini['uid'].value_counts()  # conteggia n ordini in base al user id
        hz_ord = hz_ord.head(1).reset_index()
        df_merged = pd.merge(hz_ord, df_indirizzi, left_on="index",right_on="uid")  # join con df_indirizzi per ricavare anche nome e cognome
        print('3) Utente che ordina più di frequente.\n', df_merged[['nome', 'cognome', 'uid_x']].rename(columns={"nome": "Nome", "cognome": "Cognome", "uid_x": "N_ordini"}))

    elif n == 4 :
        df_utenti = p_metodi.conn_by_pandas('utente', db=DBprog)
        newsl = df_utenti['newsletter'].value_counts(normalize=True).head(1)  # frequenza di valori '1' in newsletter
        print("4) Percentuale di utenti che ricevono la newsletter.\n", newsl * 100)

    elif n == 5:
        df_categoria = p_metodi.conn_by_pandas('categoria', db=DBprog)
        df_prodotto = p_metodi.conn_by_pandas('prodotto', db=DBprog)
        qntm = df_categoria.loc[df_categoria['nome'] == 'MASTERIZZATORI ESTERNI']
        df_merged = pd.merge(qntm, df_prodotto[['cid', 'quantita']], on='cid')
        print("5) Quantità masterizzatori esterni rimasti in magazzino sono {}.".format(df_merged['quantita'].sum()))

    elif n == 6:
        df_orpr01 = p_metodi.conn_by_pandas('orpr01', db=DBprog)
        avg_ord = df_orpr01.groupby('oid')['prezzo', 'quantita'].sum()
        print("6) Il valore medio degli ordini effettuati è {} €".format(round(avg_ord["prezzo"].mean(), 2)))

    elif n == 7:
        df_utenti = p_metodi.conn_by_pandas('utente', db=DBprog)
        riv = df_utenti['lsid'].value_counts(normalize=True).tail(1)
        print("7) Percentuale di rivenditori tra gli utenti.\n", riv * 100)

    elif n == 8:
        df_ordini = p_metodi.conn_by_pandas('ordine', db=DBprog)
        df_stato = p_metodi.conn_by_pandas('stato', db=DBprog)
        stato = df_stato.loc[df_stato['stid'] == 1]
        df_merged = pd.merge(stato, df_ordini['stid'], on='stid')
        stato = df_merged.groupby('nome').count()
        print("8) Numero ordini attualmente in elaborazione.\n", stato)

    elif n == 9:
        df_utenti = p_metodi.conn_by_pandas('utente', db=DBprog)
        drop = df_utenti['piva'].dropna()
        iva = drop[drop.str.isnumeric()]
        n_piva = iva.count()
        print("9) N° utenti con P.IVA.", n_piva)

    elif n == 10:
        df_prodotto = p_metodi.conn_by_pandas('prodotto', db=DBprog)
        df_marca = p_metodi.conn_by_pandas('marca', db=DBprog)
        king = df_marca.loc[df_marca['nome'] == 'KING-STON']
        df_merged = pd.merge(king, df_prodotto[['mid', 'nome', 'quantita']], on='mid')
        brand = df_merged[['nome_x', 'quantita']].groupby('nome_x').sum()
        print("10) Quantità di prodotti Kingston presenti in magazzino.\n",brand)

    else:
        return None



