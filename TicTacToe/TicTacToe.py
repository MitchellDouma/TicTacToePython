board = [[" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "]]

def ClearBoard():
    board[0][0] = " "
    board[0][2] = " "
    board[0][4] = " "
    board[2][0] = " "
    board[2][2] = " "
    board[2][4] = " "
    board[4][0] = " "
    board[4][2] = " "
    board[4][4] = " "

def UpdateBoard():
    for x in board:
        for y in x:
            print(y, end=" ")
        print()

def GetPlayerPiece(x):
    if(x):
        return "X"
    else:
        return "O"

def CheckWin(xsTurn):
    if(board[0][0] == board[0][2] == board[0][4] and board[0][0] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[2][0] == board[2][2] == board[2][4] and board[2][0] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[4][0] == board[4][2] == board[4][4] and board[4][0] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[0][0] == board[2][0] == board[4][0] and board[0][0] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[0][2] == board[2][2] == board[4][2] and board[0][2] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[0][4] == board[2][4] == board[4][4] and board[0][4] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[0][0] == board[2][2] == board[4][4] and board[0][0] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[0][4] == board[2][2] == board[4][0] and board[0][4] != " "):
        print(GetPlayerPiece(xsTurn) + " won!")
        return True
    elif(board[0][0] != " " and board[0][2] != " " and board[0][4] != " " and board[2][0] != " " and board[2][2] != " " and board[2][4] != " " and board[4][0] != " " and board[4][2] != " " and board[4][4]):
        print("Cat's Game!")
        return True
    else:
        return False

def PlayersTurn(xsTurnBool):
    print("It's " + GetPlayerPiece(xsTurnBool) + "'s Turn!")
    move = input("Type the square you want to place your piece: ")
    if(move == "UL"):
        if(board[0][0] == " "):
            board[0][0] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)       
    elif(move == "UM"):       
        if(board[0][2] == " "):
            board[0][2] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)
    elif(move == "UR"):
        if(board[0][4] == " "):
            board[0][4] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)       
    elif(move == "ML"):
        if(board[2][0] == " "):
            board[2][0] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)      
    elif(move == "MM"):
        if(board[2][2] == " "):
            board[2][2] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)      
    elif(move == "MR"):
        if(board[2][4] == " "):
            board[2][4] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)        
    elif(move == "LL"):
        if(board[4][0] == " "):
            board[4][0] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)       
    elif(move == "LM"):
        if(board[4][2] == " "):
            board[4][2] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)      
    elif(move == "LR"):
        if(board[4][4] == " "):
            board[4][4] = GetPlayerPiece(xsTurnBool)
        else:
            print("That spot is taken")
            UpdateBoard()
            PlayersTurn(xsTurnBool)
    else:
        print("That's not a valid space")
        UpdateBoard
        PlayersTurn(xsTurnBool)
 
    if(not CheckWin(xsTurnBool)):
        UpdateBoard()
        PlayersTurn(not xsTurnBool)
    else:
        playAgain = input("Play Again? Y/N: ")
        if(playAgain == "Y"):
            ClearBoard()
            UpdateBoard()
            PlayersTurn(True)
        else:
            print("ok")

    
UpdateBoard()
PlayersTurn(True)