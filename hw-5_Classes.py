# 1) Реализовать класс который бы производил разные операции
# над 2мя переданными числами.

class ProcessInput:
    def __init__(self, a, b):
        self.arg_1 = a
        self.arg_2 = b

    def add(self):
        return self.arg_1 + self.arg_2

    def subtract(self):
        return self.arg_1 - self.arg_2

    def multiple(self):
        return self.arg_1 * self.arg_2

    def divide(self):
        try:
            return int(self.arg_1/self.arg_2)
        except ZeroDivisionError:
            raise ZeroDivisionError("ZeroDivisionError occurs when a"
                                    " number is divided by a zero")


process_input = ProcessInput(a=20, b=10)
print(process_input.add())  # выведет 30
print(process_input.subtract())  # выведет 10
print(process_input.multiple())  # выведет 200
print(process_input.divide())  # выведет 2
