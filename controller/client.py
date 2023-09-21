import sys

sys.path.insert(1, 'service')

import connecttionpos as con

def insert(fullname, email, age):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "Insert into person(fullname, email, age) VALUES(%s, %s, %s)"
    cursor.execute(sql, (fullname, email, age))
    conn.commit()
    cursor.close()


def select_all():
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "SELECT * from  person"
    cursor.execute(sql)
    result = cursor.fetchall()
    rows = [['ID', 'FullName', 'Email', 'Age', 'Date']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows


def select_by_id(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "SELECT * from  person where id = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    rows = [['ID', 'FullName', 'Email', 'Age', 'Date']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows

def update( fullname , email , age , id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "UPDATE person SET fullname = %s , email = %s , age = %s WHERE id = %s"
    cursor.execute(sql , (fullname, email , age , id))
    conn.commit()
    cursor.close()

def delete(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "DELETE FROM person WHERE id = %s"
    cursor.execute(sql , (id,))
    conn.commit()
    cursor.close()
