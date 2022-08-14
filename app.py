from flask import Flask, render_template, request, jsonify, redirect
import utils

app = Flask(__name__)

cashiers = []
items = []
menu = []

class Cashier:
    def __init__(self, firstname, lastname):
        self.id = utils.generate_id(cashiers)
        self.firstname = firstname
        self.lastname = lastname



@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/cashier', methods=['POST'])
def cashier():

    if request.method == 'POST':
            
        data = request.get_json()
        
        firstName = data['firstName']
        lastName = data['lastName']

        utils.add_cashier(cashiers, firstName, lastName)

        return jsonify({'result' : 'Success!'})



@app.route('/sale', methods=['POST'])
def sale():
    data = request.get_json()
    
    sold_items = data['soldItems']
    cashier_id = data['cashierId']
    price = data['price']

    return jsonify({'soldItems' : sold_items, "cashierId" : cashier_id, "price" : price})



if __name__ == '__main__':
    utils.read_items_and_menu(items, menu)
    utils.create_or_read_cashier_database(cashiers)
    
    app.run(debug=True)
