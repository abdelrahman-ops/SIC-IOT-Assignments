from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'asdfghjkl'  # Replace with a secure secret key
DATABASE = './users.db'

# Function to create a connection to the database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Function to initialize the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Initialize the database
init_db()

# Route for the home page
@app.route('/')
def home():
    if 'user_id' in session:
        return f"Welcome, user {session['user_id']}!"
    return "Welcome to your Flask app!"

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = get_db()
        cursor = conn.cursor()

        # Check if the username or email is already in use
        cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Username or email already in use. Please choose another.', 'danger')
        else:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
            conn.commit()
            flash('Registration successful. Please login.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user['id']
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

# Route for user logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
