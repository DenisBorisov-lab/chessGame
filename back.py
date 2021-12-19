field = [[0 for j in range(8)] for i in range(8)]
numbers_dictionary = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
black_king = '♔'
black_queen = '♕'
black_rook = '♖'
black_bishop = '♗'
black_knight = '♘'
black_pawn = '♙'
white_king = '♚'
white_queen = '♛'
white_rook = '♜'
white_bishop = '♝'
white_knight = '♞'
white_pawn = '♟'
for i in range(len(field[1])):
    field[1][i] = black_pawn
for i in range(len(field[6])):
    field[6][i] = white_pawn

field[0][0] = black_rook
field[0][7] = black_rook
field[7][0] = white_rook
field[7][7] = white_rook

field[0][1] = black_knight
field[0][6] = black_knight
field[7][1] = white_knight
field[7][6] = white_knight

field[0][2] = black_bishop
field[0][5] = black_bishop
field[7][2] = white_bishop
field[7][5] = white_bishop

field[0][3] = black_queen
field[0][4] = black_king
field[7][3] = white_queen
field[7][4] = white_king


def generate_field():
    row_index = 8
    print(" ┌───┬───┬───┬───┬───┬───┬───┬───┐")
    for i in range(8):

        string_row = ""

        for j in range(len(field[i])):
            string_row += "   " if field[i][j] == 0 else " " + field[i][j] + " "
            string_row += "│"

        print(str(row_index) + "│" + string_row)
        if i != 7:
            print(" ├───┼───┼───┼───┼───┼───┼───┼───┤")
        else:
            print(" └───┴───┴───┴───┴───┴───┴───┴───┘")
        row_index -= 1
    print("   A   B   C   D   E   F   G   H")


def is_empty(x, y):
    if field[x][y] == 0:
        return True
    else:
        return False


def is_present(x: int, y: int):
    if x < 0 or y < 0:
        return False
    if x > 7 or y > 7:
        return False
    return True


def able_to_go(figure: str, start: str):
    abilities = []
    current_index = letter_dictionary[start[0:1]]
    current_row = 8 - int(start[1:2])

    if figure == black_pawn:
        if current_row == 1 and is_empty(current_row + 1, current_index) and is_empty(current_row + 2, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row + 2)))
        if is_empty(current_row + 1, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row + 1)))

    elif figure == white_pawn:
        if current_row == 6 and is_empty(current_row - 1, current_index) and is_empty(current_row - 2, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row - 2)))
        if is_empty(current_row - 1, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row - 1)))
    elif figure == white_rook or figure == black_rook:
        # движение вверх
        up_x = current_row
        vertical_y = current_index
        while up_x > 0:
            up_x -= 1
            if is_empty(up_x, vertical_y):
                abilities.append(numbers_dictionary[vertical_y] + str(8 - up_x))
            else:
                break
        # движение вниз
        down_x = current_row
        while down_x < 7:
            down_x += 1
            if is_empty(down_x, vertical_y):
                abilities.append(numbers_dictionary[vertical_y] + str(8 - down_x))
            else:
                break

        # движение влево
        horizontal_x = current_row
        left_y = current_index
        while left_y > 1:
            left_y -= 1
            if is_empty(horizontal_x, left_y):
                abilities.append(numbers_dictionary[left_y] + str(8 - horizontal_x))
            else:
                break
        # движение вправо
        right_y = current_index
        while right_y < 7:
            right_y += 1
            if is_empty(horizontal_x, right_y):
                abilities.append(numbers_dictionary[right_y] + str(8 - horizontal_x))
            else:
                break
    if figure == black_bishop or figure == white_bishop:
        # возможность ходить вправо вверх
        for i in range(1, 7 - current_index + 1):
            if current_row - i < 0:
                break
            if is_empty(current_row - i, current_index + i):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row - i)))
            else:
                break

        # возможность ходить влево вверх
        for i in range(1, current_index + 1):
            if current_row - i < 0:
                break
            if is_empty(current_row - i, current_index - i):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row - i)))
            else:
                break

        # возможность ходить вправо вниз
        for i in range(1, 7 - current_index + 1):
            if current_row + i > 7:
                break
            if is_empty(current_row + i, current_index + i):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row + i)))
            else:
                break

        # возможность ходить вниз влево
        for i in range(1, current_index + 1):
            if current_row + i > 7:
                break
            if is_empty(current_row + i, current_index - i):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row + i)))
            else:
                break
    if figure == white_knight or figure == black_knight:
        if is_present(current_row + 2, current_index + 1) and is_empty(current_row + 2, current_index + 1):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row + 2)))
        if is_present(current_row + 2, current_index - 1) and is_empty(current_row + 2, current_index - 1):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row + 2)))
        if is_present(current_row + 1, current_index + 2) and is_empty(current_row + 1, current_index + 2):
            abilities.append(numbers_dictionary[current_index + 2] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index + 2) and is_empty(current_row - 1, current_index + 2):
            abilities.append(numbers_dictionary[current_index + 2] + str(8 - (current_row - 1)))
        if is_present(current_row + 1, current_index - 2) and is_empty(current_row + 1, current_index - 2):
            abilities.append(numbers_dictionary[current_index - 2] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index - 2) and is_empty(current_row - 1, current_index - 2):
            abilities.append(numbers_dictionary[current_index - 2] + str(8 - (current_row - 1)))
        if is_present(current_row - 2, current_index + 1) and is_empty(current_row - 2, current_index + 1):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row - 2)))
        if is_present(current_row - 2, current_index - 1) and is_empty(current_row - 2, current_index - 1):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row - 2)))

    if figure == white_king or figure == black_king:
        if is_present(current_row + 1, current_index) and is_empty(current_row + 1, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index) and is_empty(current_row - 1, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row - 1)))
        if is_present(current_row, current_index + 1) and is_empty(current_row, current_index + 1):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - current_row))
        if is_present(current_row, current_index - 1) and is_empty(current_row, current_index - 1):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - current_row))
        if is_present(current_row + 1, current_index + 1) and is_empty(current_row + 1, current_index + 1):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row + 1)))
        if is_present(current_row + 1, current_index - 1) and is_empty(current_row + 1, current_index - 1):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index + 1) and is_empty(current_row - 1, current_index + 1):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row - 1)))
        if is_present(current_row - 1, current_index - 1) and is_empty(current_row - 1, current_index - 1):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row - 1)))
    if figure == white_queen or figure == black_queen:
        # возможность ходить вправо вверх
        for i in range(1, 7 - current_index + 1):
            if current_row - i < 0:
                break
            if is_empty(current_row - i, current_index + i):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row - i)))
            else:
                break

        # возможность ходить влево вверх
        for i in range(1, current_index + 1):
            if current_row - i < 0:
                break
            if is_empty(current_row - i, current_index - i):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row - i)))
            else:
                break

        # возможность ходить вправо вниз
        for i in range(1, 7 - current_index + 1):
            if current_row + i > 7:
                break
            if is_empty(current_row + i, current_index + i):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row + i)))
            else:
                break

        # возможность ходить вниз влево
        for i in range(1, current_index + 1):
            if current_row + i > 7:
                break
            if is_empty(current_row + i, current_index - i):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row + i)))
            else:
                break
                # движение вверх
            up_x = current_row
            vertical_y = current_index
            while up_x > 0:
                up_x -= 1
                if is_empty(up_x, vertical_y):
                    abilities.append(numbers_dictionary[vertical_y] + str(8 - up_x))
                else:
                    break
            # движение вниз
            down_x = current_row
            while down_x < 7:
                down_x += 1
                if is_empty(down_x, vertical_y):
                    abilities.append(numbers_dictionary[vertical_y] + str(8 - down_x))
                else:
                    break

            # движение влево
            horizontal_x = current_row
            left_y = current_index
            while left_y > 1:
                left_y -= 1
                if is_empty(horizontal_x, left_y):
                    abilities.append(numbers_dictionary[left_y] + str(8 - horizontal_x))
                else:
                    break
            # движение вправо
            right_y = current_index
            while right_y < 7:
                right_y += 1
                if is_empty(horizontal_x, right_y):
                    abilities.append(numbers_dictionary[right_y] + str(8 - horizontal_x))
                else:
                    break
    return abilities


def able_to_eat(figure: str, start: str):
    abilities = []
    current_index = letter_dictionary[start[0:1]]
    current_row = 8 - int(start[1:2])
    if figure == black_pawn:
        try:
            if not is_empty(current_row + 1, current_index + 1):
                abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row + 1)))
        except IndexError:
            pass
        except KeyError:
            pass
        try:
            if not is_empty(current_row + 1, current_index - 1):
                abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row + 1)))
        except IndexError:
            pass
        except KeyError:
            pass
    if figure == white_pawn:
        try:
            if not is_empty(current_row - 1, current_index + 1):
                abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row - 1)))
        except IndexError:
            pass
        except KeyError:
            pass
        try:
            if not is_empty(current_row - 1, current_index - 1):
                abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row - 1)))
        except IndexError:
            pass
        except KeyError:
            pass
    if figure == white_rook:
        # обзор фигуры которую можно съесть по вертикали
        for i in range(current_row + 1, 8):
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_row - 1, -1, -1):
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index + 1, 8):
            if not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index - 1, -1, -1):
            if not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

    if figure == black_rook:
        # обзор фигуры которую можно съесть по вертикали
        for i in range(current_row + 1, 8):
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_row - 1, -1, -1):
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index + 1, 8):
            if not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index - 1, -1, -1):
            if not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

    if figure == black_bishop:

        # возможность есть враво вверх
        for i in range(1, 7 - current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index + i) and not field[current_row - i][
                                                                            current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index + i) and field[current_row - i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

        # возможность ходить влево вверх
        for i in range(1, current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index - i) and not field[current_row - i][
                                                                            current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index - i) and field[current_row - i][
                current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

        # возможность ходить вправо вниз
        for i in range(1, 7 - current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index + i) and not field[current_row + i][
                                                                            current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index + i) and field[current_row + i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

        # возможность ходить вниз влево
        for i in range(1, current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index - i) and not field[current_row + i][
                                                                            current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index - i) and not field[current_row + i][
                                                                              current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

    if figure == white_bishop:
        # возможность есть враво вверх
        for i in range(1, 7 - current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index + i) and field[current_row - i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index + i) and not field[current_row - i][
                                                                              current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

        # возможность ходить влево вверх
        for i in range(1, current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index - i) and field[current_row - i][
                current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index - i) and not field[current_row - i][
                                                                              current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

        # возможность ходить вправо вниз
        for i in range(1, 7 - current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index + i) and field[current_row + i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index + i) and not field[current_row + i][
                                                                              current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

        # возможность ходить вниз влево
        for i in range(1, current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index - i) and field[current_row + i][
                current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index - i) and not field[current_row + i][
                                                                              current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

    if figure == white_knight:
        if is_present(current_row + 2, current_index + 1) and not is_empty(current_row + 2, current_index + 1) and field[current_row + 2][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row + 2)))
        if is_present(current_row + 2, current_index - 1) and not is_empty(current_row + 2, current_index - 1) and field[current_row + 2][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row + 2)))
        if is_present(current_row + 1, current_index + 2) and not is_empty(current_row + 1, current_index + 2) and field[current_row + 1][current_index + 2] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 2] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index + 2) and not is_empty(current_row - 1, current_index + 2) and field[current_row - 1][current_index + 2] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 2] + str(8 - (current_row - 1)))
        if is_present(current_row + 1, current_index - 2) and not is_empty(current_row + 1, current_index - 2) and field[current_row + 1][current_index - 2] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 2] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index - 2) and not is_empty(current_row - 1, current_index - 2) and field[current_row - 1][current_index - 2] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 2] + str(8 - (current_row - 1)))
        if is_present(current_row - 2, current_index + 1) and not is_empty(current_row - 2, current_index + 1) and field[current_row - 2][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row - 2)))
        if is_present(current_row - 2, current_index - 1) and not is_empty(current_row - 2, current_index - 1) and field[current_row - 2][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row - 2)))
    if figure == black_knight:
        pass
    if figure == white_king:
        if is_present(current_row + 1, current_index) and not is_empty(current_row + 1, current_index) and field[current_row + 1][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index) and not is_empty(current_row - 1, current_index) and field[current_row - 1][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row - 1)))
        if is_present(current_row, current_index + 1) and not is_empty(current_row, current_index + 1) and field[current_row][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - current_row))
        if is_present(current_row, current_index - 1) and not is_empty(current_row, current_index - 1) and field[current_row][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - current_row))
        if is_present(current_row + 1, current_index + 1) and not is_empty(current_row + 1, current_index + 1) and field[current_row + 1][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row + 1)))
        if is_present(current_row + 1, current_index - 1) and not is_empty(current_row + 1, current_index - 1) and field[current_row + 1][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index + 1) and not is_empty(current_row - 1, current_index + 1) and field[current_row - 1][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row - 1)))
        if is_present(current_row - 1, current_index - 1) and not is_empty(current_row - 1, current_index - 1) and field[current_row - 1][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row - 1)))

    if figure == black_king:
        if is_present(current_row + 1, current_index) and not is_empty(current_row + 1, current_index) and not field[current_row + 1][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index) and not is_empty(current_row - 1, current_index) and not field[current_row - 1][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row - 1)))
        if is_present(current_row, current_index + 1) and not is_empty(current_row, current_index + 1) and not field[current_row][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - current_row))
        if is_present(current_row, current_index - 1) and not is_empty(current_row, current_index - 1) and not field[current_row][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - current_row))
        if is_present(current_row + 1, current_index + 1) and not is_empty(current_row + 1, current_index + 1) and not field[current_row + 1][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row + 1)))
        if is_present(current_row + 1, current_index - 1) and not is_empty(current_row + 1, current_index - 1) and not field[current_row + 1][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row + 1)))
        if is_present(current_row - 1, current_index + 1) and not is_empty(current_row - 1, current_index + 1) and not field[current_row - 1][current_index + 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index + 1] + str(8 - (current_row - 1)))
        if is_present(current_row - 1, current_index - 1) and not is_empty(current_row - 1, current_index - 1) and not field[current_row - 1][current_index - 1] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
            abilities.append(numbers_dictionary[current_index - 1] + str(8 - (current_row - 1)))

    if figure == black_queen:
        # возможность есть враво вверх
        for i in range(1, 7 - current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index + i) and not field[current_row - i][
                                                                            current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index + i) and field[current_row - i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

        # возможность ходить влево вверх
        for i in range(1, current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index - i) and not field[current_row - i][
                                                                            current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index - i) and field[current_row - i][
                current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

        # возможность ходить вправо вниз
        for i in range(1, 7 - current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index + i) and not field[current_row + i][
                                                                            current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index + i) and field[current_row + i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

        # возможность ходить вниз влево
        for i in range(1, current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index - i) and not field[current_row + i][
                                                                            current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index - i) and not field[current_row + i][
                                                                              current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break
        # обзор фигуры которую можно съесть по вертикали
        for i in range(current_row + 1, 8):
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_row - 1, -1, -1):
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index + 1, 8):
            if not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index - 1, -1, -1):
            if not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break

    if figure == white_queen:
        # возможность есть враво вверх
        for i in range(1, 7 - current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index + i) and field[current_row - i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index + i) and not field[current_row - i][
                                                                              current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

        # возможность ходить влево вверх
        for i in range(1, current_index + 1):
            if current_row - i < 0:
                break
            if not is_empty(current_row - i, current_index - i) and field[current_row - i][
                current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row - i)))
                break
            elif not is_empty(current_row - i, current_index - i) and not field[current_row - i][
                                                                              current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

        # возможность ходить вправо вниз
        for i in range(1, 7 - current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index + i) and field[current_row + i][
                current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index + i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index + i) and not field[current_row + i][
                                                                              current_index + i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break

        # возможность ходить вниз влево
        for i in range(1, current_index + 1):
            if current_row + i > 7:
                break
            if not is_empty(current_row + i, current_index - i) and field[current_row + i][
                current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index - i] + str(8 - (current_row + i)))
                break
            elif not is_empty(current_row + i, current_index - i) and not field[current_row + i][
                                                                              current_index - i] in "♔ ♕ ♖ ♗ ♘ ♙".split(
                " "):
                break
        # обзор фигуры которую можно съесть по вертикали
        for i in range(current_row + 1, 8):
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_row - 1, -1, -1):
            if not is_empty(i, current_index) and field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[current_index] + str(8 - i))
                break
            if not is_empty(i, current_index) and not field[i][current_index] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index + 1, 8):
            if not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
        for i in range(current_index - 1, -1, -1):
            if not is_empty(current_row, i) and field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                abilities.append(numbers_dictionary[i] + str(8 - current_row))
                break
            elif not is_empty(current_row, i) and not field[current_row][i] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                break
    return abilities
