from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# adatbázis inicializálás
db = SQLAlchemy(app)

class Cashier(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)

    def repr_(self):
        return'<Name%r>' % self.id
    


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/cashier', methods=['POST', 'GET'])
def cashier():

    if request.method == 'POST':
            
        data = request.get_json()
        
        firstName = data['firstName']
        lastName = data['lastName']

        new_cashier = Cashier(id = '2', first_name = firstName, last_name = lastName)

        #return jsonify({'result' : 'Success!', 'firstName' : first_name, 'lastName' : last_name})
        
        #adatbázishoz adás
        try:
            db.session.add(new_cashier)
            db.session.commit()
            return redirect('/cashier')
        except:
            return 'Hiba az adatbázishoz adásnál!'

    else:
        cashiers = Cashier.query.order_by(Cashier.id)
        return render_template('cashier.html', cashiers=cashiers)



@app.route('/sale', methods=['POST'])
def sale():
    data = request.get_json()
    
    sold_items = data['soldItems']
    cashier_id = data['cashierId']
    price = data['price']

    return jsonify({'soldItems' : sold_items, "cashierId" : cashier_id, "price" : price})



if __name__ == '__main__':
    app.run(debug=True)
