from math import sqrt
from random import randint

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)

player_x = 0
player_y = 0
player_found_key = False
steps = 0

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

while not player_found_key:
    steps += 1
    print()
    print('Mozesz udać się w kierunkach określonych jako [W/A/S/D]: ')

    move = input('Dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y += 1

            if player_y > GAME_HEIGHT:
                print('Ups! Uderzasz w ścianę!')
                player_y = GAME_HEIGHT

        case 's':
            player_y -= 1

            if player_y < 0:
                print('Ups! Uderzasz w ścianę!')
                player_y = 0

        case 'a':
            player_x -= 1

            if player_x < 0:
                print('Ups! Uderzasz w ścianę!')
                player_x = 0

        case 'd':
            player_x += 1

            if player_x > GAME_WIDTH:
                print('Ups! Uderzasz w ścianę!')
                player_x = GAME_WIDTH

        case 'q':
            quit('Koniec gry!')
        case '-':
            print('Nie wiem dokąd idziesz...')
            continue

    if player_x == key_x and player_y == key_y:
        print('Klucz do skarbu jest Twój!')
        print(f'Wykonałeś/wykonałaś {steps} ruchów.')
        quit()

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move > distance_after_move:
            print('Ciepło!')
    else: 
        print('Zimno!')

    distance_before_move = distance_after_move



