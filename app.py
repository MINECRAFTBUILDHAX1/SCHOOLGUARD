from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded login details for simplicity
USERNAME = "schooladmin"
PASSWORD = "password123"

@app.route('/')
def home():
    return render_template('loginpage.html')  # Your login form HTML

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f"Username: {username}, Password: {password}")  # Debugging
    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        return redirect(url_for('dashboard'))
    else:
        print("Login failed!")
        return "Login Failed! Incorrect username or password."


@app.route('/dashboard')
def dashboard():
    return render_template('schoolguardfinal.html')  # Render the dashboard HTML page

if __name__ == '__main__':
    app.run(debug=True)
