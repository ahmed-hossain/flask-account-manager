from flask import flash, redirect, render_template, url_for
from root.auth import bp
from root.auth.forms import LoginForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have successfully logged in.', 'success')
        return redirect('/')
    return render_template('auth/login.html', title='Login', form=form)


@bp.route('/register')
def register():
    pass