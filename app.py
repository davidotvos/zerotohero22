from flask import Flask, render_template, request, jsonify, redirect
import utils

app = Flask(__name__)

cashiers = []
items = []
menu = []
sales = []

class Cashier:
    def __init__(self, firstname, lastname):
        self.id = utils.generate_id(cashiers)
        self.firstname = firstname
        self.lastname = lastname



@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/cashier', methods=['POST','GET'])
def cashier():

    if request.method == 'POST':
            
        data = request.get_json()
        
        firstName = data['firstName']
        lastName = data['lastName']

        utils.add_cashier(cashiers, sales, firstName, lastName)

        return jsonify({'result' : 'Success!'})

    else:
        return cashiers



@app.route('/sale', methods=['POST'])
def sale():
    if request.method == 'POST':

        data = request.get_json()
        
        sold_items = data['soldItems']
        cashier_id = data['cashierId']
        price = data['price']

        utils.add_sale(cashiers, sales, sold_items, cashier_id, price)

        return jsonify({'result' : 'sucess'})

    else:
        return sales


if __name__ == '__main__':
    utils.read_items_and_menu(items, menu)
    utils.create_or_read_cashier_database(cashiers)
    utils.create_or_read_sales_database(sales)
    
    app.run(debug=True)
