# Программа "Викторина"
"""
Программа будет задавать вам вопросы несколько раз
"""

# Импорт функций из модуля
from my_functions import get_person_and_question

rounds = int(input('Сколько раз вы хотите играть?'))

for i in range(rounds):
    get_person_and_question()

print('Пока!')
