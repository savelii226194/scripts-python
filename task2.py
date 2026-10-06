import json

with open("config.json", "r") as файл:
    конфиг = json.load(файл)
print("Имя сервиса:", конфиг.get("имя_сервиса", "не указано"))
print("Порт:", конфиг.get("порт", "не указан"))
print("Debug режим:", конфиг.get("debug", "не указан"))
print("Разрешённые хосты:", конфиг.get("разрешённые_хосты", "не указаны"))
конфиг["порт"] = 9999
with open("config.json", "w") as файл:
    json.dump(конфиг, файл, indent=2)
конфиг["порт"] = 9999
with open("config.json", "w") as файл:
    json.dump(конфиг, файл, indent=2)

