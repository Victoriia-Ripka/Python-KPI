# Запит користувача на введення чотирьох чисел
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Окреме обчислення суми перших двох та інших двох чисел
sum_first_two = num1 + num2
sum_last_two = num3 + num4

# Розділення першої суми на другу
result = sum_first_two / sum_last_two

# Виведення результату з двома цифрами після коми
print(f"Result: {result:.2f}")