from root.main import bp
from root.main.forms import AddNewAccountForm
from root.models import Account
from flask import render_template
from flask_login import current_user, login_required


@bp.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('dashboard.html', title='Dashboard')
    return render_template('landing.html')


@bp.route('/dashboard')
@login_required
def dashboard():
    form = AddNewAccountForm()
    if form.validate_on_submit():
        account = Account(account_name=form.account_name.data, email=form.email.data)
        if form.description.data:
            account.description = form.description.data
        if form.username.data:
            account.username = form.username.data
        if form.password_hint.data:
            account.password_hint = form.password_hint.data
        account.user_id = current_user.id
        db.session.add(account)
        db.session.commit()
        return '<p>Success</p>'
    return render_template('dashboard.html', title='Dashboard', form=form)