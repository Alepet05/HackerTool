import json
from flask import Flask, request, Response


app = Flask(__name__)

# инициализируем статистику сервера
stats = {
    'attempts': 0,
    'success': 0,
}

# на главной странице просто выводим статистику
@app.route('/')
def hello():
    return f'Hello, user! stats={stats}'

# страница обращения к серверу
@app.route('/auth', methods=['POST'])
def auth():
    stats['attempts'] += 1 # увеличиваем кол-во попыток с очередным запросом

    # получаем данные, отправленные post-запросом
    data = request.json
    login = data['login']
    password = data['password']

    # подгружаем словарь "зарегистрированных" пользователей
    with open('users.json') as users_file:
        users = json.load(users_file)

    # если пароль к пользователю подходит, увеличваем кол-во успешных попыток и возвращаем статус 200
    # иначе 401
    if login in users and users[login] == password:
        status_code = 200
        stats['success'] += 1
    else:
        status_code = 401

    return Response(status=status_code)

if __name__ == '__main__':
    app.run()