def div(a_1, a_2):
    try:
        a_1, a_2 = int(a_1), int(a_2)
        div_num = a_1 / a_2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return  'Zero division forbidden'
    return round(div_num, 4)



print(div(input('Enter first number - '), input('Enter second number - ')))