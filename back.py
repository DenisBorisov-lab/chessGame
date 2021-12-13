def generate_field():
    field = [[0 for j in range(8)] for i in range(8)]
    white_king = '♔'
    white_queen = '♕'
    white_rook = '♖'
    white_bishop = '♗'
    white_knight = '♘'
    white_pawn = '♙'
    black_king = '♚'
    black_queen = '♚'
    black_rook = '♜'
    black_bishop = '♝'
    black_knight = '♞'
    black_pawn = '♟'
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
