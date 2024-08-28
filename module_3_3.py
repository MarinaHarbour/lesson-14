def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params(a=2, b=4, c=False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'Heloo', False]
values_dict = {'a': 1, 'b': 'string', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6, 'Bye']
print_params(*values_list_2, 42)
