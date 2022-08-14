import string
import uuid
import os.path

# generál egy egyedi id-t a cashiernek
def generate_id(cashiers):
    temp_id = uuid.uuid4()

    if check_if_id_in_database(cashiers, temp_id):
        temp_id = generate_id(cashiers)

    return str(temp_id)


# benne van-e az id az adatbázisban
def check_if_id_in_database(cashiers, id):
    for c in cashiers:
        if id == c[0]:
            return True
    
    return False


# menu és item lista beolvasás
def read_items_and_menu(itemlist:list, menulist:list):
    read_csv('items.csv', itemlist)
    read_csv('menu.csv', menulist)


# csv fájl olvasása soronként
def read_csv(filename, list:list):
    for line in open(filename):
        csv_row = line.split(';')
        list.append(csv_row)


# Ha nem létezik a fájl csinál egyet, ha létezik beolvassa
def create_or_read_cashier_database(cashiers):
    if os.path.exists('cashiers.csv'):
        read_csv('cashiers.csv', cashiers)

    else:
        f = open('cashiers.csv', 'w')


# Cashier hozzáadása
def add_cashier(cashiers, firstName, lastName):
    templi = []
    templi = [generate_id(cashiers), firstName, lastName]
    cashiers.append(templi)
    save_cashiers(cashiers)



# Elmenti a cashierek adatait
def save_cashiers(cashiers):
    with open('cashiers.csv', 'w') as f:
        for line in cashiers:

            f.write(';'.join(line))


