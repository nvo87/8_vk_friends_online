import vk
import getpass

APP_ID = 6631591


def get_user_login():
    return input('Type your login: ')


def get_user_password():
    return getpass.getpass(prompt='Type your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, lang='ru')

    friends_id_list = api.friends.getOnline(v='5.83')
    return api.users.get(
        user_ids=friends_id_list,
        v='5.83'
    )


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()

    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        exit('Incorrect login or password.')
        
    output_friends_to_console(friends_online)