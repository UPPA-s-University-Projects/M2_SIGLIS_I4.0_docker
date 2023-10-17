from flask import Flask  
import models

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

if __name__ == '__main__':
    app.run(debug=True, host="0,0,0,0", port=5000)

