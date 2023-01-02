per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
float_percent = list(per_cent.values())
#находим сумму по каждому отдельному банку
deposit = [money * i for i in float_percent]
#находим максимальную сумму
deposit_max = max(deposit)
#переводим в целое число
dep_max = int(float(deposit_max))
print("Максимальная сумма, которую вы можете заработать -", dep_max)

