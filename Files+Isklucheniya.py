# Чтобы что-то открыть мы используем функцию open в качесте аргумента к кторой указать путь и имя файла
#Для открытия файла есть только 2 режима, только для чтения read и  команда которая перезапишет все в файле write
#Обязательно закрываем файл close() иначе данные потеряются/не сохранятся
# R - чтение W - перезапись (если в этом режиме файл не создан то питон его создаст) A - добавление
#
#
#
#
f = open('1.txt', 'w')#Путь не указан потому что файл находится в каталоге с исполнительным файлом
f.write('hello file')
f.close
# Чтение
f = open('1.txt', 'r')#Путь не указан потому что файл находится в каталоге с исполнительным файлом
print(f.read())
f.close
#Для того чтобы не закрывать файл и не проебывать есть конструкция with которая делает все сама
with open('1.txt', 'a') as f:
    f.write(' ' + 'hahaha')
    
#a = int(input('Введите число А '))
#b = int(input('Введите число Б '))
#print(a/b) 
# Здесть стандартное деление, но если мы поделим на 0 будет ошибка, поєтому есть исключение.
try:
    a = int(input('Введите число А '))
    b = int(input('Введите число Б '))
    print(a/b)
except ZeroDivisionError:
    print('Нельзя делить на ноль')





    
    






