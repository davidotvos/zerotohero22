import string
import uuid
import os.path

# generál egy egyedi id-t a cashiernek
def generate_id(cashiers, sales):
    temp_id = uuid.uuid4()

    if check_if_id_in_database(cashiers, sales, temp_id):
        temp_id = generate_id(cashiers,sales)
    
    return str(temp_id)


# benne van-e az id az adatbázisban
def check_if_id_in_database(database1, database2, id):
    for d in database1:
        if id == d[0]:
            return True
    
    for d in database2:
        if id == d[0]:
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


# Ha nem létezik a cashier adatbázis csinál egyet, ha létezik beolvassa
def create_or_read_cashier_database(cashiers):
    if os.path.exists('cashiers.csv'):
        read_csv('cashiers.csv', cashiers)

    else:
        f = open('cashiers.csv', 'w')


# Ha nem létezik a sales adatbázis csinál egyet, ha létezik beolvassa
def create_or_read_sales_database(sales):
    if os.path.exists('salescsv'):
        read_csv('cashiers.csv', sales)

    else:
        f = open('sales.csv', 'w')


# Cashier hozzáadása
def add_cashier(cashiers, sales, firstName, lastName):
    templi = [generate_id(cashiers, sales), firstName, lastName]
    cashiers.append(templi)
    save_cashiers(cashiers)


# Sale hozzáadása
def add_sale(cashiers, sales, solditems, cashierid, price):
    templi = [generate_id(cashiers, sales), str(solditems), cashierid, str(price)]
    sales.append(templi)
    save_sales(sales)


# Elmenti a cashierek adatait
def save_cashiers(cashiers):
    with open('cashiers.csv', 'w') as f:
        for line in cashiers:
            f.write(';'.join(line) + '\n')


# Elmenti a sales adatait
def save_sales(sales):
    with open('sales.csv', 'w') as f:
        for line in sales:
            f.write(';'.join(line))