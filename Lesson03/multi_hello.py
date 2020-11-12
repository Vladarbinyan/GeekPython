users = ['Artur', 'Gleb', 'Boris']


def say_hello(*user_list, **user_settings):
    print(user_settings) # user_settings это словарь
    for user in user_list:
        print(user)


say_hello(*users, discount=100, quality='bad') # Дополнительные именованные параметры будут переданы в **user_settings
say_hello('Holly')