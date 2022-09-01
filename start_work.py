import requests


def get_info(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)
    except requests.exceptions.ConnectionError:
        print('Problem with connection')


def main():
    ip = input('Enter IP: ')
    get_info(ip=ip)


if __name__ == '__main__':
    main()
