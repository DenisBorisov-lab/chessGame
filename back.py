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
white_queen = '♚'
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


def able_to_go(figure: str, start: str):
    abilities = []
    current_index = letter_dictionary[start[0:1]]
    current_row = 8 - int(start[1:2])

    if figure == black_pawn:
        if current_row == 1 and is_empty(current_row + 1, current_index) and is_empty(current_row + 2, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row + 2)))
        if is_empty(current_row + 1, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row + 1)))
        return abilities

    elif figure == white_pawn:
        if current_row == 6 and is_empty(current_row - 1, current_index) and is_empty(current_row - 2, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row - 2)))
        if is_empty(current_row - 1, current_index):
            abilities.append(numbers_dictionary[current_index] + str(8 - (current_row - 1)))
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

    return abilities
