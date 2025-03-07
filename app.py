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
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username and password match
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('dashboard'))  # Redirect to dashboard if successful
    else:
        return "Login Failed! Incorrect username or password."

@app.route('/dashboard')
def dashboard():
    return render_template('schoolguardfinal.html')  # Render the dashboard HTML page

if __name__ == '__main__':
    app.run(debug=True)
