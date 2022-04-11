def iterate_by_passwords_then_by_logins(login_generator: function, password_generator: function, query: function):
    """Генерирует пароли и логины. Для каждого сгенерированного пароля генерирует логины и итерируется по ним

    Args:
        login_generator (function): функция генерации логинов
        password_generator (function): функция генерации паролей
        query (function): функция запросов на сервер
    """
    password_state = None # начальное состояние для генерации паролей
    while True:
        password, password_state = password_generator(password_state) # генерация очередного пароля
 
        login_state = None # начальное состояние для генерации логинов
        while True:
            login, login_state = login_generator(login_state) # генерация очередного логина
            if query(login, password): # делаем запрос на сервер и проверяем валидность логина с паролем. Если True - уведомляем об успехе
                print('Success', login, password)
            if login_state is None: # если дошли до конца списка логинов 
                break

        if password_state is None: # если закончились пароли. Для брутфорса это бесполезно, т.к. слишком большое кол-во генераций
            break


def iterate_by_logins_then_by_limited_passwords(login_generator: function, password_generator: function, query: function):
    """Генерирует пароли и логины. Для каждого сгенерированного логина генерирует пароли и итерируется по ним

    Args:
        login_generator (function): функция генерации логинов
        password_generator (function): функция генерации паролей
        query (function): функция запросов на сервер
    """
    
    limit = 100000 # лимит паролей
    login_state = None # начальное состояние для генерации логинов
    
    while True:
        login, login_state = login_generator(login_state) # генерация очередного логина
        password, password_state = password_generator(None) # инициализируем первый пароль
        for _ in range(limit): 
            if query(login, password): # делаем запрос на сервер и проверяем валидность логина с паролем. Если True - уведомляем об успехе
                print('Success', login, password)
                break
            password, password_state = password_generator(password_state) # генерация очередного пароля
            if password_state is None: # если закончились пароли. Для брутфорса это бесполезно, т.к. слишком большое кол-во генераций
                break

        if login_state is None: # если дошли до конца списка логинов 
            break