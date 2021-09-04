from flask import Flask,render_template



app = Flask(__name__)

@app.route('/')
@app.route('/home')
def web():
    return render_template('home.html')



@app.route('/create_user', methods = ['POST'])
def create_user():
    return

@app.route('/get_user', methods = ['GET'])
def create_user():
    return

@app.route('/delete_user', methods = ['DELETE'])
def create_user():
    return

@app.route('/put_user', methods = ['PUT'])
def create_user():
    return

if __name__ == ('__main__'):
    app.run(debug=True)
