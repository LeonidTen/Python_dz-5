# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_index(lst, minimum, maximum):
    index = []
    for i in range(len(lst)):
        if lst[i] >= minimum and lst[i] <= maximum:
            index.append(i)
    return index

# Пример использования:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_val = 3
max_val = 7
result_indexes = find_index(my_list, min_val, max_val)
print(result_indexes)