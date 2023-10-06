from flask import Flask
app = Flask(__name__)

@app.route('/')
def redirect():
    return render_template('index.html') 

@app.route('/<param>')
def redirect():
    return redirect(url_for('hello',name=str(param))) 

@app.route('/user/hello')
def hello():
    return 'Hello, welcome to the ESbay User API\n'

@app.route('/hello/<name>') 
def hello_world(name):     
    return 'Hello World ' +str(name) 

@app.route('/user/bye')
def bye():
    return 'Goodbye, welcome to the ESbay User API\n'

@app.route('/success/<name>') 
def success(name):     
    return 'welcome %s' % name     

@app.route('/login', methods=['POST', 'GET']) 
def login():     
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user)) 
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
