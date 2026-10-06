import requests

def проверить_сервер(адрес):
    try:
        ответ = requests.get(адрес, timeout=5)
        время = ответ.elapsed.total_seconds()
        if ответ.status_code >= 400:
            print(адрес, "-> ошибка, код:", ответ.status_code, ", время:", время)
            return False
        print(адрес, "-> доступен, код:", ответ.status_code, ", время:", время)
        return True
    except requests.exceptions.RequestException:
        print(адрес, "-> недоступен")
        return False
серверы = [
    "https://github.com",
    "https://api.github.com",
    "https://этот-адрес-точно-не-существует-99999.com",
    "https://api.github.com/users/savelii-takogo-polzovatelya-tochno-net-99999",
]

доступно = 0
for адрес in серверы:
    if проверить_сервер(адрес):
        доступно = доступно + 1

print("Доступно", доступно, "из", len(серверы), "серверов")

