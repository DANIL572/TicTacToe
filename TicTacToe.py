def playing_field(field):
    # Проходим по каждой строке игрового поля
    for row in field:
        # Выводим строку, разделяя элементы символом " | "
        print(" | ".join(row))
        # Разделительная линия между строками
        print("-" * (len(row) * 4 - 3))

# Создаем пустое игровое поле размером 3x3
field = [[" " for _ in range(3)] for _ in range(3)]

# Функция для ввода имен игроков и символов
def players():
    # Создаем словарь с данными игроков
    players_dict = {
        "player1": {"name1": "имя", "symbol": "X"}, # Игрок 1 с символом Х
        "player2": {"name2": "имя", "symbol": "O"}  # Игрок 2 с символом 0
    }
    # Запрашиваем имена игроков у пользователей
    players_dict["player1"]["name1"] = input("Введите имя 1 игрока: ")
    players_dict["player2"]["name2"] = input("Введите имя 2 игрока: ")
    return players_dict

# Функция для проверки победных условий
def assigning_coefficients():
    # Создаем список всех возможных выигрышных комбинаций
    coefficients = [
        [field[0][0], field[0][1], field[0][2]],    # Горизонталь 1
        [field[1][0], field[1][1], field[1][2]],    # Горизонталь 2
        [field[2][0], field[2][1], field[2][2]],    # Горизонталь 3
        [field[0][0], field[1][0], field[2][0]],    # Вертикаль 1
        [field[0][1], field[1][1], field[2][1]],    # Вертикаль 2
        [field[0][2], field[1][2], field[2][2]],    # Вертикаль 3
        [field[0][0], field[1][1], field[2][2]],    # Диагональ 1
        [field[2][0], field[1][1], field[0][2]]     # Диагональ 2
    ]
    # Проверяем, есть ли в поле выигрышная комбинация
    for line in coefficients:
        if line[0] == line[1] == line[2] and line[0] != " ":
            return True    # Возвращаем True, если есть победитель
    return False    # Иначе возвращаем False

# Получаем данные игроков
players_dict = players()
# Отображаем начальное игровое поле
playing_field(field)
# Устанавливаем текущего игрока (начинает игрок 1)
current_player = players_dict["player1"]["name1"]

run = True
game_over = False

# Основной игровой цикл
while run:
    try:
        # Запрашиваем номер строки у текущего игрока
        row = int(input(f"{current_player}, введите номер строки (1-3): ")) - 1
        if row not in range(3):    # Проверка допустимого диапазона
            raise IndexError("Ошибка: Номер строки вне допустимого диапазона")
        # Запрашиваем номер столбца у текущего игрока
        column = int(input(f"{current_player}, введите номер столбца (1-3): ")) - 1
        if column not in range(3):    # Проверка допустимого диапазона
            raise IndexError("Ошибка: Номер столбца вне допустимого диапазона")
         
        # Проверяем, пуста ли выбранная ячейка
        if field[row][column] == " ":
            # Заполняем ячейку символом текущего игрока
            field[row][column] = players_dict["player1"]["symbol"] if current_player == players_dict["player1"]["name1"] else players_dict["player2"]["symbol"]
            # Проверяем, есть ли победитель
            if assigning_coefficients():
                playing_field(field)    # Отображаем итоговое игровое поле
                print(f"Игрок {current_player} победил!")
                print("Игра завершена")
                game_over = True
            # Проверяем, заполнено ли всё поле (ничья)
            if all(cell != " " for row in field for cell in row):
                playing_field(field)    # Отображаем итоговое поле
                print("Ничья!")
                print("Игра завершена")    
                game_over = True
            # Переключаем игрока
            current_player = players_dict["player2"]["name2"] if current_player == players_dict["player1"]["name1"] else players_dict["player1"]["name1"]
        else:
            print("Эта ячейка уже занята. Попробуйте снова.")
        playing_field(field)
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число")
    except IndexError as e:
        print(e)
    while game_over:    # Основной цикл для повторного запуска игры
        # Спрашиваем игроков, хотят ли они сыграть ещё раз
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if play_again == "нет":  # Если ответ отрицательный, выходим из цикла
            print("Спасибо за игру! До скорых встреч!")
            run = False
            game_over = False
        elif play_again == "да":
            players_dict = players()  # Получаем данные игроков
            field = [[" " for _ in range(3)] for _ in range(3)]  # Обновляем игровое поле
            playing_field(field)
            current_player = players_dict["player1"]["name1"]
            game_over = False
        else:
            print("Ошибка: ответ может быть да либо нет")
