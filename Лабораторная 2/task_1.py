money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
counter = 0  # Количество месяцев без долгов

while True:
    if money_capital < spend:
        break
    money_capital += salary
    money_capital -= spend
    if counter > 1:
        spend *= 1 + increase
    counter += 1
print("Количество месяцев, которое можно протянуть без долгов:", counter)


