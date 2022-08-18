from flask import Flask, render_template, request, jsonify, redirect
import utils

app = Flask(__name__)

_database = {
    "cashiers" : [
        
    ],

    "sales" : [

    ],

    "menu" : [
        
    ],

    "items" : [

    ]
}

cashiers = []
items = []
menu = []
sales = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/cashier', methods=['POST','GET'])
def cashier():

    if request.method == 'POST':
            
        data = request.get_json()
        
        firstName = data['firstName']
        lastName = data['lastName']

        utils.add_cashier(_database, firstName, lastName)

        return jsonify({'result' : 'Success!'})

    else:
        return cashiers



@app.route('/sale', methods=['POST'])
def sale():
    
    data = request.get_json()
    
    sold_items = data['soldItems']
    cashier_id = data['cashierId']
    price = data['price']

    utils.add_sale(_database, sold_items, cashier_id, price)

    return jsonify({'result' : 'sucess'})



@app.route('/sale/<id>', methods=['GET', 'PUT'])
def sale_with_id(id):
    if request.method == 'GET':

        return utils.get_sale(_database['sales'], id)

    else:
        #TODO
        pass


@app.route('/cashier/<id>', methods=['GET'])
def cashier_with_id(id):
    return utils.get_sales_with_cashier_id(_database['sales'], id)



if __name__ == '__main__':
    utils.create_database(_database)
    utils.read_database(_database)
    utils.import_items(_database, 'items.csv')
    utils.import_menu(_database, 'menu.csv')
    
    app.run(debug=True)
