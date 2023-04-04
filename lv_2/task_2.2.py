# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.


def quarter_of():
    try:
        n = int(input('Введите номер месяца:'))
        if 1 <= n <= 3 :
            return 'Первый квартал'
        elif 4 <= n <= 6 :
            return 'Второй квартал'
        elif 7 <= n <= 9 :
            return 'Третий квартал'
        elif 10 <= n <= 12 :
            return 'Четвертый квартал'
        else : return 'Ошибка при вводе данных, введите номер месяца!!!'
    except ValueError:print('Ошибка при вводе данных, это не число. Введите номер месяца!!!')

print(quarter_of())

# хм, ну может быть лучше было избавиться здесь вовсе от конструции if-elif, и переделать это полностью в try-except
# мой вариант опять же через словари)

def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    return [k for k,v in q.items() if v[0] <= month <= v[1]][0]
