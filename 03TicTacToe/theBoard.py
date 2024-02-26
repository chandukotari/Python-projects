theBoard={
    '7' : ' ' , '8' : ' ' , '9' :' ',
    '4' : ' ' , '5' : ' ' , '6' :' ',
    '1' : ' ' , '2' : ' ' , '3' :' '
}

def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
#printBoard(theBoard)

def clearBoard(board):
    for key in board:
        board[key]=' '

def game():
    count=0
    turn = 'X'
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")
        
        move=input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+=1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        if count>5:
            if((theBoard['7']== theBoard['8']==theBoard['9']!=' ') or #1st row match
               (theBoard['4']== theBoard['5']==theBoard['6']!=' ') or #2nd row match
               (theBoard['1']== theBoard['2']==theBoard['3']!=' ') or #3rd row match
               (theBoard['7']== theBoard['4']==theBoard['1']!=' ') or #1 column match
               (theBoard['8']== theBoard['5']==theBoard['2']!=' ') or #2 column match
               (theBoard['9']== theBoard['6']==theBoard['3']!=' ') or #3 column match
               (theBoard['7']== theBoard['5']==theBoard['3']!=' ') or #\ match
               (theBoard['9']== theBoard['5']==theBoard['1']!=' ')  #/ match
               ):#top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ******"+turn+" won."+" ******")
                return

            if count == 9:
                print("It's Tie")
                print("!!Game Over!!")
                return
        
        if turn== 'X':
            turn = 'O'
        else:
            turn = 'X'
game()
restart=input("Do you want to play again(Y/N)?")
if restart.lower!='n':
    clearBoard(theBoard)
    game()
    restart=input("Do you want to play again(Y/N)?")