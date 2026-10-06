import requests

адрес = "https://api.github.com/users/savelii-takogo-polzovatelya-tochno-net-99999"

try:
    ответ = requests.get(адрес, timeout=5)
    ответ.raise_for_status()
    данные = ответ.json()
    print("Логин:", данные["login"])
    print("Публичных репозиториев:", данные["public_repos"])
    print("Подписчиков:", данные["followers"])
except requests.exceptions.Timeout:
    print("Проблема: сервер не ответил за отведённое время (таймаут)")
except requests.exceptions.ConnectionError:
    print("Проблема: не удалось подключиться (нет соединения или неверный адрес)")
except requests.exceptions.HTTPError as ошибка:
    print("Проблема: сервер ответил с ошибочным кодом —", ошибка)
except requests.exceptions.RequestException as ошибка:
    print("Проблема: другая сетевая ошибка —", ошибка)

