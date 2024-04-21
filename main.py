

"""
      a   b   c
     --- --- ---
  1 |   |   |   |
     --- --- ---
  2 |   |   |   |
     --- --- ---
  3 |   |   |   |
     --- --- ---
"""


board =[[0, 0, 0],
    [0, 0, 0],
    [0 ,0 ,0]]
first_row = board[0]
middle_row = board[1]
bottom_row = board[2]

def board_print(board):
    print("    a   b   c")
    for x in range(3):
        horizontal = " ---"
        vert = f"| {board[x][0]} "
        vert2 = f"| {board[x][1]} "
        vert3 = f"| {board[x][2]} "
        vertend = "|   "
        print("  " + horizontal * 3)
        print(f"{x + 1} " + vert + vert2 + vert3 + vertend)
    print("  " + horizontal * 3)
def check_win(board):
    first_row = board[0]
    middle_row = board[1]
    bottom_row = board[2]

    col_1 = []
    col_1.append(first_row[0])
    col_1.append(middle_row[0])
    col_1.append(bottom_row[0])
    col_1 = set(col_1)

    col_2 = []
    col_2.append(first_row[1])
    col_2.append(middle_row[1])
    col_2.append(bottom_row[1])
    col_2 = set(col_2)

    col_3 = []
    col_3.append(first_row[2])
    col_3.append(middle_row[2])
    col_3.append(bottom_row[2])
    col_3 = set(col_3)

    diag_1 = []
    diag_1.append(first_row[0])
    diag_1.append(middle_row[1])
    diag_1.append(bottom_row[2])
    diag_1 = set(diag_1)

    diag_2 = []
    diag_2.append(first_row[2])
    diag_2.append(middle_row[1])
    diag_2.append(bottom_row[0])
    diag_2 = set(diag_2)

    first_row = set(first_row)
    middle_row = set(middle_row)
    bottom_row = set(bottom_row)

    if first_row == {"x"} or middle_row == {"x"} or col_1 == {"x"} or col_2 == {"x"} or col_3 == {"x"} or diag_1 == {
        "x"} or diag_2 == {"x"} or bottom_row == {"x"}:
        return 1
    elif first_row == {"o"} or middle_row == {"o"} or col_1 == {"o"} or col_2 == {"o"} or col_3 == {"o"} or diag_1 == {
        "o"} or diag_2 == {"o"} or bottom_row == {"x"}:
        return 2
    elif board[0][0] != 0 and board[0][1] != 0 and board[0][2] != 0 and board[1][0] != 0 and board[1][1] != 0 and board[1][2]\
        and board[2][0] != 0 and board[2][1] != 0 and board[2][2]:
        return 3

playing = True

move = 1
while playing == True:
    column_dict = {"a": 0, "b": 1, "c": 2}
    board_print(board)

    if move%2 != 0:
        p1_input = input("Player 1 make your move")
        if p1_input.strip()[0] == "a" or p1_input.strip()[0] == "b" or p1_input.strip()[0] == "c":
            p1_column_letter = p1_input.strip()[0]
            p1_column = column_dict[p1_column_letter]
            p1_row = p1_input.strip()[1]
            board_to_change = board[int(p1_row) - 1][int(p1_column)]
            if board_to_change == 0:
                move += 1
                board[int(p1_row) - 1][int(p1_column)] = "x"
            elif board_to_change != 0:
                print("This spot is already taken, try again")
        else:
            print("That column does not exist, try again")
    else:
        p2_input = input("Player 2 make your move")
        if p2_input.strip()[0] == "a" or p2_input.strip()[0] == "b" or p2_input.strip()[0] == "c":
            p2_column_letter = p2_input.strip()[0]
            p2_column = column_dict[p2_column_letter]
            p2_row = p2_input.strip()[1]
            board_to_change = board[int(p2_row) - 1][int(p2_column)]
            if board_to_change == 0:
                move += 1
                board[int(p2_row) - 1][int(p2_column)] = "o"
            elif board_to_change != 0:
                print("this spot is already taken, try again")
        else:
            print("That column does not exist, try again")
    winner = check_win(board)
    if winner == 1:
        board_print(board)
        print("Player 1 wins")
        playing = False
    elif winner == 2:
        board_print(board)
        print("Player 2 wins")
        playing = False
    elif winner == 3:
        board_print(board)
        print("Tie")
        playing = False