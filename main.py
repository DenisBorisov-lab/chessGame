from back import *
import os

count = 0

while True:

    if count != 0:
        os.system("clear")

    generate_field()
    if count % 2 == 0:
        print("Ход белых, выберите фигуру: ")
    else:
        print("Ход чёрных, выберите фигуру: ")
    count += 1
    string_movement = input()
    print(string_movement)
