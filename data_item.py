import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_item.db")

def item_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price, instock
        FROM item
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock':row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def find_itemname(item):
    ###
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price, instock
        FROM item
        WHERE name=?
    """
    val = (item,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'name': rows[0],
        'category': rows[1],
        'price': rows[2],
        'instock':rows[3]
        }
    data.append(record)
    
    conn.close()
    return data

def item_name_add(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO item(name,category,price,instock)
        VALUES(?,?,?,?)
    """
    val = (name,category,price,instock)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"

def item_delete(item):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM item
        WHERE name=?
    """
    val = (item,)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Deleted successfully"

def update_item(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE item
        SET category=? , price=?, instock=?
        WHERE name=?
    """
    val = (category,price,instock,name)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Update successfully"