from flask import Flask  
import models
from flask import make_response, request, json, jsonify 
from passlib.hash import sha256_crypt <

app = Flask(__name__)  


app.config.update(dict(
    SECRET_KEY="THIS IS AN INSECURE SECRET!! DO NOT USE IN PROD!!",
    SQLALCHEMY_DATABASE_URI='sqlite:///user.db',
))

models.init.app(app)
models.create_table(app)

@app.route('/users/hello')
def hello():
    return 'Hello, welcome to the ESBay User API \n'

@app.route('/api/user/create', methods=['POST'])
def post_register():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = sha256_crypt.hash((str(request.form['password'])))

    user = model.User()
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.password = password
    user.auth = True
    user.active = True

    models.db.session.add(user)
    models.db.sessions.commit()

    response = jsonify({'message':'User added', 'result': user.to_json()})

@app.route('/api/users', methods=['GET'])
def get_users():
    data=[]
    for row in models.User.query.all():
        data.append(row.to_json())
    
    response = jsonify(data)

    return response

if __name__ == '__main__':
    app.run(debug=True, host="0,0,0,0", port=5000)

