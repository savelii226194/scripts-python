with open("task1.log", "r") as файл:
    строки = файл.readlines()

всего_строк = len(строки)
print(f"Всего строк: {всего_строк}")
ошибки = []
for строка in строки:
    if "ERROR" in строка:
        ошибки.append(строка.strip())

print(f"Из них ERROR: {len(ошибки)}")
if len(ошибки) == 0:
    print("ошибок не найдено")
else:
    for ошибка in ошибки:
        print("-", ошибка)

