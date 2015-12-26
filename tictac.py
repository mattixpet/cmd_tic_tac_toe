#Tic Tac Toe game created by Matti roughly based on a youtube video
#created: February 2012
#
#url to the video: http://www.youtube.com/watch?v=mMO-spo20jU

import random
import copy

board = [ 0, 1, 2,
          3, 4, 5,
          6, 7, 8 ]
#test board used for hard difficulty
tboard = [ 0, 1, 2,
           3, 4, 5,
           6, 7, 8 ]

result = [ 'u' ] #result of the game

def show():
    print board[0], "|", board[1], "|", board[2]
    print "----------"
    print board[3], "|", board[4], "|", board[5]
    print "----------"
    print board[6], "|", board[7], "|", board[8]

def showt(): #show the test board, used for debugging
    print tboard[0], "|", tboard[1], "|", tboard[2]
    print "----------"
    print tboard[3], "|", tboard[4], "|", tboard[5]
    print "----------"
    print tboard[6], "|", tboard[7], "|", tboard[8]

def boardIsFull():
    cnt = 0
    for i in range(9):
        if board[i] != i:
            cnt += 1
    if cnt == 9:
        return True
    else:
        return False

def checkLine(char,spot1,spot2,spot3):
    return char == board[spot1] and char == board[spot2] and char == board[spot3]

def checkAll(char):
    if checkLine(char,0,1,2):
        return True
    elif checkLine(char,3,4,5):
        return True
    elif checkLine(char,6,7,8):
        return True
    elif checkLine(char,0,3,6):
        return True
    elif checkLine(char,1,4,7):
        return True
    elif checkLine(char,2,5,8):
        return True
    elif checkLine(char,0,4,8):
        return True
    elif checkLine(char,2,4,6):
        return True
    else: 
        return False

def checkForResult():
    r = True;	
    if checkAll('x'):
	result[0] = 'x'        
	return r
    elif checkAll('o'):
 	result[0] = 'o'	
        return r
    elif boardIsFull():
        result[0] = 'd'
        return r
    else:
	return False

#Computer AI
def easy(): #randomly generated
    while True:
        if boardIsFull():
            break
        
        random.seed()
        op = random.randint(0,8)
        
        if (board[op] != 'x' and board[op] != 'o'):
            board[op] = 'o'
            break

def medium(): #wins if two o in a row/ stops user win if two x in a row
    if boardIsFull():
        return

    if checkForTwo('o', board):
        return
    elif checkForTwo('x', board):
        return
    else:
        easy()
        
def hard(): #yeah a copout, but hey, kindof works
    random.seed()
    fate = random.randint(0,323323323)
    if fate > (323323323)/3.0:
        impossible()
    elif fate > 666 and fate < 666666:
        easy()
    else:
        medium()

def impossible(): #name says it all, it allegedly always draws, but does not try to trick you to win
    if boardIsFull():
        return

    if checkForTwo('o', board):
        return
    elif checkForTwo('x', board):
        return
    elif board[4] == 4: #always put in middle if possible
        board[4] = 'o'
        return
    elif onexwin():
        return
    elif board[4] == 'x' and isCorner(): #put in a corner
        cornerlist = corner()
        random.seed()
        op = random.randint(0,len(cornerlist)-1) #random number
        board[cornerlist[op]] = 'o'        
        return
    #these two are not really functioning as desired, but attain the desirable effect
    elif checkForTwoAhead('x'):
        return
    elif checkForTwoAhead('o'):
        return
    else:
        medium()

#onexwin checks the one win I couldnt program to avoid, do it manually
def onexwin():
    # this:
    # 0 x 2
    # 3 o 5
    # 6 7 x
    if (board[0] == 'x'):
        if board[7] == 'x' or board[5] == 'x':
            if board[8] == 8:
                board[8] = 'o'
                return True
            else:
                return False
    elif (board[2] == 'x'):
        if board[3] == 'x' or board[7] == 'x':
            if board[6] == 6:
                board[6] = 'o'
                return True
            else:
                return False
    elif (board[6] == 'x'):
        if board[1] == 'x' or board[5] == 'x':
            if board[2] == 2:
                board[2] = 'o'
                return True
            else:
                return False
    elif (board[8] == 'x'):
        if board[1] == 'x' or board[3] == 'x':
            if board[0] == 0:
                board[0] = 'o'
                return True
            else:
                return False

#checks to see if user can put an x so that next round he'll have two spots to put an x for a win
def checkForTwoAhead(char):
    checked = []
    cnt = 0
    #check how many o's and x's are already
    for i in range(len(board)):
        if board[i] != i:
            cnt += 1

    while True:
        #if we have checked all empty spots we have to break
        if len(checked)+cnt > 8:
            break

        #copy board[elements] into tboard[elements]
        for i in range(len(board)):
            tboard[i] = board[i]

        for i in range(len(tboard)):
            if tboard[i] == i and not(inList(checked,i)):
                tboard[i] = char
                checked.append(i)
                if checkForTwo(char, tboard):
                    pos = differenceOfBoards(tboard,board)
                    if pos < 0 or pos > 8:
                        print "Unexpected error in determining position for computer"
                    else:
                        board[pos] = 'o'
                    return True
                else:
                    break
    return False

#len(b1) == len(b2)
def differenceOfBoards(b1,b2):
    pos = -1
    for i in range(len(b1)):
        if b1[i] != b2[i]:
            return i
    return pos

#er x i listanum listi?
def inList(listi, x):
    for i in range(len(listi)):
        if listi[i] == x:
            return True
    return False

#returns true iff there is an available corner
def isCorner():
    return board[0] == 0 or board[2] == 2 or board[6] == 6 or board[8] == 8

#returns a list of available corners    
def corner():
    list = [ ]
    if board[0] == 0:
        list.append(0)
    if board[2] == 2:
        list.append(2)
    if board[6] == 6:
        list.append(6)
    if board[8] == 8:
        list.append(8)
    return list

def checkForTwo(char,b): #b is current board for testing
    #check all the lines
    if checkTwo(char,0,1,2,b):
        return True
    elif checkTwo(char,3,4,5,b):
        return True
    elif checkTwo(char,6,7,8,b):
        return True
    elif checkTwo(char,0,3,6,b):
        return True
    elif checkTwo(char,1,4,7,b):
        return True
    elif checkTwo(char,2,5,8,b):
        return True
    elif checkTwo(char,0,4,8,b):
        return True
    elif checkTwo(char,2,4,6,b):
        return True
    else: 
        return False

def checkTwo(char,spot1,spot2,spot3, b): # b = current board for testing
    cnt = 0 #char-count
    target = -1
    if (b[spot1] == char):
        cnt += 1
    else:
        target = spot1
    if (b[spot2] == char):
        cnt += 1
    else:
        target = spot2
    if (b[spot3] == char):
        cnt += 1
    else:
        target = spot3

    if (cnt == 2):
        if (target >= 0):
            if char == 'x':
                if b[target] == 'o': #spot taken
                    return False
                b[target] = 'o' # to stop a win from user
            else:
                if b[target] == 'x': #spot taken
                    return False
                b[target] = 'o' # for a win
        else:
            return False

        return True
    else:
        return False

def compare(dif):
    diflist = [ "easy", "medium", "hard", "impossible", "e", "m", "h", "i" ]
    for i in range(len(diflist)):
        if cmp(dif, diflist[i]) == 0:
            return True
    return False

while True:
    difficulty = raw_input("Choose difficuty:\neasy - medium - hard - impossible\n")
    difficulty = str(difficulty)
    if compare(difficulty):
        break
    else:
        print "Wrong input, type in one of the diffuculties"
        continue

while True:
    if checkForResult():
	show()
	break
    else:
	show()	

    input = raw_input("Select a spot: ")
    input = int(input)

    #user's turn
    if (board[input] != 'x' and board[input] != 'o'):
        board[input] = 'x'
	
	if checkForResult():
	    show()
	    break

        #computer's turn
        if (cmp(difficulty,"easy") == 0 or cmp(difficulty,"e") == 0):
            easy()
        elif (cmp(difficulty,"medium") == 0 or cmp(difficulty,"m") == 0):
            medium()
        elif (cmp(difficulty,"hard") == 0 or cmp(difficulty,"h") == 0):
            hard()
        elif (cmp(difficulty,"impossible") == 0 or cmp(difficulty,"i") == 0):
            impossible()
    else:
        print "That spot is taken!"

if result[0] == 'x':
    print '~~ X wins! ~~'
    if (cmp(difficulty,"impossible") == 0 or cmp(difficulty,"i") == 0):
        print "You won the impossible difficulty!?\nDang it, I need to improve my AI making skills."
elif result[0] == 'o':
    print '~~ O wins! ~~'
elif result[0] == 'd':
    print '~~ Draw! ~~'
else:
    print 'Unexpected outcome of game'

