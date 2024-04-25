from functions import check_win, board_print, get_move

## declares the board and all the rows
board =[[0, 0, 0],
    [0, 0, 0],
    [0 ,0 ,0]]
first_row = board[0]
middle_row = board[1]
bottom_row = board[2]


## player chooses whether to play with another person or a computer
"""player_or_comp = input("Type the number 1 if you would like to play with another person or 2 if you would like to play "
                       "with a computer\n")
try:
    if player_or_comp == 1:"""

playing = True

move = 1
while playing == True:
    column_dict = {"a": 0, "b": 1, "c": 2}
    board_print(board)

    if move%2 != 0:
        if get_move(1, board) == 1:
            move += 1
    else:
        if get_move(2, board) == 1:
            move += 1

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