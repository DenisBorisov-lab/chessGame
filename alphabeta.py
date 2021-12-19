import back
import random as movement
black_weights = {"♔": 900, "♕": 90, "♖": 50, "♗": 30, "♘": 30, "♙": 10}
white_weights = {"♚": 900, "♛": 90, "♜": 50, "♝": 30, "♞": 30, "♟": 10}
numbers_dictionary = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
blackScore = 1290
whiteScore = 1290
def evaluate_board(field):
    total = 0
    for y in range(len(field)):
        for x in range(len(field[y])):
            total += (x + y)
    return total
def minimax(field, depth: int, alpha, beta, is_maximising_player: bool):
    moves = get_moves(field)
    m = movement.choice(moves)
    if depth == 0:
        return m
    if is_maximising_player:
        best_move = -9999
        for move in moves:
            best_move = max(best_move, minimax(field, depth - 1, alpha, beta, not is_maximising_player))
            alpha = max(alpha, best_move)
            if beta <= alpha:
                return move
        return best_move
    else:
        best_move = 9999
        for move in moves:
            best_move = min(best_move, minimax(field, depth - 1, alpha, beta, not is_maximising_player))
            alpha = min(alpha, best_move)
            if beta <= alpha:
                return move

        return best_move
def get_moves(field):
    app = []
    for i in range(len(back.field)):
        for j in range(len(back.field[i])):
            if field[i][j] != 0 and field[i][j] in "♔ ♕ ♖ ♗ ♘ ♙".split(" "):
                for k in range(len(back.able_to_go(str(field[i][j]), numbers_dictionary[j] + str(8 - i)))):
                    app.append(numbers_dictionary[j] + str(8 - i) + back.able_to_go(str(field[i][j]), numbers_dictionary[j] + str(8 - i))[k])
                for k in range(len(back.able_to_eat(str(field[i][j]), numbers_dictionary[j] + str(8 - i)))):
                    app.append(numbers_dictionary[j] + str(8 - i) + back.able_to_eat(str(field[i][j]), numbers_dictionary[j] + str(8 - i))[k])
    return app