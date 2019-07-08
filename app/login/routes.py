from app.login import blueprint
from flask import render_template, redirect, request, url_for
from app.login.models import User

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import login_manager

import requests


@blueprint.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']

        # api-endpoint 
        URL = "http://localhost:3000/api/login"
        data = {'username': username,
                'pass': password}
        content = requests.post(URL, data)
        user = content.json()
        
        if user['success'] == 'true':
            print ('masuk ke login?')
            loginuser = user['user']
            login_user(loginuser)
            return redirect(url_for('home_blueprint.home'))
        else:
            message = user['message']
            return render_template('login.html', message=message)

    if not current_user.is_authenticated:
            print ("belum ada yang login")
            return render_template('login.html')


    return redirect(url_for('home_blueprint.home'))


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    print (current_user.is_authenticated)
    return redirect(url_for('login_blueprint.login'))
    