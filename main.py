import os
import time
from alphabeta import *
import back
from back import *

count = 0
letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


def get_figure(string: str):
    current_index = string[0:1]
    current_row = 8 - int(string[1:2])
    return back.field[current_row][letter_dictionary[current_index]]


def is_present(string: str) -> bool:
    if len(string) == 2:
        try:
            current_index = string[0:1]
            current_row = 8 - int(string[1:2])
            if 8 > current_row >= 0:
                get_figure(string)
                return True
            else:
                return False
        except IndexError:
            return False
        except ValueError:
            return False
        except KeyError:
            return False
    else:
        return False


def not_null(string: str):
    if get_figure(string) == 0:
        return True
    else:
        return False


def not_enemy(string: str):
    if count % 2 == 0:
        if get_figure(string) in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            return True
        else:
            return False
    else:
        if get_figure(string) in "♚ ♛ ♜ ♝ ♞ ♟".split(" "):
            return True
        else:
            return False

print("Вы хотите играть с ботом?[Y/n]")
choice = input()
if choice == "Y":
    depth = 0
    print("вы играете за белых!")
    while True:

        if count != 0:
            os.system("clear")

        generate_field()
        print("Ход белых, выберите фигуру: ")
        start = input()

        if is_present(start) and not not_null(start) and get_figure(start) in "♚ ♛ ♜ ♝ ♞ ♟".split(" "):
            figure = get_figure(start)
        elif is_present(start) and not_null(start):
            print("Такой фигуры не существует, попробуйте ещё раз!")
            time.sleep(2)
            continue
        else:
            print("Вы выбрали чужую фигуру, попробуйте ещё раз!")
            time.sleep(2)
            count -= 1
            continue

        print("Сделайте ход: ")
        end = input()
        done_figure = ""
        if is_present(end):
            to_go = back.able_to_go(figure, start)
            to_eat = back.able_to_eat(figure, start)
            if end in to_go or end in to_eat:
                start_index = start[0:1]
                start_row = 8 - int(start[1:2])
                end_index = end[0:1]
                end_row = 8 - int(end[1:2])
                done_figure = str(field[end_row][letter_dictionary[end_index]])
                field[start_row][letter_dictionary[start_index]] = 0
                field[end_row][letter_dictionary[end_index]] = figure
            else:
                print("Вы не можете сделать такой ход, попробуйте ещё раз!")
                time.sleep(2)
                continue

        else:
            print("Такого хода не существует, попробуйте ещё раз!")
            time.sleep(2)
            count -= 1
            continue

        if done_figure == "♔":
            generate_field()
            print("Шах и мат, белые выиграли!")
            break
        movement = minimax(field, depth, 10000, -10000, False)
        s = movement[0:2]
        e = movement[2:4]
        start_index = s[0:1]
        start_row = 8 - int(s[1:2])
        end_index = e[0:1]
        end_row = 8 - int(e[1:2])
        done_figure = str(field[end_row][letter_dictionary[end_index]])
        figure = field[start_row][letter_dictionary[start_index]]
        field[start_row][letter_dictionary[start_index]] = 0
        field[end_row][letter_dictionary[end_index]] = figure


else:
    while True:

        if count != 0:
            os.system("clear")

        generate_field()
        if count % 2 == 0:
            print("Ход белых, выберите фигуру: ")
        else:
            print("Ход чёрных, выберите фигуру: ")
        count += 1
        start = input()

        if is_present(start) and not not_null(start) and not_enemy(start):
            figure = get_figure(start)
        elif is_present(start) and not_null(start):
            print("Такой фигуры не существует, попробуйте ещё раз!")
            time.sleep(2)
            count -= 1
            continue
        else:
            print("Вы выбрали чужую фигуру, попробуйте ещё раз!")
            time.sleep(2)
            count -= 1
            continue

        print("Сделайте ход: ")
        end = input()
        done_figure = ""
        if is_present(end):
            to_go = back.able_to_go(figure, start)
            to_eat = back.able_to_eat(figure, start)
            if end in to_go or end in to_eat:
                start_index = start[0:1]
                start_row = 8 - int(start[1:2])
                end_index = end[0:1]
                end_row = 8 - int(end[1:2])
                done_figure = str(field[end_row][letter_dictionary[end_index]])
                field[start_row][letter_dictionary[start_index]] = 0
                field[end_row][letter_dictionary[end_index]] = figure
            else:
                print("Вы не можете сделать такой ход, попробуйте ещё раз!")
                time.sleep(2)
                count -= 1
                continue

        else:
            print("Такого хода не существует, попробуйте ещё раз!")
            time.sleep(2)
            count -= 1
            continue

        if done_figure == "♔":
            generate_field()
            print("Шах и мат, белые выиграли!")
            break
        elif done_figure == "♚":
            generate_field()
            print("Шах и мат, чёрные выиграли!")
            break



