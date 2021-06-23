revenue = int(input('Введите значение выручки '))
costs = int(input('Введите значение издержек '))
Profitability = (revenue / costs) * 100
if revenue > costs:
    print('Прибыль')
    employees = int(input('Введите количество сотрудников '))
    Profitability1 = Profitability / employees
    print(f'{Profitability1}')
else: print('Убыток')