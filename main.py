from back import *
import os

count = 0
letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

def is_present(string: str) -> bool:
    if len(string) == 2:
        try:
            return True
        except IndexError:
            return False
    else:
        return False

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
    if is_present(start):
        pass
    else:
        print("Такой фигуры не существует, попробуйте ещё раз!")
        continue
    print("Сделайте ход: ")
    end = input()



