from flask import render_template, redirect, url_for, flash, session, request
from app import app

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Your login logic
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')
