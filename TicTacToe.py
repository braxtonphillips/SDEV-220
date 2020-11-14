"""
Braxton Phillips
SDEV 220
Chapter 11 Exercise 11.9
Due Nov 14, 2020
"""

Active = 0 
boardPosition = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1 #initialize player value for in/decrementing         
Stop = 1
Tie = -1
Game = Active    
Mark = ''
Win = 1  
   
#Draw board & assign positions
def drawBoard():    
    print("|  %s  |  %s  |  %s  |" % (boardPosition[1], boardPosition[2], boardPosition[3])) #using % as a conversion specifier, puts positon number in place of string 
    print("-------------------")    
    print("|  %s  |  %s  |  %s  |" % (boardPosition[4], boardPosition[5], boardPosition[6]))    
    print("-------------------")    
    print("|  %s  |  %s  |  %s  |" % (boardPosition[7], boardPosition[8], boardPosition[9]))    
    print("-------------------")    
   
#This Function Checks position is empty or not    
def checkPosition(x):    
    if(boardPosition[x] == ' '):    
        return True    
    else:    
        return False    
   
#func checks every turn to see if a winning move has been made
def winResults():
    
    global Game    
    #row win   
    if(boardPosition[1] == boardPosition[2] and boardPosition[2] == boardPosition[3] and boardPosition[1] != ' '):    
        Game = Win    
    elif(boardPosition[4] == boardPosition[5] and boardPosition[5] == boardPosition[6] and boardPosition[4] != ' '):    
        Game = Win    
    elif(boardPosition[7] == boardPosition[8] and boardPosition[8] == boardPosition[9] and boardPosition[7] != ' '):    
        Game = Win
        
    #column win
    elif(boardPosition[1] == boardPosition[4] and boardPosition[4] == boardPosition[7] and boardPosition[1] != ' '):    
        Game = Win    
    elif(boardPosition[2] == boardPosition[5] and boardPosition[5] == boardPosition[8] and boardPosition[2] != ' '):    
        Game = Win    
    elif(boardPosition[3] == boardPosition[6] and boardPosition[6] == boardPosition[9] and boardPosition[3] != ' '):    
        Game = Win 
        
    #diagonal win
    elif(boardPosition[1] == boardPosition[5] and boardPosition[5] == boardPosition[9] and boardPosition[5] != ' '):    
        Game = Win    
    elif(boardPosition[3] == boardPosition[5] and boardPosition[5] == boardPosition[7] and boardPosition[5] != ' '):    
        Game = Win
        
    #tie   
    elif(boardPosition[1]!=' ' and boardPosition[2]!=' ' and boardPosition[3]!=' ' and boardPosition[4]!=' ' and boardPosition[5]!=' ' and boardPosition[6]!=' ' and boardPosition[7]!=' ' and boardPosition[8]!=' ' and boardPosition[9]!=' '):    
        Game = Tie    
    else:            
        Game = Active    
    
print("~~~~~~~~~~~~Tic-Tac-Toe~~~~~~~~~~~~\n")    
print("Player 1 is X & Player 2 is O\n")
print("Sample Board\t\t|  1  |  2  |  3  |")
print("\t\t\t|  4  |  8  |  6  |")
print("\t\t\t|  7  |  8  |  9  |")
print("Let's Play")

#Runs game while status hasnt ben returned
while(Game == Active):    
    drawBoard()    
    if(player % 2 != 0): #using modulo to evaluate which players turn it is. only 2 will return an int   
        print("\nPlayer 1's turn")    
        Mark = 'X'    
    else:    
        print("\nPlayer 2's turn")    
        Mark = 'O'    
    choice = int(input("Enter desired position, using an integer, between 1-9 that the player wishes to claim: "))    
    if(checkPosition(choice)): #reads player input
        boardPosition[choice] = Mark #assigns integer choice to the board position    
        player += 1    #increments to player 2 
        winResults()    
        
drawBoard()

#game results
if (Game == Tie):    
    print("Tied Game. There is no winner.")    
elif (Game == Win):    
    player -= 1 #decrements back to player 1    
    if (player % 2 != 0):
        print("\n########################") #flash and trash
        print("#Player 1 is the winner#")
        print("########################")
    else:    
        print("\n########################")
        print("#Player 2 is the winner#")
        print("########################")