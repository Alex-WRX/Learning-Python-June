def my_fun (a1, a2):
    try:
        res = a1 ** a2
    except TypeError:
        return 'Enter a float number and a negative power'
    return res

print(my_fun(5.6, -4))

