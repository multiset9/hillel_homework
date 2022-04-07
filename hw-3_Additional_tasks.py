# 8) Дано целое число. Необходимо подсчитать произведение
# всех цифр в этом числе, за исключением нулей.

def get_multiplication(number):
    result = 1

    if number.isnumeric() and number != "0":
        if "0" in number:
            number = number.replace("0", "")
        for i in number:
            result = result * i
        return result
    else:
        return "Number is not valid"


print("Multiplication all digits in the number - {}".format(
    get_multiplication(str(30))))


# 9) Есть массив с положительными числами и число n
# (def some_function(array, n)). Необходимо найти n-ую степень элемента в
# массиве с индексом n. Если n за границами массива, тогда вернуть -1.

def get_exponentiation(list_of_values, extent):
    try:
        value = int(list_of_values[extent])
    except IndexError:
        return -1
    return value**extent


print("Power of N element in array at index N - {}".format(
    get_exponentiation([1, 3.4, 3, "2", 5.2], 3)))


# 10) Есть строка со словами и числами, разделенными пробелами
# (один пробел между словами и/или числами). Слова состоят только из букв.
# Вам нужно проверить есть ли в исходной строке три слова подряд.

def is_three_words(string):
    count = 0
    for word in string.split():
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print("There are three words in the string - {}".format(
    is_three_words("hello 1 one two three 15 world")))
