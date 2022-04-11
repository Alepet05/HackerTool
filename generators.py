alphabet = '0123456789abcdefghijklmnopqrstuvwxyz' # алфавит с.с
base = len(alphabet) # основание алфавита

def generate_by_brute_force(num: int, length: int):
    """Генерация пароля брутфорсом

    Args:
        num (int): число, соответствующее очередному генерируемому паролю
        length (int): необходимая длина генерируемого пароля

    Returns:
        password(str): сгенерированный пароль
    """
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

    return password
