from app import app
from flask import request,flash,session,render_template,url_for,redirect
from app.module.forms.login_user import Login_user, Registry_user,login_required

@app.route('/login', methods = ['POST','GET'])
def login():
    form = Login_user(request.form)
    if request.method == 'POST' and form.validate():
        session['login_user'] = form.user.username
        return redirect(url_for('index'))
    else:
        return render_template('login.html',form = form)

@app.route('/registry', methods = ['POST','GET'])
#@login_required
def registry():
    form = Registry_user(request.form)
    if request.method == 'POST' and form.validate():
        session['login_user'] = form.user.username
        return redirect(url_for('index'))
    else:
        return render_template('registry.html',form = form)

@app.route('/logout')
@login_required
def logout():
    if 'login_user' in session:
        session.pop('login_user',None)
    return redirect(url_for('index'))

