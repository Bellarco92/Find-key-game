from math import sqrt
from random import randint

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)

player_x = 0
player_y = 0
player_found_key = False


while not  player_found_key:
    print()
    print('Moesz udać się w kierunkach określonych jako [W/A/S/D]: ')

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
        if player_x > 0:
            print('Ups! Uderzasz w ścianę!')
            player_y = 0

    case 'd':
        player_x += 1
        if player_x > GAME_WIDTH:
            print('Ups! Uderzasz w ścianę!')
            player_x = GAME_WIDTH
    case 'q':
        quit()
    case '-':
        print('Nie wiem dokąd idziesz...')
        continue

if player_x == key_x and player_y == key_y:
    print('Klucz do skarbu jest Twój!')

print(player_x, player_y)

