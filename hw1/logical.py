# Задання змінних
var1 = 5
var2 = 10

# Складні логічні вирази з оператором and
logical_expr1 = (var1 > 0) and (var2 < 20)
logical_expr2 = (var1 == 5) and (var2 == 15)

# Складні логічні вирази з оператором or
logical_expr3 = (var1 > 0) or (var2 > 20)
logical_expr4 = (var1 == 3) or (var2 == 10)

# Виведення результатів
print("Logical Expression 1 (and):", logical_expr1)
print("Logical Expression 2 (and):", logical_expr2)
print("Logical Expression 3 (or):", logical_expr3)
print("Logical Expression 4 (or):", logical_expr4)

# Перевірка чисел на більше чи менше одне від одного
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(num1 > num2)