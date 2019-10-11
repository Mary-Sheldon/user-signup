from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route('/')
def index():
    return render_template ('form.html')

def empty_val(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x)>3 and len(x)<21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >=1:
        return True
    else:
        return False

def email_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def email_period_more_than_one(x):
    if x.count('.') <= 1:
        return True
    else:
        return False





@app.route('/', methods=['POST'])
def display_signup():

    username=request.form['username']
    password=request.form['password']
    password_validate= request.form['verify_password']
    email= request.form['email']

    username_error = ''
    password_error= ''
    verify_error=''
    email_error=''

    empty_error = 'Please enter something'
    char_error = 'username must be between 3 and 20 characters'
    password_error_e = "please re-enter your password"
    space_error = 'You cannot uses spaces'
    password_validate_error = password_error_e

    if not empty_val(password):
        password_error = empty_error
        password = ''
        password_validate = ''
    elif not char_length(password):
        password_error = "Password " + char_error
        password = ''
        password_validate = ''
        password_validate_error = password_error_e
    else:
        if " " in password:
            password_error = "Password " + space_error
            password = ''
            password_validate = ''
            password_validate_error = password_error_e

#probabl gonna have A problem here
    if password_validate != password:
        password_validate_error = "Passwords must match"
        password = ''
        password_validate = ''
        password_error = 'Passwords must match'


    if not empty_val(username):
        username_error = empty_error
        password = ''
        password_validate = ''
        password_error = password_error_e
        password_validate_error = password_error_e
    elif not char_length(username):
        username_error = "Username " + char_error
        password = ''
        password_validate = ''
        password_error = password_error_e
        password_validate_error = password_error_e
    else:
        if " " in username:
            username_error = "Username " + space_error
            password = ''
            password_validate = ''
            password_error = password_error_e
            password_validate_error = password_error_e



    
        if not char_length(email):
            email_error = "Email " + char_error
            password = ''
            password_validate = ''
            password_error = password_error_e
            password_validate_error = password_error_e
        elif not email_at_symbol(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            password_validate = ''
            password_error = password_error_e
            password_validate_error = password_error_e
        elif not email_at_symbol_more_than_one(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            password_validate = ''
            password_error = password_error_e
            password_validate_error = password_error_e
        elif not email_period(email):
            email_error = "Email must contain ."
            password = ''
            password_validate = ''
            password_error = password_error_e
            password_validate_error = password_error_e
        elif not email_period_more_than_one(email):
            email_error = "Email must contain only one ."
            password = ''
            password_validate = ''
            password_error = password_error_e
            password_validate_error = password_error_e
        else:
            if " " in email:
                email_error = "Email " + space_error
                password = ''
                password_validate = ''
                password_error = password_error_e
                password_validate_error = password_error_e
   
   
    #if not username_error and not password_error and not password_validate_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    #else:
      #  return render_template('form.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)



@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()