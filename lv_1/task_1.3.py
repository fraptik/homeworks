# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

n = int(input('Введите номер месяца:'))
if (n > 0) and (n <= 12) :
    if (n % 2 != 0) and (n != 2) and (n < 8):
        print('В этом месяце 31 день')
    elif (n % 2 == 0) and (n != 2) and (n >= 8):
        print('В этом месяце 31 день')
    elif n == 2 :
        print('В этом месяце 28 дней')
    else:print('В этом месяце 30 дней')
else: print('Такого месяца нет!')