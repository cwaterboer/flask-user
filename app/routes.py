from flask import render_template, redirect, url_for, flash
from app import app

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Add login logic here
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Add logic to check if user is authenticated
    return render_template('dashboard.html')
