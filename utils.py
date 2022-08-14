import uuid

# generál egy egyedi id-t a cashiernek
def generate_id(cashiers):
    temp_id = uuid.uuid4()

    if check_if_id_in_database(cashiers, temp_id):
        temp_id = generate_id(cashiers)

    return temp_id

# benne van-e az id az adatbázisban
def check_if_id_in_database(cashiers, id):
    for c in cashiers():
        if id == c.id:
            return True
    
    return False

# menu és item lista beolvasás
def read_items_and_menu(itemlist:list, menulist:list):
    for line in open('items.csv'):
        csv_row = line.split(';')
        itemlist.append(csv_row)

    for line in open('menu.csv'):
            csv_row = line.split(';')
            menulist.append(csv_row)




def save_cashier(cashiers):

    pass