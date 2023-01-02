per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))/100
float_percent = list(per_cent.values())
#находим сумму по каждому отдельному банку
dep_osit = [money * i for i in float_percent]
#формируем список deposit значений
deposit = [int(dep_osit) for dep_osit in dep_osit]
#находим максимальную сумму
deposit_max = max(deposit)
print(deposit)
print("Максимальная сумма, которую Вы можете заработать -", deposit_max)

