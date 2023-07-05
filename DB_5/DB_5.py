import psycopg2
from pprint import pprint

# Перед началом работы необходимо создать базу данных и внести данные в (database='', user='', password='').

def create_table(cur):
    """Создание таблиц клиентских данных"""

    # Создание основной таблицы данных, где хранятся: имя, фамилия, email.
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    client_surname VARCHAR(100) NOT NULL,
    client_email VARCHAR(100) NOT NULL);
    """)

    # Создание дополнительной таблицы, связанной с основной, где хранятся номера клиентов.
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients_phones(
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(id) ON DELETE CASCADE,
    phonenumber VARCHAR(20));
    """)

def add_new_client(cur, client_name, client_surname, client_email):
    """Добавление нового клиента в таблицу clients"""
    cur.execute("""
    INSERT INTO clients(client_name, client_surname, client_email) VALUES (%s, %s, %s);
    """, (client_name, client_surname, client_email))
    conn.commit()
    print('Данные о клиенте добавлены')

def add_client_phonenumber(cur, client_id, phonenumber):
    """Добавление нового номера телефона в таблицу clients_phones"""
    cur.execute("""
    INSERT INTO clients_phones(client_id, phonenumber) VALUES (%s, %s);
    """, (client_id, phonenumber))
    conn.commit()
    print('Номер телефона добавлен')

def change_client_data(cur):
    """Изменение информации о клиенте"""
    print("Для изменения данных клиента, укажите команду которую необходимо выполнить. \n "
          "1 - изменить имя; 2 - изменить фамилию; 3 - изменить email; 4 - изменить номер телефона; 0 - выход из цикла")
    
    while True:
        command = int(input())
        if command == 1:
            id_changing_name = input("Введите id клиента имя которого хотите изменить: ")
            name_changing = input("Введите имя для замены: ")
            cur.execute("""
            UPDATE clients SET client_name=%s WHERE id=%s;
            """, (name_changing, id_changing_name))
            break
        elif command == 2:
            id_changing_surname = input("Введите id клиента фамилию которого хотите изменить: ")
            surname_changing = input("Введите фамилию для замены: ")
            cur.execute("""
            UPDATE clients SET client_surname=%s WHERE id=%s;
            """, (surname_changing, id_changing_surname))
            break
        elif command == 3:
            id_changing_email = input("Введите id клиента email которого хотите изменить: ")
            email_changing = input("Введите email для замены: ")
            cur.execute("""
            UPDATE clients SET client_email=%s WHERE id=%s;
            """, (email_changing, id_changing_email))
            break
        elif command == 4:
            number_changing_old = input("Введите номер телефона который хотите изменить: ")
            number_changing_new = input("Введите новый номер телефона: ")
            cur.execute("""
            UPDATE clients_phones SET phonenumber=%s WHERE phonenumber=%s;
            """, (number_changing_new, number_changing_old))
            break
        elif command == 0:
            break
        else:
            print("Команда не распознана. Повторите ввод.")

    conn.commit()

def delete_client_phonenumber(cur):
    """Удаление номера телефона из таблицы clients_phones"""
    id_client = input("Введите id клиента для которого необходимо удалить номер телефона: ")
    print("Выберите действие по удалению номера телефона. \n "
          "1 - удаление всех номеров по клиенту; 2 - удаление конкретного номера; 0 - выход из цикла.")
    while True:
        command = int(input())
        if command == 1:
            cur.execute("""
            DELETE FROM clients_phones WHERE client_id=%s;
            """, (id_client))
            break
        elif command == 2:
            phonenumber_new = input("Введите номер телефона: ")
            cur.execute("""
            DELETE FROM clients_phones WHERE client_id=%s AND phonenumber=%s;
            """, (id_client, phonenumber_new))
            break
        elif command == 0:
            break
        else:
            print("Команда не распознана. Повторите ввод.")

    conn.commit()

def delete_client(cur):
    """Удаление всей имеющейся информации о клиенте"""
    id_client = input("Введите id клиента которого необходимо удалить: ")
    cur.execute("""
    DELETE FROM clients_phones WHERE client_id=%s;
    """, (id_client,))
    cur.execute("""
    DELETE FROM clients WHERE id=%s;
    """, (id_client,))

    conn.commit()

def find_client(cur):
    """Поиск полной информации о клиенте по имеющимся данным"""
    print("Выберите метод поиска. \n "
          "1 - по имени; 2 - по фамилии; 3 - по email; 4 - по номеру телефона; 0 - выход из цикла.")
    while True:
        command = int(input("Введите код выбранного метода поиска: "))
        if command == 1:
            name_finding = input("Введите имя для поиска информации о клиенте: ")
            cur.execute("""
            SELECT clients.id, client_name, client_surname, client_email, phonenumber
            FROM clients
            LEFT JOIN clients_phones AS cp ON cp.client_id = clients.id
            WHERE client_name=%s
            """, (name_finding,))
            print(cur.fetchall())
            break
        elif command == 2:
            surname_finding = input("Введите фамилию для поиска информации о клиенте: ")
            cur.execute("""
            SELECT clients.id, client_name, client_surname, client_email, phonenumber
            FROM clients
            LEFT JOIN clients_phones AS cp ON cp.client_id = clients.id
            WHERE client_surname=%s
            """, (surname_finding,))
            print(cur.fetchall())
            break
        elif command == 3:
            email_finding = input("Введите email для поиска информации о клиенте: ")
            cur.execute("""
            SELECT clients.id, client_name, client_surname, client_email, phonenumber
            FROM clients
            LEFT JOIN clients_phones AS cp ON cp.client_id = clients.id
            WHERE client_email=%s
            """, (email_finding,))
            print(cur.fetchall())
            break
        elif command == 4:
            number_finding = input("Введите номер для поиска информации о клиенте: ")
            cur.execute("""
            SELECT clients.id, client_name, client_surname, client_email, phonenumber
            FROM clients
            LEFT JOIN clients_phones AS cp ON cp.client_id = clients.id
            WHERE cp.phonenumber=%s
            """, (number_finding,))
            print(cur.fetchall())
            break
        elif command == 0:
            break
        else:
            print("Команда не распознана. Повторите ввод.")

def table_info(cur):
    """Отображает данные по всем клиентам"""
    cur.execute("""
    SELECT * FROM clients;
    """)
    pprint(cur.fetchall())
    cur.execute("""
    SELECT * FROM clients_phones;
    """)
    pprint(cur.fetchall())
    

with psycopg2.connect(database='clients', user='postgres', password='') as conn:
    with conn.cursor() as cur:
        create_table(cur)
        add_new_client(cur, 'John', 'Johnson', 'j@nsg.com')
        add_new_client(cur, 'Tod', 'Williams', 't@dg.com')
        add_new_client(cur, 'Jack', 'Pinky', 'j@ckg.com')
        add_new_client(cur, 'Brian', 'Griffin', 'b@rg.com')
        add_new_client(cur, 'Edward', 'Grey', 'e@dg.com')
        add_client_phonenumber(cur, 1, '00000')
        add_client_phonenumber(cur, 1, '11111')
        add_client_phonenumber(cur, 2, '22222')
        add_client_phonenumber(cur, 3, '33333')
        add_client_phonenumber(cur, 4, '44444')
        add_client_phonenumber(cur, 5, '55555')
        change_client_data(cur)
        delete_client_phonenumber(cur)
        delete_client(cur)
        find_client(cur)
        table_info(cur)

conn.close()
