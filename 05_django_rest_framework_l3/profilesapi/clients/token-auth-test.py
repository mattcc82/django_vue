import requests

def client():
    token_h = 'Token 75ac0a579a6dc1d62e5a0f6cb6677d72b87aab9d'
    # credentials = {}
    # credentials['username'] = 'admin'
    # credentials['password'] = 'gongos1'

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    #     data=credentials
    # )

    headers = {}
    headers['Authorization'] = token_h

    response = requests.get('http://127.0.0.1:8000/api/profiles/',
        headers=headers
    )

    print ('status code: ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()
