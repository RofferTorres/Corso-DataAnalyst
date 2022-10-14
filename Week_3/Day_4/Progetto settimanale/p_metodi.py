import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

def connection_database(u='root', psw='Pssmysql', h='127.0.0.1', db=''):
    """
    Permette la connessione al database che desidero. Di default sono presenti le mie credenziali.
    :param u: username
    :param psw: password
    :param h: indirizzo server
    :param db: nome database
    :return: c
    """
    try:
        c = mysql.connector.connect(user=u, password=psw, host=h, database=db)
        return c
    except mysql.connector.errors.DataError as db_error:
        print(db_error.msg)
        return None


def conn_by_pandas(tbl=None, u='root', psw='Pssmysql', h='127.0.0.1', db=''):
    """
    Ulteriore metodo di connessione al database. In questo caso ottengo un dataframe.
    Di default sono presenti le mie credenziali.
    :param tbl: nome tabella che desidero convertire in dataframe
    :param u: username
    :param psw: password
    :param h: indirizzo server
    :param db: nome database
    :return: result, dataframe per pandas
    """
    try:
        db_connection_str = 'mysql+pymysql://%s:%s@%s/%s' % (u, psw, h, db)
        db_connection = create_engine(db_connection_str)
        result = pd.read_sql(tbl, db_connection)
        # print(prodotto)
        return result
    except mysql.connector.errors.DataError as db_error:
        print(db_error.msg)
        return None


def query_wo_parameters(q='', c=None, type_fetch='fetchall'):
    """
    Esegue ogni tipo di query 'select' a partire dalla query completa inserita come stringa.
    :param q: stringa della query scritta su un unica riga
    :param c: conn variabile della connessione al databse
    :param type_fetch: modo in cui varranno raccolti i dati dal cursore
    :return: result, risultato query sotto forma di lista di tuple
    """
    cursor = c.cursor()
    cursor.execute(q)
    if type_fetch == 'fetchall':
        result = cursor.fetchall()
    elif type_fetch == 'fetchone':
        result = cursor.fetchone()
    else:
        result = cursor.fetchmany()

    return result


def close_connection(conn):
    conn.close()


def list_to_category(t=None, l=None, c=None):
    """
    Metodo specifico per l'inserimento di una lista di tuple all'interno della tabella 't'
    nel database 'ecommerce'
    :param t: nome tabella
    :param l: lista che desidero inserire
    :param c: conn variabile della connessione al databse
    :return: result, risultato dell'insert
    """
    cursor = c.cursor()
    sql = "INSERT INTO `ecommerce`.`%s` (`cid`)" % t
    sql = sql + " VALUES (%s);"
    try:
        cursor.executemany(sql, l)
        c.commit()
        print(cursor.rowcount, "record inserted.")
        result = cursor.fetchall()
        return result
    except:
        c.rollback()



def list_to_column(t=None, col=None, l=None, c=None):
    """
    Metodo specifico per l'inserimento di una lista di tuple all'interno della tabella 't', nella colonna 'col' e
    nel database 'ecommerce'
    :param t: nome tabella
    :param col: nome colonna
    :param l: lista che desidero inserire
    :param c: conn variabile della connessione al databse
    :return: result, risultato dell'insert
    """
    cursor = c.cursor()
    sql = "INSERT INTO `ecommerce`.`%s` (`%s`)" % (t, col)
    sql = sql + " VALUES (%s);"
    try:
        cursor.executemany(sql, l)
        c.commit()
        print(cursor.rowcount, "record(s) inserted.")
        result = cursor.fetchall()
        return result
    except:
        c.rollback()



def delete_row_table(t=None, n=None, c=None):
    """
    Metodo specifico per la cancellazione di una riga all'interno della tabella 't', nel databse 'discografia'
    :param t: nome tabella
    :param n: record colonna 'nome'
    :param c: record colonna 'TitoloCanzone'
    :return: result, risultato del delete
    """
    cursor = c.cursor()
    sql = "DELETE FROM `discografia`.`%s` WHERE (`nome` = '%s') or (`TitoloCanzone` = '%s');" % (t, n, n)
    try:
        cursor.execute(sql)
        c.commit()
        print(cursor.rowcount, "record(s) deleted.")
        result = cursor.fetchall()
        return result
    except:
        c.rollback()





