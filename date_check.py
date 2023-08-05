# 1.Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
#
# 2.В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from datetime import datetime
import sys


def date_check(in_arg: list):
    """В функции обрабатывается введённая в консоли дата и возвращается "True' или 'False' взависимости от того
       верный ли формат даты указан или нет.
       Значение даты можно ввести в терминале, например: 'python date_check.py 12.12.20002'"""

    try:
        value_from_terminal = in_arg[1]
        datetime.strptime(value_from_terminal, '%d.%m.%Y').date()
        print(in_arg)
        return True
    except IndexError:
        try:
            print("Не найден аргумент в функции 'date_check()'")

            _date_string = input(f"Укажите дату в формате дд.мм.гггг: ")
            datetime.strptime(_date_string, '%d.%m.%Y').date()
            print("yes")
            return True
        except ValueError:
            print("no")
            return False

    except ValueError:
        print("no arg")
        return False


if __name__ == "__main__":
    """Просто запуск функции"""

    date_check(sys.argv)
