from flask import Flask  
import models
from flask import make_response, request, json, jsonify 

app = Flask(__name__)  


app.config.update(dict(
    SECRET_KEY="THIS IS AN INSECURE SECRET!! DO NOT USE IN PROD!!",
    SQLALCHEMY_DATABASE_URI='sqlite:///user.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
))

models.init.app(app)
models.create_table(app)

@app.route('/products/hello')
def hello():
    return 'Hello, welcome to the ESBay Product API \n'

@app.route('/api/product/create', method=['POST'])
def post_create():
    name = request.form['name']
    seller = request.form['seller']
    price = request.form['price']

    item = models.Product()
    item.name = name
    item.seller = seller
    item.price = price

    models.db.session.add(item)
    models.db.session.commit()

    response = jsonify({'message': 'Product created', 'product': item.to_json()})

@app.route('/api/products', method=['GET'])
def products():
    data = []
    for row in models.Product.query.all():
        data.append(row.to_json())

    response = jsonify({
        'results':data
    })

    return response

if __name__ == '__main__':
    app.run(debug=True, host="0,0,0,0", port=5000)

