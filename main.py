

users: list = [
    {'username':'oliwia', 'location':'łódż', 'posts':1,'usermessage':['zyczenia1', 'kocham Legie', 'sprzedam Opla', 'kiwi']},
    {'username':'paweł', 'location':'ostróda', 'posts':2,'usermessage':['zyczenia2', 'kocham Legie1', 'sprzedam Opla1']},
    {'username':'eliza', 'location':'radom', 'posts':3,'usermessage':['zyczenia3', 'kocham Legie2']},
    {'username':'filip', 'location':'deblin', 'posts':4,'usermessage':['zyczenia4', 'kocham Legie3', 'sprzedam Opla3', 'kiwi']},
]

for user in users[1:]:
    print(f'twój znajomy {user ['username']} z miejscowości {user ['location']} opublikował {user ['posts']} wiadomości. Ostatnia wiadomość ma treść {user ['usermessage'][-1]}')

#    twój znajomy filip z mejscowosci deblin opublikował 1 posto treści: zyczenia
