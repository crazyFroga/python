# Напишите программу, которая сначала запрашивает логин пользователя,
# проверяет, существует он или нет,
# а потом с помощью вложенного условия проверяет пароль этого пользователя.

login_list = [
    'root',
    'username1'
]

password_list = {
    'root': '1q2w3e4r',
    'username1': 'qwerty123'
}

username = str(input('Введите логин:\n'))

if username in login_list[0]:
    print(password_list['root'])

elif username == login_list[1]:
    print(password_list['username1'])

else:
    print("Такого логина не существует")

