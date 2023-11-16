import random

def get_user_choice():
    user_choice = input("Выберите: камень, ножницы,бумага, ящерица или спок? ").lower()
    while user_choice not in ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']:
        print("Неверный ввод. Пожалуйста, выберите заново")
        user_choice = input("Выберите: камень, ножницы или бумага, ящерица или спок? ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага', 'ящерица', 'спок'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
            (user_choice == 'камень' and computer_choice == 'ножницы') or
            (user_choice == 'камень' and computer_choice == 'ящерица') or
            (user_choice == 'ножницы' and computer_choice == 'бумага') or
            (user_choice == 'ножницы' and computer_choice == 'ящерица') or
            (user_choice == 'бумага' and computer_choice == 'камень') or
            (user_choice == 'бумага' and computer_choice == 'спок') or
            (user_choice == 'ящерица' and computer_choice == 'бумага') or
            (user_choice == 'ящерица' and computer_choice == 'ножницы') or
            (user_choice == 'спок' and computer_choice == 'камень') or
            (user_choice == 'спок' and computer_choice == 'ножницы') 
        ):
        return f"Вы выиграли!"
    else:
        return f"Вы проиграли."


def game():
    print("Добро пожаловать в игру 'камень, ножницы, бумага DLS:SHELDON'")
    score = {'you': 0, 'ai': 0}

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "Вы выиграли!":
            score['you'] += 1
        
        elif result == "Вы проиграли.":
            score['ai'] += 1
        
        print(f"Счет: Вы - {score['you']}, AI - {score['ai']}")
        
        
        if score['you'] == 3:
            print("Вы победили!")
            break
        
        elif score['ai'] == 3:
            print("AI победил!")
            break
        
        
        play_again = input("Гоу ту опять? (да/нет) ").lower()
        if play_again != 'да':
            print("Ну лан. До встречи работяга")
            break

game()
