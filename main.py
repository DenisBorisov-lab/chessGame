import os
import time

import back
from back import *

count = 0
letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


def is_present(string: str) -> bool:
    if len(string) == 2:
        try:
            current_index = string[0:1]
            current_row = 8 - int(string[1:2])
            if 8 > current_row > 0:
                figure = back.field[current_row][letter_dictionary[current_index]]
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


while True:

    if count != 0:
        os.system("cls")

    generate_field()
    if count % 2 == 0:
        print("Ход белых, выберите фигуру: ")
    else:
        print("Ход чёрных, выберите фигуру: ")
    count += 1
    start = input()
    if is_present(start):
        pass
    else:
        print("Такой фигуры не существует, попробуйте ещё раз!")
        time.sleep(2)
        count -= 1
        continue

    print("Сделайте ход: ")
    end = input()
    if is_present(end):
        pass
    else:
        print("Такого хода не существует, попробуйте ещё раз!")
        time.sleep(2)
        count -= 1
        continue
