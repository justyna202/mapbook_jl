def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość ma treść {user['usermessage'][-1]}')


def add_user(users_data: list) -> None:
    name = input('podaj imię: ')
    location = input('podaj lokalizację: ')
    posts = int(input('podaj liczbę postów:'))
    usermessage = ['']
    users_data.append({'username': name, 'location': location, 'posts': posts,
                       'usermessage': usermessage}, )


def remove_user(users_data: list) -> None:
    name = input('Podaj imię użytkownika do usunięcia: ')

    for user in users_data:
        if user['username'] == name:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    name = input('Podaj imię użytkownika do zmiany: ')

    for user in users_data:
        if user['username'] == name:
            user['username'] = input('Podaj nowe imię:')
            user['location'] = input('Podaj nową lokalizację:')
            user['posts'] = int(input("Podaj liczbę postów"))
