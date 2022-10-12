import mysql.connector
import m_mysql

DB = 'discografia'
lista_autori = [('Metallica','The Unforgiven'),('Celentano','Azzurro'),('Foo Fighters','The Pretender'),('Linkin Park','Numb'),('Orietta Berti','Mille'),('Fedez','Mille'),('Celentano','A un passo da te'),('Mina','A un passo da te')]

try:
    conn = m_mysql.connection_database(db=DB)

    request = input("Il database in uso è '{}'.".format(DB.upper()) +"\nQuale operazione desidera effettuare?  [Query] [Insert] [Delete] [Free_query] ").upper()    #Tipo operazione da scegliere(Q/I/D/F)

    if request == 'Q':
        print("Risultato query già salvate:\n")
        q_es = {'query1':"select distinct autore.Nome Cantautore from esecuzione, autore, canzone where (esecuzione.TitoloCanz = autore.TitoloCanzone) AND (canzone.CodiceReg = esecuzione.CodiceReg) AND (autore.Cantautore = canzone.NomeCantante) AND (esecuzione.TitoloCanz like ‘D%’);",
                'query2':"select DISCO.TitoloAlbum Album from DISCO, CONTIENE, esecuzione where DISCO.NroSerie = CONTIENE.NroSerieDisco AND CONTIENE.CodiceReg = esecuzione.CodiceReg AND esecuzione.Anno IS NULL;",
                'query3':"select distinct NomeCantante from canzone where NomeCantante not in (select S1.NomeCantante from canzone as S1 where CodiceReg not in (select CodiceReg from canzone S2 where S2.NomeCantante <> S1.NomeCantante));",
                'query4':"select S1.NomeCantante from canzone as S1 where CodiceReg not in (select CodiceReg from canzone S2 where S2.NomeCantante <> S1.NomeCantante) group by S1.NomeCantante having count(S1.NomeCantante) = 1;"
                }

        # risultati delle query registrate in precedenza
        #q_es1 = m_mysql.query_wo_parameters(q_es['query1'], conn)
        #q_es2 = m_mysql.query_wo_parameters(q_es['query2'], conn)
        q_es3 = m_mysql.query_wo_parameters(q_es['query3'], conn)
        print('I cantanti che non hanno mai fanno un brano da solista sono: ',q_es3)
        q_es4 = m_mysql.query_wo_parameters(q_es['query4'], conn)
        print("I cantanti che hanno cantato da solisti sono :",q_es4)
        #m_mysql.print_result(q_es4)

    elif request == 'I':    # Inserimento dati nella tabella autore
        print("\nSono stati inseriti i dati della lista_autori")
        new_authors = m_mysql.list_to_author('autore', lista_autori, conn)
        query_stmt = "SELECT * FROM %s;" % 'autore'
        q_test = m_mysql.query_wo_parameters(query_stmt, conn)
        #print(q_test)

    elif request == 'D':
        tbl_del = input('\nScegli tabella in cui cancellare i dati (autore, cazone): ')
        delete_in_autore = m_mysql.delete_row_table(tbl_del, input("Elemento da eliminare: "), conn)    # Cancella riga relativa al un valore inserito

    elif request == 'F':
        free_query = m_mysql.query_wo_parameters(input("\nScrivi o copy&paste (come unica riga) la query che desideri: "), conn)     #query inserita manualmente
        print(free_query)
    else:
        print("Valore input non riconosciuto. RUN AGAIN!")

    conn.close()

except mysql.connector.errors.DataError as db_error:
    print(db_error.msg)
    sys.exit()