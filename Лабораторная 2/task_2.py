salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.05  # Ежемесячный рост цен

# Начальная подушка безопасности
money_capital = 0

for i in range(months):
    # Подсчет разницы на текущий месяц
    shortfall = spend - salary
    money_capital += shortfall  # Добавляем разницу к подушке безопасности

    # Увеличиваем расходы на 5% после первого месяца
    spend *= (1 + increase)

# Округляем результат до целого числа
money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
