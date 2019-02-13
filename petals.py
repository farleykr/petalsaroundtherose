import random

dice_dict = {
    1: u'\u2680',
    2: u'\u2681',
    3: u'\u2682',
    4: u'\u2683',
    5: u'\u2684',
    6: u'\u2685'
}


def play_game():
    total = 0
    dice_roll = [random.randint(1, 6) for x in range(1, 6)]

    for x in dice_roll:

        if x == 3:
            total += 2
        elif x == 5:
            total += 4
        else:
            pass

    print(f'{dice_dict[dice_roll[0]]}\
            {dice_dict[dice_roll[1]]}\
            {dice_dict[dice_roll[2]]}\
            {dice_dict[dice_roll[3]]}\
            {dice_dict[dice_roll[4]]}')

    guess = input('Can you guess the answer? ')

    if int(guess) == total:
        print('Right!')
        play_again()

    else:
        print(f'Wrong! The answer is {total}.')
        play_again()

def play_again():
        answer = input('do you want to play again? (Y/N) ')

        if answer.upper() == 'Y':
            play_game()

        else:
            pass

play_game()
