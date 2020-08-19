from root import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), unique=True, nullable=False)
    accounts = db.relationship('Account', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User '{self.username}'>"


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(40))
    email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(20))
    password_hint = db.Column(db.Text(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Account '{self.account_name}', '{self.email}'>"