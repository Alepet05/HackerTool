import requests


def request_local_server(login: str, password: str):
    """Посылает данные аутентификации на локальный сервер, написанный в Server/server.py

    Args:
        login (str): подобранный логин пользователя
        password (str): подобранный пароль пользователя

    Returns:
        bool: ответ сервера: True - если пароль подошел, иначе - False
    """
    # посылаем post-запрос на локальный сервер
    response = requests.post('http://127.0.0.1:5000/auth',
                            # передаем именно json, как это требует сервер, а не data
                            json={'login': login, 'password': password})

    return response.status_code == 200 