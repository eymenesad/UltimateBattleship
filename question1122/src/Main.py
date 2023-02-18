
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    # taking a list for player 1
    my_list = [[['-' for i in range(10)] for j in range(10)], [['-' for i in range(10)] for j in range(10)]]
    second_ship = []
    m = True
    flag = 0
    elemInside = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    ships_in_my_list = []
    while m:
        if elemInside == []:
            print_3d_list(my_list)
            # making a loop for confirmation
            while True:
                print_confirm_placement()
                a = input()
                if a == "y" or a == "Y":
                    m = False
                    break
                elif a == "n" or a == "N":
                    elemInside = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
                    my_list = [[['-' for i in range(10)] for j in range(10)], [['-' for i in range(10)] for j in range(10)]]
                    flag = 0
                    second_ship = []
                    break
                else:
                    continue
        if m == False:
            break
        print_3d_list(my_list)
        print_ships_to_be_placed()

        for i in elemInside:
            print_single_element(i)
        print_empty_line()
        print_player_turn_to_place(1)
        print_to_place_ships()
        try:
            place = input()
        except:
            break
        # checking for errors
        if len(place.split()) < 4:
            print_incorrect_input_format()
            continue
        try:
            place.split()[1] = int(place.split()[1])
            place.split()[2] = int(place.split()[2])
        except:
            print_incorrect_input_format()
            continue
        ships_lower = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
        shipName = place.split(" ")[0]
        column = int(place.split(" ")[1])
        column1 = column
        column2 = column
        row = int(place.split(" ")[2])
        row1 = row
        row2 = row
        vert_or_hor = place.split(" ")[3]
        if place.split(" ")[0].lower() not in ships_lower:
            print_incorrect_ship_name()
            continue
        if int(place.split(" ")[1]) < 0 and int(place.split(" ")[1]) > 10:
            print_incorrect_coordinates()
            continue
        if int(place.split(" ")[2]) < 0 and int(place.split(" ")[2]) > 10:
            print_incorrect_coordinates()
            continue
        if place.split(" ")[3].lower() not in ["h", "v"]:
            print_incorrect_orientation()
            continue
        # assigning ships to integers
        ship_length = 0
        if place.split(" ")[0].lower() == ships_lower[0]:
            ship_length = 5
        if place.split(" ")[0].lower() == ships_lower[1]:
            ship_length = 4
        if place.split(" ")[0].lower() == ships_lower[2]:
            ship_length = 3
        if place.split(" ")[0].lower() == ships_lower[3]:
            ship_length = 3
        if place.split(" ")[0].lower() == ships_lower[4]:
            ship_length = 2
        # placing ships for horizontal case
        if vert_or_hor == "h":
            if ship_length + column > 11:
                print_ship_cannot_be_placed_outside(shipName.title())
            else:
                first_ship = []
                # checking if the coordinate occupied
                for b in range(1, ship_length+1):
                    first_ship.append((int(column1), int(row)))
                    column1 += 1
                for i in second_ship:
                    if i in first_ship:
                        print_ship_cannot_be_placed_occupied(shipName.title())
                        flag = 1
                        break
                if flag == 1 :
                    continue
                for b in range(1, ship_length+1):
                    second_ship.append((int(column2), int(row)))
                    column2 += 1
                for k in range(ship_length):
                    my_list[0][int(row)-1][int(column)-1] = "#"
                    column += 1
                    ships_in_my_list.append((column - 1, row - 1))
                elemInside.remove(shipName.title())
        # placing ships for vertical case
        if vert_or_hor == "v":
            if ship_length + row > 11:
                print_ship_cannot_be_placed_outside(shipName.title())
            else:
                first_ship = []
                # checking if the coordinate occupied
                for b in range(1, ship_length + 1):
                    first_ship.append((int(column), int(row1)))
                    row1 += 1
                for i in second_ship:
                    if i in first_ship:
                        print_ship_cannot_be_placed_occupied(shipName.title())
                        flag = 1
                        break
                if flag == 1:
                    continue
                for b in range(1, ship_length + 1):
                    second_ship.append((int(column), int(row2)))
                    row2 += 1
                for k in range(ship_length):
                    my_list[0][int(row) - 1][int(column) - 1] = "#"
                    row += 1
                    ships_in_my_list.append((column-1, row-1))
                elemInside.remove(shipName.title())
    # taking a list for player 2
    my_list_2 = [[['-' for i in range(10)] for j in range(10)], [['-' for i in range(10)] for j in range(10)]]
    second_ship_2 = []
    ma = True
    flag_2 = 0
    elemInside_2 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    ships_in_my_list2 = []
    while ma:
        if elemInside_2 == []:
            print_3d_list(my_list_2)
            while True:
                # making a loop for confirmation
                print_confirm_placement()
                a = input()
                if a == "y" or a == "Y":
                    ma = False
                    break
                elif a == "n" or a == "N":
                    elemInside_2 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
                    my_list_2 = [[['-' for i in range(10)] for j in range(10)],
                               [['-' for i in range(10)] for j in range(10)]]
                    flag_2 = 0
                    second_ship_2 = []
                    break
                else:
                    continue
        if ma == False:
            break
        print_3d_list(my_list_2)
        print_ships_to_be_placed()

        for i in elemInside_2:
            print_single_element(i)
        print_empty_line()
        print_player_turn_to_place(2)
        print_to_place_ships()
        # checking for errors
        try:
            place = input()
        except:
            break
        if len(place.split()) < 4:
            print_incorrect_input_format()
            continue
        try:
            place.split()[1] = int(place.split()[1])
            place.split()[2] = int(place.split()[2])
        except:
            print_incorrect_input_format()
            continue
        ships_lower = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
        shipName = place.split(" ")[0]
        column = int(place.split(" ")[1])
        column1 = column
        column2 = column
        row = int(place.split(" ")[2])
        row1 = row
        row2 = row
        vert_or_hor = place.split(" ")[3]

        if place.split(" ")[0].lower() not in ships_lower:
            print_incorrect_ship_name()
            continue
        if int(place.split(" ")[1]) < 0 and int(place.split(" ")[1]) > 10:
            print_incorrect_coordinates()
            continue
        if int(place.split(" ")[2]) < 0 and int(place.split(" ")[2]) > 10:
            print_incorrect_coordinates()
            continue
        if place.split(" ")[3].lower() not in ["h", "v"]:
            print_incorrect_orientation()
            continue
        # assigning ships to integers
        ship_length = 0
        if place.split(" ")[0].lower() == ships_lower[0]:
            ship_length = 5
        if place.split(" ")[0].lower() == ships_lower[1]:
            ship_length = 4
        if place.split(" ")[0].lower() == ships_lower[2]:
            ship_length = 3
        if place.split(" ")[0].lower() == ships_lower[3]:
            ship_length = 3
        if place.split(" ")[0].lower() == ships_lower[4]:
            ship_length = 2
        # placing ships for horizontal case
        if vert_or_hor == "h":
            if ship_length + column > 11:
                print_ship_cannot_be_placed_outside(shipName.title())
            else:
                first_ship = []
                # checking if the coordinate occupied
                for b in range(1, ship_length + 1):
                    first_ship.append((int(column1), int(row)))
                    column1 += 1
                for i in second_ship_2:
                    if i in first_ship:
                        print_ship_cannot_be_placed_occupied(shipName.title())
                        flag_2 = 1
                        break
                if flag_2 == 1:
                    continue
                for b in range(1, ship_length + 1):
                    second_ship_2.append((int(column2), int(row)))
                    column2 += 1
                for k in range(ship_length):
                    my_list_2[1][int(row)- 1][int(column) - 1] = "#"
                    column += 1
                    ships_in_my_list2.append((column-1, row-1))
                elemInside_2.remove(shipName.title())
        # placing ships for vertical case
        if vert_or_hor == "v":
            if ship_length + row > 11:
                print_ship_cannot_be_placed_outside(shipName.title())
            else:
                # checking if the coordinate occupied
                first_ship = []
                for b in range(1, ship_length + 1):
                    first_ship.append((int(column), int(row1)))
                    row1 += 1
                for i in second_ship_2:
                    if i in first_ship:
                        print_ship_cannot_be_placed_occupied(shipName.title())
                        flag_2 = 1
                        break
                if flag_2 == 1:
                    continue
                for b in range(1, ship_length + 1):
                    second_ship_2.append((int(column), int(row2)))
                    row2 += 1
                for k in range(ship_length):
                    my_list_2[1][int(row) - 1][int(column) - 1] = "#"
                    row += 1
                    ships_in_my_list2.append((column, row))
                elemInside_2.remove(shipName.title())

    k = 1
    flag = 0
    total_ship_character_1 = 17
    total_ship_character_2 = 17
    print_3d_list(my_list)
    while total_ship_character_1 > 0  and total_ship_character_2 > 0:
        # making a loop for hit miss situation
        if k == 1 :    # a loop for player 1
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            # taking errors
            try:
                m = input()
            except:
                break
            if len(m) < 2:
                print_incorrect_input_format()
                continue
            if m.split()[0].isdecimal() == False or m.split()[1].isdecimal() == False:
                print_incorrect_input_format()
                continue
            try:
                m.split()[0] = int(m.split()[0])
                m.split()[1] = int(m.split()[1])
            except:
                print_incorrect_input_format()
                continue
            row_for_strike1 = m.split()[0]
            column_for_strike1 = m.split()[1]
            # hit situaiton
            if my_list_2[1][int(column_for_strike1)-1][int(row_for_strike1)-1] == "#":
                my_list[1][int(column_for_strike1)-1][int(row_for_strike1)-1] = "!"
                my_list_2[1][int(column_for_strike1)-1][int(row_for_strike1)-1] = "!"
                print_hit()
                total_ship_character_1 -= 1
                k = 1
                print_3d_list(my_list)
            # miss situaiton
            elif my_list_2[1][int(column_for_strike1)-1][int(row_for_strike1)-1] == "-":
                my_list[1][int(column_for_strike1)-1][int(row_for_strike1)-1] = "O"
                my_list_2[1][int(column_for_strike1)-1][int(row_for_strike1)-1] = "O"
                print_miss()
                k = 2
                # making a loop for proceeding to next player
                correction_t_f = True
                while correction_t_f:
                    print_type_done_to_yield(k)
                    correction = input()
                    if correction.lower() == "done":
                        correction_t_f = False
                    else:
                        correction_t_f = True
                print_3d_list(my_list_2)
            else :
                print_tile_already_struck()
                k = 2
                print_3d_list(my_list)
                continue
        if k == 2 :   # a loop for player 1
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            m = input()
            if len(m) < 2:
                print_incorrect_input_format()
                continue
            # taking errors
            try:
                m.split()[0] = int(m.split()[0])
                m.split()[1] = int(m.split()[1])
            except:
                print_incorrect_input_format()
                continue
            row_for_strike2 = m.split()[0]
            column_for_strike2 = m.split()[1]
            # hit situaiton
            if my_list[0][int(column_for_strike2)-1][int(row_for_strike2)-1] == "#":
                my_list[0][int(column_for_strike2)-1][int(row_for_strike2)-1] = "!"
                my_list_2[0][int(column_for_strike2)-1][int(row_for_strike2)-1] = "!"
                print_hit()
                total_ship_character_2 -= 1
                k = 2
                print_3d_list(my_list_2)
            # miss situaiton
            elif my_list[0][int(column_for_strike2)-1][int(row_for_strike2)-1] == "-":
                my_list[0][int(column_for_strike2)-1][int(row_for_strike2)-1] = "O"
                my_list_2[0][int(column_for_strike2)-1][int(row_for_strike2)-1] = "O"
                print_miss()
                k = 1
                # making a loop for proceeding to next player
                correction_t_f = True
                while correction_t_f:
                    print_type_done_to_yield(k)
                    correction = input()
                    if correction.lower() == "done":
                        correction_t_f = False
                    else:
                        correction_t_f = True
                print_3d_list(my_list)

            else:
                print_tile_already_struck()
                print_3d_list(my_list_2)
    # printing the winner
    if total_ship_character_1 == 0:
        print_player_won(1)
        print_thanks_for_playing()
    elif total_ship_character_2 == 0:
        print_player_won(2)
        print_thanks_for_playing()
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

