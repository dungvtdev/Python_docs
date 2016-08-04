from functools import wraps
from flask import request, redirect, url_for,session
from flask_wtf import Form
from wtforms import TextField,PasswordField,RadioField
from wtforms import validators
from app.module.database.db_user import User_Service
from  app.module.user import User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('login_user'):
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


class Login_user(Form):
    username = TextField('Username', [validators.DataRequired('Username cannot empty')],render_kw={"placeholder": "username"})
    password = PasswordField('Password', [validators.DataRequired('Password cannot empty')], render_kw={"placeholder": "password"})

    def __init__(self,*args,**kwargs):
        Form.__init__(self,*args,**kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        print(rv)
        if not rv:
            return False
        user_service = User_Service()
        user = user_service.check_user(self.username.data)
        if user is None :
            self.username.errors.append('Unknown username')
            return False
        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False
        self.user = user
        return True

class Registry_user(Form):
    firstname = TextField('First Name',[validators.DataRequired()],render_kw={"placeholder": "First name"})
    lastname = TextField('Last Name', [validators.DataRequired()],render_kw={"placeholder": "Last name"})
    username = TextField('User name',[validators.length(min=5,max=30),validators.DataRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField('Password',[validators.length(min=5,max=30),validators.DataRequired()],render_kw={"placeholder": "Password"})
    repassword = PasswordField('Repassword',[validators.DataRequired()],render_kw={"placeholder": "Repassword"})
    email = TextField("Email", [validators.DataRequired("Please enter your email address."),
                                validators.Email("email incorrect")],render_kw={"placeholder": "Your email"})
    phone = TextField('Phone number',render_kw={"placeholder": "Phone number"})
    role = RadioField(
        'Role ?',
        [validators.DataRequired()],
        choices=[('1', 'User'), ('0', 'Admin')], default='choice1'
    )

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user_service = User_Service()
        user = user_service.check_user(self.username.data)
        if user:
            print("error user")
            self.username.errors.append('username already exists!!!')
            return False
        self.user = User(self.firstname.data,self.lastname.data,self.username.data
                         ,self.email.data,self.password.data,self.phone.data,self.role.data)

        user_service.add_user(self.user)
        return True




