from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return redirect('/dashboard')
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', name=username)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
