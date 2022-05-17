import sqlite3

def create_tables():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS locomotive_types
            (
            locomotive_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );''')
    conn.commit()
    conn.execute('''CREATE TABLE IF NOT EXISTS client
            (
            client_id  INTEGER PRIMARY KEY NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
            );''')
    conn.commit()
    conn.execute('''CREATE TABLE IF NOT EXISTS gender
            (
            gender_id INTEGER PRIMARY KEY NOT NULL ,
            gender_name TEXT NOT NULL
            );''')
    conn.commit()    
    conn.execute('''CREATE TABLE IF NOT EXISTS carriage_types
            (
            carriage_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );''')
    conn.commit()   
    conn.execute('''CREATE TABLE IF NOT EXISTS client_document_types
            (
            client_document_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );''')
    conn.commit()  
    conn.execute('''CREATE TABLE IF NOT EXISTS trains
            (
            train_id INTEGER PRIMARY KEY NOT NULL,
            train_name TEXT NOT NULL
            );''')
    conn.commit()
    conn.execute('''CREATE TABLE IF NOT EXISTS geo_entities
            (
            geo_entity_id INTEGER PRIMARY KEY NOT NULL,
            geo_entity_name TEXT NOT NULL
            );''')
    conn.commit()
    conn.execute('''CREATE TABLE IF NOT EXISTS routes
            (
            route_id INTEGER PRIMARY KEY NOT NULL,
            route_name TEXT NOT NULL
            );''')
    conn.commit()    

def fill_locomotive_types():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into locomotive_types(type_name) values('�������');''')
    conn.execute('''insert into locomotive_types(type_name) values('����������');''')
    conn.execute('''insert into locomotive_types(type_name) values('����������');    ''')
    conn.commit()
    conn.close()      

def fill_client():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into client(username,password,email) values('Harry','fhgd786','Harry.@mail.ru');''')
    conn.execute('''insert into client(username,password,email) values('Endrew','kjhert65','Endrew.@mail.ru');''')
    conn.execute('''insert into client(username,password,email) values('lambert','vbnm76','Elenamber.@mail.ru');    ''')
    conn.execute('''insert into client(username,password,email) values('Peter','gjkrt845','Lizborn.@mail.ru');    ''')  
    conn.commit()
    conn.close() 

def fill_gender():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into gender(gender_name) values('attack helicopter');''')
    conn.execute('''insert into gender(gender_name) values('murlock');''')
    conn.execute('''insert into gender(gender_name) values('watermelon');   ''')
    conn.commit()
    conn.close()   

def fill_carriage_types():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into carriage_types(type_name) values('����');''')
    conn.execute('''insert into carriage_types(type_name) values('��������');''')
    conn.execute('''insert into carriage_types(type_name) values('��������');    ''')
    conn.commit()
    conn.close()  
    
def fill_client_document_types():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into client_document_types(type_name) values('�������');''')
    conn.execute('''insert into client_document_types(type_name) values('������������� � ��������');''')
    conn.execute('''insert into client_document_types(type_name) values('������ �������');    ''')
    conn.commit()
    conn.close()  
    
def fill_trains():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into trains(train_name) values('THOMAS');''')
    conn.execute('''insert into trains(train_name) values('PROXIMA');''')
    conn.execute('''insert into trains(train_name) values('O.L.E.G.');    ''')
    conn.commit()
    conn.close()   

def fill_geo_entities():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into geo_entities(geo_entity_name) values('������');''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('������');''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('���������� �������');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('�����������');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('�����');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('������');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('��� ������');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('��� ������');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('��� ������');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('��������');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('�����');    ''')
    conn.execute('''insert into geo_entities(geo_entity_name) values('������� �������');    ''')
    conn.commit()
    conn.close()
    
    
def fill_():
    conn = sqlite3.connect('railwaysFB.db')
    conn.execute('''insert into locomotive_types(type_name) values('�������');''')
    conn.execute('''insert into locomotive_types(type_name) values('����������');''')
    conn.execute('''insert into locomotive_types(type_name) values('����������');    ''')
    conn.commit()
    conn.close()  



def check_tables():
    conn = sqlite3.connect('railwaysFB.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table';''')
    res = cursor.fetchall()
    for r in res:
        print(r)
    
def db_init():    
    create_tables()
    check_tables()
    fill_locomotive_types()
    fill_client()
    fill_gender()
    fill_carriage_types()
    fill_client_document_types()
    fill_trains()
    fill_geo_entities()

from os.path import exists
if not exists('railwaysFB.db'):
    db_init()
conn = sqlite3.connect('railwaysFB.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM client;''')
res = cursor.fetchall()
for r in res:
    print(r)
    
from os.path import exists
if not exists('railwaysFB.db'):
    db_init()

conn = sqlite3.connect('railwaysFB.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM locomotive_types;''')
res = cursor.fetchall()
for r in res:
    print(r)
    
from os.path import exists
if not exists('railwaysFB.db'):
    db_init()
conn = sqlite3.connect('railwaysFB.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM gender;''')
res = cursor.fetchall()
for r in res:
    print(r)
    
from os.path import exists
if not exists('railwaysFB.db'):
    db_init()
conn = sqlite3.connect('railwaysFB.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM carriage_types;''')
res = cursor.fetchall()
for r in res:
    print(r) 
    
from os.path import exists
if not exists('railwaysFB.db'):
    db_init()
conn = sqlite3.connect('railwaysFB.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM  client_document_types;''')
res = cursor.fetchall()
for r in res:
    print(r)
    
from os.path import exists
if not exists('railwaysFB.db'):
    db_init()
conn = sqlite3.connect('railwaysFB.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM trains;''')
res = cursor.fetchall()
for r in res:
    print(r)

from os.path import exists
if not exists('railwaysFB.db'):
    db_init()
conn = sqlite3.connect('railwaysFB.db')
cursor = conn.cursor()
cursor.execute('''
SELECT * FROM geo_entities;''')
res = cursor.fetchall()
for r in res:
    print(r)

