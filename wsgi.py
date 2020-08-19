from root import app, db
from root.models import User, Account


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Account': Account}


if __name__ == '__main__':
    app.run()