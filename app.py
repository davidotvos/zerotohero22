from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/cashier', methods=['POST'])
def cashier():
    data = request.get_json()
    
    first_name = data['firstName']
    last_name = data['lastName']

    return jsonify({'result' : 'Success!', 'firstName' : first_name, 'lastName' : last_name})


@app.route('/sale', methods=['POST'])
def sale():
    data = request.get_json()
    
    sold_items = data['soldItems']
    cashier_id = data['cashierId']
    price = data['price']

    return jsonify({'soldItems' : sold_items, "cashierId" : cashier_id, "price" : price})



if __name__ == '__main__':
    app.run(debug=True)
