while True: # Створює нескінченний цикл, у якому користувач повторно вводить значення, поки воно не відповідатиме умовам
 try:
  # Просимо користувача ввести число
  number = input("Введіть 4-значне число: ")

  # Перевіряємо, чи це число і чи воно складається рівно з 4 цифр
  if len(number) == 4 and number.isdigit():
   number = int(number)  # Конвертуємо в ціле число для обчислень

   # Розділяємо на окремі цифри
   n1 = number // 1000
   n2 = (number % 1000) // 100
   n3 = (number % 100) // 10
   n4 = number % 10


   # Виводимо цифри стовпчиком
   print(n1)
   print(n2)
   print(n3)
   print(n4)
   print("Спрацювало все добре",)
   break  # Завершуємо цикл після успішного введення
  else:
   print("Помилка: потрібно ввести саме 4 цифри. Спробуйте ще раз.")
 except ValueError:
  print("Помилка: введено некоректні дані. Спробуйте ще раз.")


