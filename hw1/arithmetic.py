# Задання прикладу
example = 4 * 100 - 54

# Виведення інформації та отримання відповіді користувача
print("Solve the following expression: 4 * 100 - 54")
user_answer = input("Your answer: ")

# Перевірка правильності відповіді
if int(user_answer) == example:
    print("Correct!")
else:
    print("Incorrect. The correct answer is:", example)