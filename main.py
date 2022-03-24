
my_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

# 1.1 Remove the same elements from list
print("1.1 List without duplicates - {}".format(list(set(my_list))))

# 1.2 Output the 3 largest values
new_list = sorted(list(set(my_list)), reverse=True)
print("1.2 Thee largest values - {}".format(new_list[:3]))

# 1.3 Output the index of min value
print("1.3 The index of min value - {}".format(my_list.index(min(my_list))))

# 1.4 Output the original array in reverse order
print("1.4 Reversed list - {}".format(my_list[::-1]))

# 2. Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать
# в результирующий массив только четные числа.

generated_list = [i for i in range(101) if i % 2 == 0]
print("2. List of even values - {}".format(generated_list))
