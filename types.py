# a = 2
# b = 0.5
# print(a + b)
# name = "Даниил".replace("Даниил", "My Lord")
# a = "Привет"
# b = f'{a}, {name}!'
# print(b)
# v = int(input('Введите число от 1 до 10: '))
# print(v)
# v = v + 10
# print(v)
# name = input('Введите ваше имя: ')
# a = f'Привет {name}! Как дела?'
# print(a)
# print (float('1'))
# print (int(float('2.5')))
# print (bool(1))
# print (bool(''))
# print (bool(0))
# list = [3, 5, 7, 9, 10.5]
# print(list)
# list.append("Python")
# print(list)
# print(len(list))
# print(list[0])
# print(list[-1])
# print(list[1:4])
# # index = list.index("Python")
# # del list[index]
# list.remove("Python")
# print(list)
def get_summ(one, two, delimetr ='&'):
    string_1 = str(one)
    string_2 = str(two)
    unite_string = f'{string_1}{delimetr}{string_2}'.upper()
    return unite_string

result = get_summ("Learn", "python")
print(result)