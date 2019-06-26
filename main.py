
from flask import Flask, request, redirect
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():

    template = jinja_env.get_template('index.html')
    return template.render()





@app.route("/", methods=["POST"])

def validate_user_info():
    username = request.form["username"]
    password = request.form["password"]
    passwordconfirm = request.form["passwordconfirm"]
    email = request.form["email"]



    username_error = ''
    password_error = ''
    passwordconfirm_error = ''
    email_error = ''




    if username == '':
        username_error = "You must choose a username."

    elif " " in username:
        username_error = "Your username cannot contain spaces."

    elif len(username) < 3:
        username_error = "Your username is too short."

    elif len(username) > 20:
        username_error = "Your username is too long."

    
    if password == '':
        password_error = "You must choose a password."

    elif " " in password:
        password_error = "Your password cannot contain spaces."

    elif len(password) < 3:
        password_error = "Your password is too short."

    elif len(password) > 20:
        password_error = "Your password is too long."

    if passwordconfirm == '':
        passwordconfirm_error = "You must confirm your password."

    elif passwordconfirm != password:
        passwordconfirm_error = "You password entries did not match."

    if email == '':
        email_error = ''

    elif "@" not in email:
        email_error = "This address does not have an @ symbol."

    elif "." not in email:
        email_error = "This address does not have a . symbol."

    elif " " in email:
        email_error = "Email addresses cannot contain spaces."

    elif len(email) < 3:
        email_error = "This address is too short to be a valid email address."

    elif len(email) > 20:
        email_error = "This address is too long for our form."
    
    
    if not username_error and not password_error and not passwordconfirm_error and not email_error:
        return redirect("/welcome?username={0}".format(username))

    else:

        template = jinja_env.get_template('index.html')
        return template.render(username = username, email = email, username_error = username_error, password_error = password_error, passwordconfirm_error = passwordconfirm_error, email_error = email_error)


@app.route('/welcome')

def welcome():
    username = request.args.get("username")
    template = jinja_env.get_template('welcome.html')
    return template.render(name = username)


if __name__=='__main__':
    app.run()




