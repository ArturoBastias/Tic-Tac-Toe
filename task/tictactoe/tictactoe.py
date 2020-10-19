
inp = list("_" * 9)
field = f"""---------
| {inp[0]} {inp[1]} {inp[2]} |
| {inp[3]} {inp[4]} {inp[5]} |
| {inp[6]} {inp[7]} {inp[8]} |
---------"""
print(field)
# print(s)
coordinates = [(i, j) for j in range(3, 0, -1) for i in range(1, 4)]
s = False
while not s:
    # Make move.
    ok = False
    while not ok:
        nxt_move = input("Enter the coordinates: ")
        moves = nxt_move.split()
        if not (moves[0].isdigit() and moves[1].isdigit()):
            print("You should enter numbers!")
        else:
            num1 = int(moves[0])
            num2 = int(moves[1])
            if not ((0 < num1 < 4) and (0 < num2 < 4)):
                print("Coordinates should be from 1 to 3!")
            else:
                move_in_field = coordinates.index((num1, num2))
                if inp[move_in_field] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    if inp.count("_") % 2 != 0:
                        inp[move_in_field] = "X"
                    else:
                        inp[move_in_field] = "O"
                    ok = True
    # Print updated field.
    field = (f"---------\n"
             f"| {inp[0]} {inp[1]} {inp[2]} |\n"
             f"| {inp[3]} {inp[4]} {inp[5]} |\n"
             f"| {inp[6]} {inp[7]} {inp[8]} |\n"
             f"---------")
    print(field)

    # Check if there are three consecutive adjacent symbols.
    three_X_in_row = False
    three_O_in_row = False
    for i in range(3):
        # Check columns.
        if inp[i] == inp[i + 3] == inp[i + 6]:
            if inp[i] == "X":
                three_X_in_row = True
            elif inp[i] == "O":
                three_O_in_row = True
        # Check rows.
        j = i * 3
        if inp[j] == inp[j + 1] == inp[j + 2]:
            if inp[j] == "X":
                three_X_in_row = True
            elif inp[j] == "O":
                three_O_in_row = True
    # Check diagonals.
    if (inp[0] == inp[4] == inp[8]) or \
            (inp[2] == inp[4] == inp[6]):
        if inp[4] == "X":
            three_X_in_row = True
        elif inp[4] == "O":
            three_O_in_row = True

    # Check if the game is finished and who won.
    if not (three_X_in_row or three_O_in_row) and not ("_" in inp):
        s = "Draw"
    elif three_X_in_row:
        s = "X wins"
    elif three_O_in_row:
        s = "O wins"

    # Check if the game is impossible
    if (three_X_in_row and three_O_in_row) or \
            abs(inp.count("X") - inp.count("O")) > 1:
        s = "Impossible"
print(s)
