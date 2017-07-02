#board for each user
#vs "AI"
#option to place ships
#inputs of attack areas
#end game if all ships are hit for either side
#---------------------------------------------

#boards for both players
#player 2 board is the player's view of the opponents board, showing only what the player knows

#Class to setup the viewable boards for the player
class Playable_Boards(object):
    def __init__(self):
        self.board = [["  ","A","B","C","D","E","F","G","H","I","J"],
                      [" 1","-","-","-","-","-","-","-","-","-","-"],
                      [" 2","-","-","-","-","-","-","-","-","-","-"],
                      [" 3","-","-","-","-","-","-","-","-","-","-"],
                      [" 4","-","-","-","-","-","-","-","-","-","-"],
                      [" 5","-","-","-","-","-","-","-","-","-","-"],
                      [" 6","-","-","-","-","-","-","-","-","-","-"],
                      [" 7","-","-","-","-","-","-","-","-","-","-"],
                      [" 8","-","-","-","-","-","-","-","-","-","-"],
                      [" 9","-","-","-","-","-","-","-","-","-","-"],
                      ["10","-","-","-","-","-","-","-","-","-","-"]]
        
    def print_board(self, board):
        for element in self.board:
            print (" ".join(element))
            
#class to setup the boards that track ship positions
class Board_To_Track_Game(object):
    def __init__(self):
        self.tracking_board = []
        for x in range(0,12):
            row = []
            self.tracking_board.append(row)
            for y in range(0,12):
                column = []
                row.append(column)
            
def print_boards(playersb, oppsb):
    split = " "
    print (split)
    print ("A, B, S, C, P: ship | 0: Missed Shot | X: Successful Hit")
    print ("---------------------------------------------------------")
    print (split)
    print ("Opponents Board")
    print (split)
    oppsb.print_board(oppsb.board)
    print ("---------------------------------------------------------")
    print ("Your Board")
    print (split)
    playersb.print_board(playersb.board)
    print (split)

#Function to check the inputs are valid (on the grid)
def input_check(x, y):
    if x == "a" or x == "b" or x == "c" or x == "d" or x == "e" or x == "f" or x == "g" or x == "h" or x == "i" or x == "j":
        pass
    elif x != "a" or x != "b" or x != "c" or x != "d" or x != "e" or x != "f" or x != "g" or x != "h" or x != "i" or x != "j":
        print ("The column entered is not in the range A - J!")
        input("Press enter to continue...")
        good_inputs = False
        return good_inputs
    if 0 > y or 11 < y:
        print ("The row entered is not in the range 1 - 10!")
        input("Press enter to continue...")
        good_inputs = False
        return good_inputs
    else:
        good_inputs = True
        return good_inputs

#function to change the lettercoordinate to a number so that it can be used for list referencing
def convert_lettercoord_to_num(numcoord):
    translator = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
    numcoord = translator[numcoord]
    return numcoord
            
#Dictionary for the ships
ships = {"aircraft carrier": 5, "battleship": 4, "submarine": 3, "cruiser": 3, "patrol boat": 2}

#Class that stores all of the functions for entering the player's ships
        
def intro():
    print (" ")
    print ("You must select where you want to place your boats, there are 5 to place, here is all of them and the spaces they will take up: ")
    print ("Aircraft carrier = 5")
    print ("Battleship = 4")
    print ("Submarine = 3")
    print ("Cruiser = 3")
    print ("Patrol boat = 2")
    print (" ")
    
    #First coordinate for ship chosen
def ship_coordinate(ship_type):
    print ("Now select the coordinate of one end of the %s you want to place." % (ship_type))
    print ("Remember, the %s is %s sections long on the grid!" % (ship_type, ships[ship_type]))
    input("Press enter to continue")
    #code to get a legitimate coordinate
    check = False
    while check == False:
        x = input("Enter the X coordinate at which you want to place the first section of the %s (A - J): " % (ship_type)).lower()
        y = int(input("Enter the y coordiante at which you want to place the first section of the %s (1 - 10): "% (ship_type)))
        check = input_check(x, y)
        if check == True:
            break
    x = convert_lettercoord_to_num(x)
    #code to get the orientation of the ship
    print ("Enter what orientation you want the %s to be from the given coordinate." % (ship_type))
    orientation = input("Either vertically or horizontally (v or h): ").lower()
    orientation_direction = input("Now enter the direction along this axis (+ or -): ")
    orientation = "%s%s" % (orientation, orientation_direction)
    if orientation == "v+" or orientation == "v-" or orientation == "h+" or orientation == "h-":
        pass
    elif orientation != "v+" or orientation != "v-" or orientation != "h+" or orientation != "h-":
        print ("Wht you entered was not valid!")
        print ("Enter what orientation you want the %s to be from the given coordinate." % (ship_type))
        orientation = input("Either vertically or horizontally (v or h): ").lower()
        orientation_direction = input("Now enter the direction along this axis (+ or -): ")
        orientation = "%s%s" % (orientation, orientation_direction)
    return (x, y, orientation)


def check_ship_can_be_placed(x, y, orientation, ship_type):
    valid = False
    for length in range(ships[ship_type]):
        if orientation == "v+":
            if y + ships[ship_type] > 10 or players_tracking_board.tracking_board[y+length][x] == 1:
                print ("There is not enough space for a %s to be placed there!" % (ship_type))
                input("Press enter to continue...")
                valid = False
                return valid
        elif orientation == "v-":
            if y - ships[ship_type] < 1 or players_tracking_board.tracking_board[y-length][x] == 1:
                print ("There is not enough space for a %s to be placed there!" % (ship_type))
                input("Press enter to continue...")
                valid = False
                return valid
        elif orientation == "h+":
            if x + ships[ship_type] > 10 or players_tracking_board.tracking_board[y][x+length] == 1:
                print ("There is not enough space for a %s to be placed there!" % (ship_type))
                input("Press enter to continue...")
                valid = False
                return valid
        elif orientation == "h-" or players_tracking_board.tracking_board[y][x-length] == 1:
            if x - ships[ship_type] < 1:
                print ("There is not enough space for a %s to be placed there!" % (ship_type))
                input("Press enter to continue...")
                valid = False
                return valid
        else:
            valid = True
            return valid

def place_ship(x, y, orientation, ship_type, player):
    identifier = ship_type[0].upper()
    #place players ships
    if player == "player":
        players_board.board[y][x] = identifier
        if orientation == "v+":
            for length in range(ships[ship_type]):
                players_board.board[y+length][x] = identifier
                players_tracking_board.tracking_board[y+length][x] = 1
        elif orientation == "v-":
            for length in range(ships[ship_type]):
                players_board.board[y-length][x] = identifier
                players_tracking_board.tracking_board[y-length][x] = 1
        elif orientation == "h+":
            for length in range(ships[ship_type]):
                players_board.board[y][x+length] = identifier
                players_tracking_board.tracking_board[y][x+length] = 1
        elif orientation == "h-":
            for length in range(ships[ship_type]):
                players_board.board[y][x-length] = identifier
                players_tracking_board.tracking_board[y][x-length] = 1
    #place AI ships
    elif player == "AI":
        opponents_tracking_board.tracking_board[y][x] = identifier
        if orientation == "v+":
            for length in range(ships[ship_type]):
                opponents_tracking_board.tracking_board[y+length][x] = 1
        elif orientation == "v-":
            for length in range(ships[ship_type]):
                opponents_tracking_board.tracking_board[y-length][x] = 1
        elif orientation == "h+":
            for length in range(ships[ship_type]):
                opponents_tracking_board.tracking_board[y][x+length] = 1
        elif orientation == "h-":
            for length in range(ships[ship_type]):
                opponents_tracking_board.tracking_board[y][x-length] = 1
            
def place_users_ships():
    player = "player"
    #run the intro code
    intro()
    #Patrol boat insertion
    ship_type = "patrol boat"
    x, y, orientation = ship_coordinate(ship_type)
    can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    while can_be_placed == False:
        x, y, orientation = ship_coordinate(ship_type)
        can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    place_ship(x, y, orientation, ship_type, player)
    print_boards(players_board, opponents_board)

    #cruiser boat insertion
    ship_type = "cruiser"
    x, y, orientation = ship_coordinate(ship_type)
    can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    while can_be_placed == False:
        x, y, orientation = ship_coordinate(ship_type)
        can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    place_ship(x, y, orientation, ship_type, player)
    print_boards(players_board, opponents_board)

    #submarine insertion
    ship_type = "submarine"
    x, y, orientation = ship_coordinate(ship_type)
    can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    while can_be_placed == False:
        x, y, orientation = ship_coordinate(ship_type)
        can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    place_ship(x, y, orientation, ship_type, player)
    print_boards(players_board, opponents_board)

    #battleship insertion
    ship_type = "battleship"
    x, y, orientation = ship_coordinate(ship_type)
    can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    while can_be_placed == False:
        x, y, orientation = ship_coordinate(ship_type)
        can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    place_ship(x, y, orientation, ship_type, player)
    print_boards(players_board, opponents_board)

    #aircraft carrier insertion
    ship_type = "aircraft carrier"
    x, y, orientation = ship_coordinate(ship_type)
    can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    while can_be_placed == False:
        x, y, orientation = ship_coordinate(ship_type)
        can_be_placed = check_ship_can_be_placed(x, y, orientation, ship_type)
    place_ship(x, y, orientation, ship_type, player)
    print_boards(players_board, opponents_board)
    
def generate_random_coords():
    from random import randrange
    x = randrange(1, 11)
    y = randrange(1, 11)
    direction = {1: "v+", 2: "v-", 3: "h+", 4: "h-"}
    orientation = direction[randrange(1, 5)]
    return (x, y, orientation)
        
def check_AI_coord_valid(x, y, orientation, ship_type):
    for length in range(ships[ship_type]):
        if orientation == "v+":
            if y + ships[ship_type] > 10 or opponents_tracking_board.tracking_board[y+length][x] == 1  :
                valid = False
                return valid
        elif orientation == "v-":
            if y - ships[ship_type] < 1 or opponents_tracking_board.tracking_board[y-length][x] == 1:
                valid = False
                return valid
        elif orientation == "h+":
            if x + ships[ship_type] > 10 or opponents_tracking_board.tracking_board[y][x+length] == 1:
                valid = False
                return valid
        elif orientation == "h-":
            if x - ships[ship_type] < 1 or opponents_tracking_board.tracking_board[y][x-length] == 1:
                valid = False
                return valid
        else:
            valid = True
            return valid
    
def place_AIs_ships():
    #function to place the AI's boats
    player = "AI"
    #place their patrol boat
    ship_type = "patrol boat"
    valid = False
    while valid == False:
        x, y, orientation = generate_random_coords()
        valid = check_AI_coord_valid(x, y, orientation, ship_type)
        if valid == True:
            break
    place_ship(x, y, orientation, ship_type, player)
    #place cruiser
    ship_type = "cruiser"
    valid = False
    while valid == False:
        x, y, orientation = generate_random_coords()
        valid = check_AI_coord_valid(x, y, orientation, ship_type)
        if valid == True:
            break
    place_ship(x, y, orientation, ship_type, player)
    #place submarine
    ship_type = "submarine"
    valid = False
    while valid == False:
        x, y, orientation = generate_random_coords()
        valid = check_AI_coord_valid(x, y, orientation, ship_type)
        if valid == True:
            break
    place_ship(x, y, orientation, ship_type, player)
    #place battleship
    ship_type = "battleship"
    valid = False
    while valid == False:
        x, y, orientation = generate_random_coords()
        valid = check_AI_coord_valid(x, y, orientation, ship_type)
        if valid == True:
            break
    place_ship(x, y, orientation, ship_type, player)
    #place aircraft carrier
    ship_type = "aircraft carrier"
    valid = False
    while valid == False:
        x, y, orientation = generate_random_coords()
        valid = check_AI_coord_valid(x, y, orientation, ship_type)
        if valid == True:
            break
    place_ship(x, y, orientation, ship_type, player)
    
def AI_missile_fire():
    from random import randrange
    x = randrange(1,11)
    y = randrange(1,11)
    return (x, y)

def missile_fire(player):
    if player == "player":
        print ("Now enter the coordinates at which you want to fire a missile!")
        check = False
        while check == False:
            x = input("Enter the X coordinate at which you want to fire a missile (A - J): ")
            y = int(input("Enter the y coordiante at which you want to fire a missile (1 - 10): "))
            check = input_check(x, y)
            if check == True:
                break
        x = convert_lettercoord_to_num(x)
        
        if opponents_tracking_board.tracking_board[y][x] == 1:
            opponents_board.board[y][x] = "X"
            opponents_tracking_board.tracking_board[y][x] = 0
            print_boards(players_board, opponents_board)
            print ("Your missile hit one of your opponents ships!")
            input("Press enter to continue...")
        elif opponents_tracking_board.tracking_board[y][x] != 1:
            opponents_board.board[y][x] = "0"
            miss_tracking_board[y][x] = 1
            print_boards(players_board, opponents_board)
            print ("You missed your opponents ships!")
            input("Press enter to continue...")
            
    elif player == "AI":
        x, y = AI_missile_fire()
        if players_tracking_board.tracking_board[y][x] == 1:
            players_board.board[y][x] = "X"
            players_tracking_board.tracking_board[y][x] = 0
            print_boards(players_board, opponents_board)
            print ("Your opponent fired... and hit your ship!")
            input("Press enter to continue...")
        elif players_tracking_board.tracking_board[y][x] != 1:
            print_boards(players_board, opponents_board)
            print ("Your opponent fired... and missed your ships.")
            input("Press enter to continue...")
            
def check_win(shot_from):
    opp_dead_number_of_sections = 0
    player_dead_number_of_sections = 0
    if shot_from == "player":
        for i in range(1,11):
            for j in range(1,11):
                if opponents_tracking_board.tracking_board[i][j] == 0:
                    opp_dead_number_of_sections += 1
        if opp_dead_number_of_sections == 17:
            print ("You have hit all of your opponents ships and have won!")
            input("Press enter to continue...")
            win = True
            return win
        elif opp_dead_number_of_sections != 17:
            win = False
            return win
        
    elif shot_from == "AI":
        for i in range(1,11):
            for j in range(1,11):
                if players_tracking_board.tracking_board[i][j] == 0:
                    player_dead_number_of_sections += 1
        if player_dead_number_of_sections == 17:
            print ("The opponent has hit all of your ships and has won!")
            input("Press enter to continue...")
            win = True
            return win
        elif player_dead_number_of_sections != 17:
            win = False
            return win

#Create the player's boards
players_board = Playable_Boards()
players_tracking_board = Board_To_Track_Game()

#Create the opponents boards (Opp is AI so it's only what the player will see)
opponents_board = Playable_Boards()
opponents_tracking_board = Board_To_Track_Game()

#print the empty boards
print_boards(players_board, opponents_board)

#insert users ship's
place_users_ships()

miss_tracking_board = []
for x in range(0,12):
    row = []
    miss_tracking_board.append(row)
    for y in range(0,12):
        column = []
        row.append(column)

#insert AI's ship's
place_AIs_ships()

def game_loop():
    win = False
    while win == False:
        player = "player"
        missile_fire(player)
        win = check_win(player)
        if win == True:
            break

        player = "AI"
        missile_fire(player)
        win = check_win(player)
        if win == True:
            break
            
game_loop()

#-------------------------------------------------
#All working now :)
