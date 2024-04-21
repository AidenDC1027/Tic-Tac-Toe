
## This was used to play the game before i made a function for it

"""
p1_input = input("Player 1 make your move")
try:
    if p1_input.strip()[0] == "a" or p1_input.strip()[0] == "b" or p1_input.strip()[0] == "c":
        if int(p1_input.strip()[1]) <= 3:
            p1_column_letter = p1_input.strip()[0]
            p1_column = column_dict[p1_column_letter]
            p1_row = p1_input.strip()[1]
            board_to_change = board[int(p1_row) - 1][int(p1_column)]
            if board_to_change == 0:
                move += 1
                board[int(p1_row) - 1][int(p1_column)] = "x"
            else:
                print("This spot is already taken, try again")
        else:
            print("That row does not exist, try again")
    else:
        print("That column does not exist, try again")
except IndexError:
    print("You did something wrong, try again")
else:
p2_input = input("Player 2 make your move")
try:
    if p2_input.strip()[0] == "a" or p2_input.strip()[0] == "b" or p2_input.strip()[0] == "c":
        p2_row = int(p2_input.strip()[1])
        if p2_row <= 3:
            p2_column_letter = p2_input.strip()[0]
            p2_column = column_dict[p2_column_letter]
            board_to_change = board[p2_row - 1][int(p2_column)]
            if board_to_change == 0:
                move += 1
                board[int(p2_row) - 1][int(p2_column)] = "o"
            else:
                print("this spot is already taken, try again")
        else:
            print("That row does not exist, try again")
    else:
        print("That column does not exist, try again")
except IndexError:
    print("You did something wrong, try again")
"""

## i used this to design the board

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
