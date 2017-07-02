
# coding: utf-8

# In[ ]:

#creates a blank board to play on
def print_board():
    split = " "
    print (split)
    for element in board:
        print (" | ".join(element))
        print(" | ")
    print (split)
    
board = [["3","-","-","-"],
         ["2","-","-","-"],
         ["1","-","-","-"],
         [" ","1","2","3"]]
            
def check_win():
    for c in range(0,3):
        #check rows for win
        if board[c][1] == "X" and board[c][2] == "X" and board[c][3] == "X":
            print (" ")
            print ("%s has won!" % (player1))
            win = True
            return win
        elif board[c][1] == "O" and board[c][2] == "O" and board[c][3] == "O":
            print (" ")
            print ("%s has won!" % (player2))
            win = True
            return win
    for c in range(1,4):
        #check columns for win
        if board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X":
            print (" ")
            print ("%s has won!" % (player1))
            win = True
            return win
        elif board[0][c] == "O" and board[1][c] == "O" and board [2][c] == "O":
            print (" ")
            print ("%s has won!" % (player2))
            win = True
            return win
        #check diagonals for win
        #right to left
        elif board[0][3] == "X" and board[1][2] == "X" and board[2][1] == "X":
            print (" ")
            print ("%s has won!" % (player1))
            win = True
            return win
        elif board[0][3] == "O" and board[1][2] == "O" and board[2][1] == "O":
            print (" ")
            print ("%s has won!" % (player2))
            win = True
            return win
        #left to right
        elif board[0][1] == "X" and board[1][2] == "X" and board[2][3] == "X":
            print (" ")
            print ("%s has won!" % (player1))
            win = True
            return win
        elif board[0][1] == "O" and board[1][2] == "O" and board[2][3] == "O":
            print (" ")
            print ("%s has won!" % (player2))
            win = True
            return win
    else:
        win = False
        return win
        
num_convert = {1: 3, 2: 2, 3:1}

def player_1_turn(col, row):
    row = num_convert[row]
    board[row-1][col] = "X"
       
def player_2_turn(col, row):
    row = num_convert[row]
    board[row-1][col] = "O"
    
def input_check(column, row):
    row = num_convert[row]
    if row <= 0 or row >= 4:
        print ("The row you entered is not valid!")
        return False
    if column <= 0 or column >= 4:
        print ("The column you entered is not valid!")
        return False
    if board[row-1][column] == "X" or board[row-1][column] == "O":
        print ("That space has already been played!")
        return False
    return True
        
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")
print (" ")
print ("Hello %s and %s, welcome to Liam's Noughts and Crosses game!" % (player1, player2))
print ("In order to play, you will be asked to input the column number\nand row number of the area you wish to place a nought, or a cross.")
print (" ")
print ("REMEMBER:\nYOU WILL BE ASKED TO INPUT A COLUMN NUMBER FIRST (HORIZONTAL ACROSS THE GRID)\nAND A ROW NUMBER SECOND (VERTICAL UP THE GRID).")
print (" ")
print ("Have fun! - Liam")
print (" ")

win = False
turn = 0

print (print_board())
while (win == False):
    #player 1's turn
    column = int(input("%s: Enter the column you wish to select (1 - 3): " % (player1)))
    row = int(input("%s: Enter the row you wish to select (1 - 3): " % (player1)))
            
    check = input_check(column, row)
    while check == False:
        column = int(input("%s: Enter the column you wish to select (1 - 3): " % (player1)))
        row = int(input("%s: Enter the row you wish to select (1 - 3): " % (player1)))
        check = input_check(column, row)
            
    player_1_turn(column, row)
    turn += 1
    
    if check_win() == True: 
        break
        
    if turn == 9:
        print (" ")
        print ("The game has resulted in a draw!")
        break
        
    print_board()
    
    #player 2's turn
    column = int(input("%s: Enter the column you wish to select (1 - 3): " %(player2)))
    row = int(input("%s please enter the row you wish to select (1 - 3): " % (player2)))
    
    check = input_check(column, row)
    while check == False:
        column = int(input("%s: Enter the column you wish to select (1 - 3): " % (player2)))
        row = int(input("%s: Enter the row you wish to select (1 - 3): " % (player2)))
        check = input_check(column, row)
            
    player_2_turn(column, row)
    turn += 1
    
    if check_win() == True: 
        break
        
    print_board()
    
print (" ")
print_board()

input()

#Check function is not checking columns 2 and 3
#Checks column 1 okay...

#Else statement was inside the for loop
#needed taking back an indent in order for it to run if none of the criteria in the loop was met


# In[ ]:



