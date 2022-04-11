from ctypes import Union


simple_logins = ['admin', 'jack', 'cat'] # список логинов для нашего локального сервера
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz' # алфавит с.с
base = len(alphabet) # основание алфавита
# считываем список самых популярных паролей из файла
with open('10-million-password-list-top-1000000.txt') as f:
    popular_passwords = f.read().split('\n')

def generate_popular_password(state: Union[int, None]):
    """Генерация популярных паролей

    Args:
        state (Union[int, None]): состояние для генерации очередного пароля

    Returns:
        tuple: генерированный пароль и след. состояние для последующей генерации пароля
    """
    if state is None:  # ожидается, что первый state = None
        state = 0

    if state == len(popular_passwords) - 1: # если дошли до конца списка popular_passwords
        next_state = None
    else:
        next_state = state + 1

    return popular_passwords[state], next_state

def generate_simple_login(state: Union[int, None]):
    """Генерация очередного логина из списка simple_logins

    Args:
        state (Union[int, None]): состояние для генерации очередного логина

    Returns:
        tuple: сгенерированный логин и след. состояние для последующей генерации логина
    """
    if state is None: # ожидается, что первый state = None
        state = 0

    # генерация следующего состояния
    # next_state передается при следующем вызове как state и нужен для генерации следующего логина
    if state == len(simple_logins) - 1: # если дошли до конца списка simple_logins
        next_state = None
    else:
        next_state = state + 1

    # next_state нужен для того, чтобы потом передать его в качестве параметра state 
    # для генерации следующего лоигна
    return simple_logins[state], next_state

def generate_by_brute_force(state: Union[list, None]):
    """Генерация очередного пароля брутфорсом

    Args:
        state (Union[list, None]): состояние для генерации очередного пароля брутфорсом

    Returns:
        tuple: сгенерированный брутфорсом пароль и след. состояние для последующей генерации пароля
    """
    if state is None: # ожидается, что первый state = None
        state = [0, 0] # в качестве состояния указываем число, соответствующее очередному генерируемому паролю (num) и длину очередного генерируемого пароля (length)
    
    num, length = state # распаковываем данные из состояния

    password = '' # инициализируем переменную пароля
    temp = num # заводим под число временную переменную, чтобы проделывать с ней операции, не затерев само число
    # обычный алгоритм перевода из 10 сс в n сс
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password

    # если пароль меньше нужной длины, к нему добавляются 0. 
    # Например, если мы итерируемся по 3-х значным паролям, а пароль = 1, то 001
    password = alphabet[0] * (length - len(password)) + password

    # проверяем, последний ли пароль заданной длины.
    # Например, если мы итерируеся по 3-х значным паролям, 
    # и очередной пароль = zzz, то счетчик обнуляется, а длина увеличивается на 1 
    if password == alphabet[-1] * length:
        length += 1
        num = 0
    else:
        num += 1

    next_state = [num, length] # формируем следующее состояние для последющей генерации пароля

    # возвращаем сам сгенерированный пароль и след. состояние
    return password, next_state
