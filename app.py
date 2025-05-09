from flask import Flask, render_template, request, redirect, session
import jwt, datetime

app = Flask(__name__)
app.secret_key = 'supersecurekey'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email == 'admin@example.com' and password == 'admin123':
        token = jwt.encode({
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.secret_key, algorithm='HS256')
        session['token'] = token
        return redirect('/dashboard')
    return "Login Failed"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
