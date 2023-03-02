def print_board(board):
    for row in reversed(board):
        print(" ".join(row))
    print()


def initialize_board(num_rows, num_cols):
    return [['-' for x in range(num_cols)] for y in range(num_rows)]


def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row
    return -1


def check_if_winner(board, col, row, chip_type):
    # Check horizontally
    count = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertically
    count = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False



def main():
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))

    board = initialize_board(num_rows, num_cols)

    print_board(board)

    print("Player 1: x")
    print("Player 2: o")

    player = 1
    while True:
        col = int(input(f"Player {player}: Which column would you like to choose? "))
        row = insert_chip(board, col, 'x' if player == 1 else 'o')

        if row == -1:
            print("That column is already full. Please choose another column.")
            continue

        print_board(board)

        if check_if_winner(board, col, row, 'x' if player == 1 else 'o'):
            print(f"Player {player} won the game!")
            break

        if not any('-' in row for row in board):
            print("Draw. Nobody wins.")
            break

        player = 3 - player  # Switch players (player 1 -> player 2, and vice versa)

if __name__ == '__main__':
    main()