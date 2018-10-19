'''
Created on 08-Jun-2018

@author: Pritika
'''
import sqlite3

conn =sqlite3.connect('june8.sqlite')
cur = conn.cursor()

query ='select sqlite_version()'

query ='''
create table Person(
id integer primary key autoincrement,
first_name text,
last_name text,
age integer)
'''

query1 ='insert into Person(first_name, last_name, age) values (?,?,?)'
data_set=[['larry','will',3],
          ['john','brown',10],
          ['michelle','greene',35]]
#cur.executemany(query1, data_set)
conn.commit()
cur.close()
conn.close()

def edit_persons():
    conn =sqlite3.connect('june8.sqlite')
    cur = conn.cursor()
    
    query ='update * from Person'   
    cur.execute(query)
    
    column_names =[col_info[0] for col_info in cur.description]
    
    persons =[dict(zip(column_names,row)) for row in cur.fetchall()] 
    #print(cur.fetchone())
    #print(cur.fetchall())
    cur.close()
    conn.close()
    
    return persons

def select_all_persons():
    conn =sqlite3.connect('june8.sqlite')
    cur = conn.cursor()
    
    query ='select * from Person'   
    cur.execute(query)
    
    column_names =[col_info[0] for col_info in cur.description]
    
    persons =[dict(zip(column_names,row)) for row in cur.fetchall()] 
    #print(cur.fetchone())
    #print(cur.fetchall())
    cur.close()
    conn.close()
    
    return persons

if __name__ == '__main__':
    print(select_all_persons())