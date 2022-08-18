import uuid
import os.path
import json


# generál egy egyedi id-t a cashiernek
def generate_id(database):
    temp_id = uuid.uuid4()

    if check_if_id_is_taken(database, temp_id):
        temp_id = generate_id(database)
    
    return str(temp_id)


# benne van-e az id az adatbázisban
def check_if_id_is_taken(database, id):
    for ids in database['cashiers']:
        if id == ids['id']:
            return True
    
    return False


# itemek beolvasása
def import_items(database, filename):
    try:
        for line in open(filename):
            csv_row = line.split(';')
            temp_dict = {
                'name' : csv_row[0].lower(),
                'price' : csv_row[1].strip()
            }
            database['items'].append(temp_dict)

    except:
        print("items.csv nem importálható")


# menu beolvasása
def import_menu(database, filename):
    try:
        for line in open(filename):
            csv_row = line.split(';')
            
            temp_dict = {
                'price' : csv_row[0],
                'name' : csv_row[1].lower(),
                'items' : [n.strip().lower() for n in csv_row[2:]]
            }
            
            database['menu'].append(temp_dict)
    
    except:
        print("menu.csv nem importálható")


# Ha nem létezik az adatbázis csinál egyet, ha létezik beolvassa
def read_database(database):
    filename = 'database.csv'
    with open(filename, 'r') as f:
        data = json.load(f)
        database['cashiers'] = data['cashiers']
        database['sales'] = data['sales']
        database['items'] = data['items']
        database['menu'] = data['menu']


def create_database(database):
    if not os.path.isfile('database.csv'):
        with open('database.csv', 'w') as f:
            json.dump(database, f)


# Cashier hozzáadása
def add_cashier(database, firstName, lastName):
    temp_dict = {
        "id" : generate_id(database),
        "firstName" : firstName,
        "lastName" : lastName
    }

    database['cashiers'].append(temp_dict)
    save_database(database)
    

def add_sale(database, soldItems, cashierId, price):
    real_price = 0
    sale_id = generate_id(database)
    menu_size = 0


    big_bucket_menu = database['menu'][0]['items']
    small_bucket_menu = database['menu'][1]['items']
    chicken_burger_menu = database['menu'][2]['items']
    double_burger_menu = database['menu'][3]['items']

    if common_elements(big_bucket_menu, soldItems):
        real_price += float(database['menu'][0]['price'])
        soldItems = [item for item in soldItems if item not in big_bucket_menu]
        soldItems.append('Big Bucket Menu')
        menu_size += 1
    elif common_elements(small_bucket_menu, soldItems):
        real_price += float(database['menu'][1]['price'])
        soldItems = [item for item in soldItems if item not in small_bucket_menu]
        soldItems.append('Small Bucket Menu')
        menu_size += 1
    elif common_elements(chicken_burger_menu, soldItems):
        real_price += float(database['menu'][2]['price'])
        soldItems = [item for item in soldItems if item not in chicken_burger_menu]
        soldItems.append('Chicken Burger Menu')
        menu_size += 1
    elif common_elements(double_burger_menu, soldItems):
        real_price += float(database['menu'][3]['price'])
        soldItems = [item for item in soldItems if item not in double_burger_menu]
        soldItems.append('Double Burger Menu')
        menu_size += 1

    if len(soldItems) > menu_size:
        for item in soldItems:
            for food in database['items']:
                if food.get('name') == item:
                    real_price += float(food.get('price'))

    if real_price < float(price):
        status = "REFUND"
    else:
        status = "PROCESSED"


    temp_dict = {
        "saleId" : sale_id,
        "soldItems" : soldItems,
        "cashierId" : cashierId,
        "price" : price,
        "status" : status,
        "difference" : float(price - real_price)
    }

    database['sales'].append(temp_dict)
    save_database(database)



def common_elements(menu, soldItems):

    common = list(set(menu).intersection(soldItems))

    if len(common) == len(menu):
        return True
    else:
        return False
    

    



# Elmenti az adatbázist
def save_database(database):
    with open('database.csv', 'w') as f:
        json.dump(database, f)

