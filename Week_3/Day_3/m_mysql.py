import mysql.connector

def connection_database(u='root',psw='Pssmysql',h='127.0.0.1', db=''):
    try:
        c = mysql.connector.connect(user=u, password=psw, host=h, database=db)
        return c
    except mysql.connector.errors.DataError as db_error:
        print(db_error.msg)
        return None

def query(select, frm, where='None', grouby='None',order='None'):
    stmt = "select %s from %s" % (select,frm)
    if where is not None:
        stmt = stmt +" where %s" % where
    if grouby is not None:
        stmt = stmt + " group by %s" % grouby
    if order is not None:
        stmt= stmt + " order by %s" % order
    return stmt

"""def print_result(cursor):
    for i in cursor.fetchall():
        print(i)"""

def query_wo_parameters(q='',c=None ,type_fetch='fetchall'):
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


def list_to_author(t=None,l=None,c=None):
    """

    :param t:
    :param l:
    :param c:
    :return:
    """
    cursor = c.cursor()
    sql = "INSERT INTO `discografia`.`%s` (`nome`, `TitoloCanzone`)" % t
    sql = sql + " VALUES (%s, %s);"
    cursor.executemany(sql,l)
    c.commit()
    print(cursor.rowcount, "record inserted.")
    result = cursor.fetchall()
    return result

def delete_row_table(t=None ,n=None ,c=None):
    """

    :param t:
    :param n:
    :param c:
    :return:
    """
    cursor = c.cursor()
    sql = "DELETE FROM `discografia`.`%s` WHERE (`nome` = '%s') or (`TitoloCanzone` = '%s');" % (t,n, n)
    cursor.execute(sql)
    c.commit()
    print(cursor.rowcount, "record(s) deleted.")
    result = cursor.fetchall()
    return result

