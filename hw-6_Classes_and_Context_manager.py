# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:


class IpProcessing:
    def __init__(self, ip_addresses):
        self.ip_addresses = ip_addresses

    def get_reversed_ip(self):
        reversed_ip = []
        for ip in self.ip_addresses:
            reversed_ip.append(f'{ip} -> {".".join(ip.split(".")[::-1])}')
        return reversed_ip

    def get_ip_without_first_octet(self):
        without_first_octet = []
        for ip in self.ip_addresses:
            without_first_octet.append(f'{ip} -> {".".join(ip.split(".")[1::])}')
        return without_first_octet

    def get_last_octet(self):
        last_octet = []
        for ip in self.ip_addresses:
            last_octet.append(f'{ip} -> {".".join(ip.split(".")[-1::])}')
        return last_octet


ip_addresses = ["10.11.12.13", "10.11.12.14", "10.11.12.15"]
ip_processing = IpProcessing(ip_addresses)

# # 1) Получить список IP адресов в развернутом виде
# # (пример 10.11.12.13 -> 13.12.11.10)
# print("Reversed IP addresses:")
# print(ip_processing.get_reversed_ip())
# print("-"*100)
# # 2) Получить список IP адресов без первых октетов
# # (пример 0.11.12.13 -> 11.12.13)
# print("IP addresses without first octets:")
# print(ip_processing.get_ip_without_first_octet())
# print("-"*100)
# # 3) Получить список последних октетов IP адресов
# # (пример 10.11.12.13 -> 13)
# print("IP addresses last octets:")
# print(ip_processing.get_last_octet())
# print("-"*100)

# Задача-2
# Вам необходимо написать
# класс который будет описывать работу с файлами, а
# именно:
# 1) Запись данных в файл
# 2) Чтение данных из файла
# 3) Удаление данных из файла


class FilesProcessing:
    def __init__(self, file_path, coding):
        self.file_path = file_path
        self.coding = coding

    def write_file(self, data):
        with open(self.file_path, 'w', encoding=self.coding) as f:
            f.write(data)

    def read_file(self):
        with open(self.file_path, 'r', encoding=self.coding) as f:
            print(f.read())

    def delete_content(self):
        with open(self.file_path, 'w') as f:
            f.truncate(0)


path = "./test_data/test.txt"
files_processing = FilesProcessing(path, coding="UTF-8")
files_processing.write_file(data="TEST, test, TeSt!!!")
files_processing.read_file()
files_processing.delete_content()
