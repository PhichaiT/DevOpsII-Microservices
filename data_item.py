import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_item.db")

def item_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT item, password , name
        FROM itemname 
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'item': row[0],
            'password': row[1],
            'name': row[2]
            }
        data.append(record)
    
    conn.close()
    return data

def find_itemname(item):
    ###
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT item, password , name
        FROM itemname 
        WHERE item=?
    """
    val = (item,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'item': rows[0],
        'password': rows[1],
        'name': rows[2]
        }
    data.append(record)
    
    conn.close()
    return data

def item_name_add(item,passwd,name):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO itemname(item,password,name)
        VALUES(?,?,?)
    """
    val = (item,passwd,name)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"

def item_delete(item):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM itemname
        WHERE item=?
    """
    val = (item,)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Deleted successfully"

def update_item(item,passwd,name):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE itemname
        SET password=? , name=?
        WHERE item=?
    """
    val = (passwd,name,item)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Update successfully"