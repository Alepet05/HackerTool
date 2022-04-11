import logic
import query
import generators

# склеиваем все составные части
logic.iterate_by_logins_then_by_limited_passwords( # можно выбрать любую логику перебора логинов с паролями
    generators.generate_simple_login, # можно выбрать любой генератор логинов
    generators.generate_popular_password, # можно выбрать любой генератор паролей
    query.request_local_server # можно выбрать любую функцию запроса
)
