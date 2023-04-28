# Список ідентифікаторів зайнятих місць для паркування
occupied_parking_spaces = [3, 6, 10, 12]

def is_parking_space_occupied(parking_space_id):
    """
    Перевіряє, чи зайняте місце для паркування з вказаним ідентифікатором.
    Повертає True, якщо місце зайняте, та False - якщо вільне.
    """
    return parking_space_id in occupied_parking_spaces


# Запит номера місця для паркування від користувача
parking_space_id = int(input("Введіть номер місця для паркування: "))

# Перевірка, чи зайняте введене користувачем місце для паркування
if is_parking_space_occupied(parking_space_id):
    print("Місце зайняте")
else:
    print("Місце вільне")
