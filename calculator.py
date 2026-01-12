"""
Простой калькулятор с базовыми математическими операциями.
"""


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание второго числа из первого."""
    return a - b


def multiply(a, b):
    """Умножение двух чисел."""
    return a * b


def divide(a, b):
    """Деление первого числа на второе."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b


def power(a, b):
    """Возведение первого числа в степень второго."""
    return a ** b


def main():
    """Интерактивный режим калькулятора."""
    print("=== Простой калькулятор ===\n")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("0. Выход\n")
    
    while True:
        try:
            choice = input("Выберите операцию (0-5): ")
            
            if choice == '0':
                print("До свидания!")
                break
            
            if choice not in ['1', '2', '3', '4', '5']:
                print("Неверный выбор! Попробуйте снова.\n")
                continue
            
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            operations = {
                '1': ('+', add),
                '2': ('-', subtract),
                '3': ('*', multiply),
                '4': ('/', divide),
                '5': ('^', power)
            }
            
            operator, func = operations[choice]
            result = func(num1, num2)
            
            print(f"\nРезультат: {num1} {operator} {num2} = {result}\n")
            
        except ValueError as e:
            print(f"Ошибка: {e}\n")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана. До свидания!")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}\n")


if __name__ == "__main__":
    main()
