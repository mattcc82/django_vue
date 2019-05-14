import requests


def client():
    # credentials = {}
    # credentials['username'] = 'testUser'
    # credentials['password1'] = 'asdasdasdasd'
    # credentials['password2'] = 'asdasdasdasd'
    # credentials['email'] = 'test@gongos.com'

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',
    #     data=credentials
    # )

    token_h = 'Token 76b887cb6b449cccd89abd3b464564deed152bf0'
    headers = {}
    headers['Authorization'] = token_h

    response = requests.get('http://127.0.0.1:8000/api/profiles/',
                            headers=headers
                            )

    print('status code: ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
