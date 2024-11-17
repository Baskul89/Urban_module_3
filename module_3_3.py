def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, [1, 2, 3], "Строка"]
values_dict = {"a": 10, "b": (6, 6, 6), "c": [1, 2]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Строка2", False]
print_params(*values_list_2, 42)