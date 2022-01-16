from flask import render_template, make_response, request

from models import Users


def read_user():
    message = ''
    error = None
    if request.method == 'POST':
        user = request.form.get('username')  # запрос к данным формы
        if user == '':
            error = "Ім'я користувача не може бути порожнім"
        else:
            user1 = Users.get_or_none(Users.username == user)   # запрос к базе данных
            if user1 is None:
                Users.create(username = user)
                message = 'Привіт, ' + user
            else:
                message = 'Вже бачилися, ' + user

    return render_template('login.html', message=message, error=error)    


def get_all_users():
    users = Users.select()
    return render_template("users.html", users=users)
