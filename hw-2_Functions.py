# 1) Заменить в произвольной строке согласные буквы на гласные.
import random

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"


def replace_consonants(my_string):
    for i in my_string:
        if i in consonants:
            my_string = my_string.replace(i, vowels[random.randint(0, 4)])
    return my_string


print(replace_consonants(input("Enter any string: ")))

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}
]


# 2.1) Отсортировать массив из словарей по значению ключа 'age'


def sort_by_age(data):
    return sorted(data, key=lambda d: d['age'])


print("Sorted by Age - {}".format(sort_by_age(data)))


# 2.2) сгруппировать данные по значению ключа 'city'

def group_by_city(data):
    result = {}
    for i in data:
        result.setdefault(i['city'], []).append(i)
    for k, v in result.items():
        for a in v:
            a.pop('city')
    return result


print("Grouped by city - {}".format(group_by_city(data)))

# 3) У вас есть последовательность строк. Необходимо определить наиболее
# часто встречающуюся строку в последовательности.


def most_frequent(list_var):
    if list_var:
        count_var = {list_var.count(var): var for var in list_var}
        return count_var[max(count_var)]
    else:
        return print("List is Empty")


print("Most frequent item - {}".format(
     most_frequent(['a', 'a', 'bi', 'bi', 'bi'])))
