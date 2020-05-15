# HW 1 - Нужно реализовать Польскую нотацию для двух положительных чисел.
# Реализовать нужно будет следующие операции:
# Сложение
# Вычитание
# Умножение
# Деление
# + 2 2 Ответ должен быть: 4




def polish_notation():
    try:
        input_data = input("Введите через пробел: знак оператора, число1, число 2: ")
        symbols = input_data.split()
        operator = str(symbols[0])
        digit1 = int(symbols[1])
        digit2 = int(symbols[2])
        assert len(symbols) == 3, "Введено неверное кол-во символов"

        try:
            if operator == "+":
                result = digit1 + digit2
                return print(result)

            elif operator == "-":
                result = digit1 - digit2
                return print(result)
            elif operator == "*":
                result = digit1 * digit2
                return print(result)
            elif operator == "/":
                result = digit1 / digit2
                return print(result)
            else:
                return(print("Вы ввели неверный оператор"))
        except ZeroDivisionError as ex:
            print(f'Деление на ноль запрещено. Ошибка: {ex}')

    except AssertionError as e:
        return print(f'Ошибка: {e}')

    except (IndexError, ) as e:
        print(f'Не введены пробелы. Ошибка: {e}')

    except ValueError as e:
        print(f'Введены буквы. Ошибка: {e}')

polish_notation()
# polish_notation("+", 9,3)
# polish_notation("*", 9,3)
# polish_notation("/", 9,3)
# polish_notation("-", 9,3)
# polish_notation(6, 9,3)