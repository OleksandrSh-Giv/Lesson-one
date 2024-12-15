def calculator():
    print("Проста математична програма (+, -, *, /)\n")

    # Запит чисел у користувача
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть дію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))


        # Обчислення результату на основі оператора
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Перевірка ділення на 0
            if num2 == 0:
                print("Помилка: Ділення на 0 неможливе!")
                return
            result = num1 / num2
        else:
            print("Помилка: Невідома дія. Використовуйте тільки +, -, *, /.")
            return

        # Вивід результату
        print(f"Результат: {result}")
    except ValueError:
        print("Помилка: Введіть числові значення!")

# Виклик функції
calculator()
