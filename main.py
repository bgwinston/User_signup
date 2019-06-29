from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/signup')
def show_signup_form():
    return render_template('signup.html', username='', username_error='', password='', password_error='', verify_password='', verify_password_error='', email='', email_error='')

@app.route('/signup', methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']   

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

#User types in nothing for username
    if int(len(username)) <=0:
        username_error = "Username invalid. Please try again"
        username = ''
    else:
        if int(len(username)) < 3 or int(len(username)) > 20:
            username_error = "Username invalid. Please try again."
            username = ''
 #password less than 3 characters   
    if int(len(password)) <= 0:
        password_error = 'Thats not a valid password'
        password = ''
    else:
        if int(len(password)) < 3 or int(len(password)) > 20:
            password_error = "Password invalid. Please try again."
            password = ''
#passwords don't match
    if int(len(verify_password)) <= 0:
        verify_password_error = "Passwords do not match"
        verify_password = ''
    else:
        if int(len(password)) != int(len(verify_password)):
            verify_password_error = "Passwords do not match"
            verify_password_error = ''
#User's email is missing or includes things that aren't apart of email. 
    if int(len(email)) > 0:
        if "@" not in email and "." not in email and " " not in email:
            email_error = 'This is not a valid email'
            email = ''
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = str(username)
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username, password=password, verify_password=verify_password, email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

app.run()
