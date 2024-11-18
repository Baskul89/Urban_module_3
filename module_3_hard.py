def calculate_structure_sum(data):
    if isinstance(data, str): #data - строка
        return len(data)
    elif (isinstance(data, int) or #data - число
          isinstance(data, float)):
        return data
    elif (isinstance(data, list) or #data - список, кортреж, множество
          isinstance(data, tuple) or
          isinstance(data, set)):
        sum_ = 0
        for d in data:
            sum_ += calculate_structure_sum(d)
        return sum_
    elif isinstance(data, dict): #data - словарь
        sum_ = 0
        for key, value in data.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)
        return sum_
    else:
        print("Неверный тип даных: ", data)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)




